import lejos.nxt.*;
import lejos.nxt.comm.*;
import lejos.robotics.navigation.*;

import java.io.*;
import java.util.EmptyQueueException;

/**
 * The main class for running the robot. Responsible for monitoring
 * the bluetooth connection, transforming received packets into 
 * commands and executing the commands. Also responsible for monitoring
 * the touch sensors and reacting appropriately when they are pressed.
 * 
 * @author Stephen McGruer
 */
public class RobotMain {

  /* Wheel diameter and track width are used by the SDPPilot for
   * precise movement. */
  public static final float WHEEL_DIAMETER = 8.16f;
  public static final float TRACK_WIDTH = 12.7f;

  /* Standard movement, turn and kick speeds. Movement and
   * turn speeds given in cm/s, kick speed given in voltage
   * to the motor. */
  public static final int MOVE_SPEED = 30;
  public static final int TURN_SPEED = 90;
  public static final int KICK_SPEED = 900;

  /* Constants for the commands. We used to use Enums but ran into
   * some weird problems with them identifying as the wrong enum so
   * stopped. */
  public static final int QUIT = 0;
  public static final int FORWARD = 1;
  public static final int BACKWARD = 2;
  public static final int STOP = 3;
  public static final int LEFT = 4;
  public static final int RIGHT = 5;
  public static final int KICK = 6;
  public static final int SETLEFTMOTOR = 7;
  public static final int SETRIGHTMOTOR = 8;

  /* Used when a touch sensor is activated, to override normal
   * action. */
  private boolean overrideMode;

  /* Flag for notifying the sensor and command threads that they
   * should shut down. */
  private boolean shutdownFlag;

  /* Holds the currently executing command. */
  private Command currentCommand;

  /**
   * Default constructor.
   */
  public RobotMain() {
    this.overrideMode = false;
    this.shutdownFlag = false;
  }

