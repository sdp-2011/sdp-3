import lejos.nxt.*;
import lejos.nxt.comm.*;
import lejos.robotics.navigation.*;

import java.io.*;
import java.util.EmptyQueueException;

/**
 * @author Stephen McGruer
 */
public class SensorTest {

  public static final float WHEEL_DIAMETER = 8.16f;
  public static final float TRACK_WIDTH = 12.7f;
  public static final int MOVE_SPEED = 30;
  public static final int TURN_SPEED = 180;
  public static final int KICK_SPEED = 900;

  private boolean overrideMode;

  /** Class constructor. */
  public SensorTest() {
    this.overrideMode = false;
  }

  public void go() throws IOException, InterruptedException {

    /* Touch sensors. */
    TouchSensor frontRightTouchSensor = new TouchSensor(SensorPort.S1);
    TouchSensor frontLeftTouchSensor = new TouchSensor(SensorPort.S2);

    /* Create a new SDP pilot class to pilot the robot. */
    SDPPilot pilot = new SDPPilot(WHEEL_DIAMETER, TRACK_WIDTH, 
                         Motor.B, Motor.A, Motor.C, true);

    /* Robot speeds. All very theoretical, what you actually get is dependent on
     * power levels. */
   // pilot.regulateSpeed(true);
   // pilot.setMoveSpeed(MOVE_SPEED);
   // pilot.setTurnSpeed(TURN_SPEED);
   // pilot.setKickerSpeed(KICK_SPEED);
    pilot.setSpeed(700);

    /* Start the SensorMonitor thread, which monitors the sensors and activates the
     * override if they are touched. */
    SensorMonitor sensorMonitor = new SensorMonitor(pilot, frontLeftTouchSensor, frontRightTouchSensor);
    sensorMonitor.start();

    /* Until ready to shut down continously pop commands off of the queue and execute them. */
    pilot.forward();
    while(!overrideMode);

  }

  /**
   * The main control method for the class. Controls all aspects of robot
   * movement based on the commands recieved, including the overrides sent
   * by the touch sensors.
   *
   * @author Stephen McGruer
   *
   * @param args                  The program arguments. Not used.
   *
   * @throws IOException          If an IO exception occurs, for example when 
   *                              closing the DataInputStream.
   * @throws InterruptedException If we are interrupted when joining the command
   *                              thread.
   */
  public static void main(String[] args) {

    SensorTest mainThread = new SensorTest();
    try {
      mainThread.go();
    } catch (IOException e) {
      System.out.println("IOException!");
    } catch (InterruptedException e) {
      System.out.println("InterruptedException!");
    }

  }

  private class SensorMonitor extends Thread {

    SDPPilot pilot;
    TouchSensor frontLeftSensor;
    TouchSensor frontRightSensor;

    public SensorMonitor(SDPPilot pilot,
        TouchSensor frontLeftSensor, TouchSensor frontRightSensor) {

      this.pilot = pilot;
      this.frontLeftSensor = frontLeftSensor;
      this.frontRightSensor = frontRightSensor;

    }

    public void run() {

      while(!overrideMode) {

        if ((frontLeftSensor.isPressed() || frontRightSensor.isPressed()) && !overrideMode) {
          
          System.out.println("SENSOR PRESSED!");

          /* Set override mode on. */
          overrideMode = true;

          reactToFrontSensors();

        }

      }

    }

    // NOP
    private void reactToFrontSensors() {
      System.out.println("REVERSING");
      pilot.backward();
      System.out.println("REVERSED");
    }

  }

}
