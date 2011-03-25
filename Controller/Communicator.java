import lejos.nxt.*;
import lejos.nxt.remote.*;
import lejos.pc.comm.*;

import java.io.*;
import java.lang.Thread;

/**
 * Communicates to the Robot via bluetooth connection.
 *
 * @author Daniel Holden
 * @author Stephen McGruer
 */
public class Communicator {

  public static final String BOT_NAME = "BotTheThird";
  public static final String BOT_MAC_ADDRESS = "00:16:53:07:75:31";

  private lejos.pc.comm.NXTComm mBlueToothLink;
  private NXTInfo mNxtInfo;
  private DataOutputStream mOutStream;
  public static DataInputStream mInStream;

  private boolean mConnected;

  /**
   * The constructor for the Communicator class sets up and opens the bluetooth 
   * link to the robot, and opens a DataOutputStream for sending instructions.
   *
   * @throws NXTCommException
   */
  public Communicator() throws NXTCommException {
    
    System.out.println("Constructing communicator.");
    
    mConnected = false;

    mBlueToothLink = NXTCommFactory.createNXTComm(NXTCommFactory.BLUETOOTH);
    mNxtInfo = new NXTInfo(NXTCommFactory.BLUETOOTH, BOT_NAME, BOT_MAC_ADDRESS);

  }

  /**
   * Attempts to connect to the robot.
   */  
  public void connect() {

    System.out.println("Connecting to the robot.");
  
    try {

      /* Open the bluetooth link. */
      System.out.println("Opening...");
      mBlueToothLink.open(mNxtInfo); 
      System.out.println("Opened!");

      /* Open an outgoing and incoming datastream for two way communication. */
      mOutStream = new DataOutputStream(mBlueToothLink.getOutputStream());
      mInStream = new DataInputStream(mBlueToothLink.getInputStream());

      mConnected = true;

    } catch (NXTCommException e) {

      System.err.println("Could not connect:" + e.getMessage());

    }
  }
  
  
  /**
   * Attempts to disconnect from the robot gracefully.
   */  
  public void disconnect() {
  
    System.out.println("Disconnecting from Robot");
  
    try {

      shutDownRobot();
      
      mOutStream.close();
      mBlueToothLink.close();
      mConnected = false;

    } catch (IOException e) {
      System.err.println("Could not disconnect:" + e.getMessage());
    }

  }

  /**
   * Returns whether or not the robot is currently connected.
   *
   * @return      True if the robot is connected, false otherwise.
   */
  public boolean isConnected() {
    return mConnected;
  }
  
  /**
   * Sends an integer command over the DataOutputStream.
   *
   * @throws IOException    If there is an exception while writing the
   *                        command or flushing the pipe.
   */
  public void sendRawInt(int i) throws IOException {
    System.out.println("Sending int: " + i);
    mOutStream.writeInt(i);
    mOutStream.flush();
  }

  /**
   * Sends a float command over the DataOutputStream
   *
   * @throws IOException    If there is an exception when writing the
   *                        command or flushing the pipe.
   */
  public void sendRawFloat(float i) throws IOException {
    mOutStream.writeFloat(i);
    mOutStream.flush();
  }

  /**
   * Send a 'set left motor speed' command.
   *
   * @param speed           The speed to set the left motor to.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void setLeftMotorSpeed(int speed) throws IOException {
    System.out.println("Sending command: Set Left Motor Speed.");
    sendRawInt(constructCommand(Command.SETLEFTMOTOR, speed));
  }

  /**
   * Send a 'set right motor speed' command.
   *
   * @param speed           The speed to set the right motor to.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void setRightMotorSpeed(int speed) throws IOException {
    System.out.println("Sending command: Set Right Motor Speed.");
    sendRawInt(constructCommand(Command.SETRIGHTMOTOR, speed));
  }
  
  /**
   * Send a 'forward' command.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void forward() throws IOException {
    System.out.println("Sending command: Forward.");
    sendRawInt(constructCommand(Command.FORWARD));
  }
  
  /**
   * Send a 'forward' command, with a speed argument.
   *
   * @param speed           The speed to move forward at.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void forward(float speed) throws IOException {
    System.out.println("Sending command: Forward.");
    sendRawInt(constructCommand(Command.FORWARD, (int) speed));
  }
  
  /**
   * Send a 'backward' command.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void backward() throws IOException {
    System.out.println("Sending command: Reverse.");
    sendRawInt(constructCommand(Command.BACKWARD));
  }  

  /**
   * Send a 'backward' command, with a speed argument.
   *
   * @param speed           The speed to move backward at.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void backward(float speed) throws IOException {
    System.out.println("Sending command: Reverse.");
    sendRawInt(constructCommand(Command.BACKWARD, (int) speed));
  }  
  
  /**
   * Send a 'stop' command.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void stop() throws IOException {
    System.out.println("Sending command: Stop.");
    sendRawInt(constructCommand(Command.STOP));
  }    
  
  /**
   * Send a 'turn left' command.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void left() throws IOException {
    System.out.println("Sending command: Turn Left.");
    sendRawInt(constructCommand(Command.LEFT));
  }
  
  /**
   * Send a 'turn left' command, with a speed argument.
   *
   * @param speed           The speed to turn left at.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void left(float speed) throws IOException {
    System.out.println("Sending command: Turn Left.");
    sendRawInt(constructCommand(Command.LEFT, (int) speed));
    // We just... assume. Yeah. >_>.
  }
  
  /**
   * Send a 'turn right' command.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void right() throws IOException {
    System.out.println("Sending command: Turn Right.");
    sendRawInt(constructCommand(Command.RIGHT));
  }
  
  /**
   * Send a 'turn right' command, with a speed argument.
   *
   * @param speed           The speed to turn right at.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void right(float speed) throws IOException {
    System.out.println("Sending command: Turn Right.");
    sendRawInt(constructCommand(Command.RIGHT, (int) speed));
    // We just... assume. Yeah. >_>.
  }
  
  /**
   * Send a 'shoot' command.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void shoot() throws IOException {
    System.out.println("Sending command: Shoot.");
    sendRawInt(constructCommand(Command.KICK));
  }

  /**
   * Sends the 'shut down' command to the robot over the 
   * DataOutputStream.
   *
   * @throws IOException    If there is an exception when sending
   *                        the command.
   */
  public void shutDownRobot() throws IOException {
    System.out.println("Sending command: Shutdown.");
    sendRawInt(constructCommand(Command.QUIT));
  }

  /**
   * Creates a command from a type.
   *
   * @param type  The type of the command.
   * 
   * @return      The command code, which is the type shifted 
   *              left 16 bits.
   */
  public int constructCommand(Command type) {

    /* Type occupies the top 16 bits of the command int. */
    int command = type.getIndex() << 16;

    System.out.println("Command is " + command);

    return command;
  }

  /**
   * Creates a command from a type and an argument
   *
   * @param type        The type of the command.
   * @param argument    The argument for the command.
   * 
   * @return            The command code, which is the type shifted 
   *                    left 16 bits and ORed with the argument (which
   *                    has been shortened to be only 16 bits.)
   */
  public int constructCommand(Command type, int argument) {

    /* Type occupies the top 16 bits of the command int,
     * the argument the lower 16 bits. */
    System.out.println("Constructing command for type " + type + ", argument " + argument);
    int command = (type.getIndex() << 16) | (argument & 0x0000FFFF);

    return command;

  }

}