  /**
   * The main thread. Sets up the bluetooth connection to the PC and then 
   * monitors the connection until a "shutdown" signal is received.
   *
   * @throws IOException          If an IO exception occurs, for example when 
   *                              closing the DataInputStream.
   * @throws InterruptedException If we are interrupted when joining the command
   *                              thread.
   */
  public void go() throws IOException, InterruptedException {

    /* Open the connection and data transfer streams. */
    System.out.println("Waiting for a connection...");
    NXTConnection conn = Bluetooth.waitForConnection();
    DataInputStream din = conn.openDataInputStream();
    System.out.println("Connected!");

    /* Use if we need to communicate the other way too. */
    /* DataOutputStream dout = conn.openDataOutputStream(); */

    /* The command queue holds the list of commands to execute. */
    ConcurrentQueue<Command> commandQueue = new ConcurrentQueue<Command>();

    /* Touch sensors. */
    TouchSensor frontRightTouchSensor = new TouchSensor(SensorPort.S1);
    TouchSensor frontLeftTouchSensor = new TouchSensor(SensorPort.S2);

    /* Create a new SDP pilot class to pilot the robot. */
    SDPPilot pilot = new SDPPilot(WHEEL_DIAMETER, TRACK_WIDTH, 
                         Motor.B, Motor.A, Motor.C, true);

    /* Robot speeds. All very theoretical, what you actually get is dependent on
     * power levels. */
    pilot.setSpeed(500);
    pilot.setKickerSpeed(KICK_SPEED);

    /* Start the CommandChecker thread, which scans for new commands and adds
     * them to the queue. */
    CommandChecker commandChecker = new CommandChecker(commandQueue, din);
    commandChecker.start();

    /* Start the SensorMonitor thread, which monitors the sensors and activates
     * the override if they are touched. */
    SensorMonitor sensorMonitor = new SensorMonitor(pilot, commandQueue, 
        frontLeftTouchSensor, frontRightTouchSensor);
    sensorMonitor.start();

    /* Until ready to shut down, continously pop commands from the queue and
     * execute them. */
    while(!shutdownFlag) {

      if (!commandQueue.isEmpty() && !overrideMode) {

        /* We can't be sure that there is actually something in the queue, due 
         * to concurrency (the touch sensor monitor may strip the command queue
         * between the "if" and the following lines. In truth we should use a
         * synchronized statement here, but this works too. */
        try {
          
          currentCommand = (Command) commandQueue.pop();
          short argument = currentCommand.getArgument();
          boolean hasArgument = currentCommand.hasArgument();

          StringBuffer debugBuffer = new StringBuffer();

          switch (currentCommand.getType()) {

            case QUIT:

              debugBuffer.append("QUIT.");

              /* Shutdown flag tells all threads to finish. */
              shutdownFlag = true;

              break;

            case FORWARD: 

              debugBuffer.append("FORWARD.");

              if (hasArgument) {
                debugBuffer.append("\n  Arg: " + argument + ".");

                pilot.forward(argument);
              } else {
                pilot.forward();
              }

              break;

            case BACKWARD: 

              debugBuffer.append("BACKWARD.");

              if (hasArgument) {
                debugBuffer.append("\n  Arg: " + argument + ".");

                pilot.backward(argument);
              } else {
                
                pilot.backward();
              }

              break;

            case STOP: 

              debugBuffer.append("STOP.");

              pilot.stop();

              break;

            case LEFT: 

              debugBuffer.append("LEFT.");

              if (hasArgument) {
                debugBuffer.append("\n  Arg: " + argument + ".");

                pilot.left(argument);
              } else {
                pilot.left();
              }

              break;
                
            case RIGHT:

              debugBuffer.append("LEFT.");

              if (hasArgument) {
                debugBuffer.append("\n  Arg: " + argument + ".");

                pilot.right(argument);
              } else {
                pilot.right();
              }
              break;

            case KICK:

              debugBuffer.append("KICK.");

              pilot.shoot();

              break;

            case SETLEFTMOTOR:

              debugBuffer.append("SETLEFTMOTOR.\n  Arg: " + 
                  argument + ".");

              pilot.setLeftMotorSpeed(argument);

              break;

            case SETRIGHTMOTOR:

              debugBuffer.append("SETRIGHTMOTOR.\n  Arg: " + 
                  argument + ".");

              pilot.setRightMotorSpeed(argument);

              break;

            default: 

              /* Unrecognised command. */
              debugBuffer.append("Error: Unrecog command - " + 
                  currentCommand.getType());

              break;

          }

          System.out.println(debugBuffer.toString());


        } catch (EmptyQueueException eqe) {
          /* Ignore these exceptions. */
        }

        Thread.yield();

      }

    }
  
    pilot.stop();

    /* Wait for the other threads to terminate. */
    commandChecker.join();
    sensorMonitor.join();

  }

  /**
   * The main method for the class. Creates a new RobotMain instance and
   * runs it.
   *
   * @param args    The program arguments. Not used.
   */
  public static void main(String[] args) {

    RobotMain mainThread = new RobotMain();
    try {
      mainThread.go();
    } catch (IOException e) {
      System.out.println("IOException!");
    } catch (InterruptedException e) {
      System.out.println("InterruptedException!");
    }

    System.out.println("Ready to finish.");
    Button.waitForPress();

  }

  /**
   * The CommandThread class constantly checks for commands being sent over
   * the DataInputStream from the PC, and notifies the main thread when a new
   * command arrives. If the recieved command is an extended command, records
   * this information too.
   *
   * Currently not very concurrent safe.
   *
   * @author Stephen McGruer
   */
  private class CommandChecker extends Thread {

    /* A queue for holding commands - we push new commands here. */
    ConcurrentQueue<Command> commandQueue;

    /* The incoming Bluetooth datastream. */
    DataInputStream din;

    /* Temporary storage for commands. */
    Command newCommand;

    /**
     * Default constructor.
     *
     * @param commandQueue    The queue of commands the robot must execute.
     * @param din             The incoming Bluetooth datastream.
     */
    public CommandChecker(ConcurrentQueue<Command> commandQueue,
                          DataInputStream din) {
      this.commandQueue = commandQueue;
      this.din = din;
    }

    /**
     * The main run method for the thread. Waits for input from the PC,
     * then creates a new command and pushes it onto the command queue.
     */
    public void run() {

      /* shutdownFlag is a global flag indicating when we should stop
       * receiving commands. */
      while(!shutdownFlag) {

        /* There is no way to tell if the connection is dead other than to try
         * and read something and see if we get thrown an IOException. */
        try {

          /* The new command. This thread will block here. */
          int command = din.readInt();

          /* Command packets are split in two - the upper 16 bits are the
           * command type, and the lower 16 bits are the command argument. */
          int type = command >>> 16;
          short argument = (short) command;

          /* Commands don't have to have arguments. */
          if (argument != 0) {
            newCommand = new Command(type, argument);
          } else {
            newCommand = new Command(type);
          }

          /* When the touch sensor override is in play we ignore all commands,
           * except for quit commands. */
          if (!overrideMode || type == QUIT) {

            /* Kick commands have priority. */
            if (type == KICK) {
              commandQueue.insertElementAt(newCommand, 0);
            } else {
              commandQueue.push(newCommand);
            }

          }

          /* Type '0' is the finish command. */
          if (type == QUIT) {
            break;
          }

          /* Try not to spam commands onto the thread... */
          Thread.yield();

        } catch (IOException e) {

          System.out.println("IOException (reading command).");
          
          /* We want to quit in this situation, so push a quit command onto
           * the queue. */
          newCommand = new Command(QUIT);
          commandQueue.push(newCommand);

          break;

        }

      }

    }


  }

  /**
   * The SensorMonitor class constantly checks the touch sensors for collisions
   * and reacts appropriately. Currently the reaction is to strip the command
   * queue of commands, move backwards for a short period of time and then 
   * resume the previously executing command. (It is assumed that the AI will
   * then override this command for the new situation.)
   *
   * @author Stephen McGruer
   */
  private class SensorMonitor extends Thread {

    /* The SDPPilot that controls the robot. */
    SDPPilot pilot;

    /* The queue of commands. We need this here so we can strip it when
     * a sensor input is detected. */
    ConcurrentQueue<Command> commandQueue;

    /* The touch sensors. */
    TouchSensor frontLeftSensor;
    TouchSensor frontRightSensor;

    /**
     * Default constructor.
     *
     * @param pilot             The SDPPilot that is controlling the robot.
     * @param commandQueue      The queue of commands that the robot is 
     *                          executing.
     * @param frontLeftSensor   The front-left touch sensor on the robot.
     * @param frontRightSensor  The front-right touch sensors on the robot.
     */
    public SensorMonitor(SDPPilot pilot, ConcurrentQueue<Command> commandQueue, 
        TouchSensor frontLeftSensor, TouchSensor frontRightSensor) {

      this.pilot = pilot;
      this.commandQueue = commandQueue;
      this.frontLeftSensor = frontLeftSensor;
      this.frontRightSensor = frontRightSensor;

    }

    /**
     * The main run method for the thread. Constantly monitors sensor inputs,
     * waiting for a collision. When a collision is detected the thread strips
     * the command queue of any commands, moves backwards for a short while and
     * then resumes the previously executing command.
     */
    public void run() {

      /* shutdownFlag is a global flag indicating when we should stop
       * receiving commands. */
      while(!shutdownFlag) {

        /* Check for a sensor press. */
        if ((frontLeftSensor.isPressed() || frontRightSensor.isPressed())) {

          /* Set override mode on. */
          overrideMode = true;

          /* Empty the command queue */
          synchronized(commandQueue) {
            while(!commandQueue.isEmpty()) {
              commandQueue.pop();
            }
          }

          /* React to the front sensors being pressed. */
          reactToFrontSensors();

          /* Push on a stop command. */
          commandQueue.push(new Command(STOP));

          /* Our override is finished. */
          overrideMode = false;

        }

      }

    }

    /**
     * Reacts to either of the front sensors being pressed. Reverses for 0.5
     * seconds, away from the collision.
     */
    private void reactToFrontSensors() {

      pilot.stop();

      pilot.setLeftMotorSpeed(500);
      pilot.setRightMotorSpeed(500);

      pilot.backward();

      try { Thread.sleep(500); } catch (InterruptedException ie) { }

      pilot.stop();

    }

  }

}
