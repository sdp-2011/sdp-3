import Ice.*;

/**
 * The ControllerI class represents the topic interface.
 * It must implement all functions listed in Control.ice
 *
 * It sends commands via the bluetooth adapter class (Communicator)
 * to achieve this.
 *
 *
 * @author Daniel Holden
 * @author Stephen McGruer
 */
public class ControllerI extends ControlTopic._ControlDisp {

  private Communicator mCom;

  /**
   * The constructor for the ControllerI class simply creates the Communicator
   * needed to send commands to the robot.
   */
  public ControllerI() {

    System.out.println("Building Communication Interface.");

    /* Try to construct bluetooth communicator */
    try {

      mCom = new Communicator();

    } catch (Exception e) {

      System.err.println("Could not create Communicator: " + e.getMessage());

    }
  }

  /**
   * Implements the sendInt method from the ICE interface, which sends an
   * integer (representing a command) to the robot.
   *
   * @param i          The int to send to the robot.
   * @param current    Information about the current method invocation.
   */
  public void sendInt(int i, Ice.Current current) {

    try {

      mCom.sendRawInt(i);

    } catch (Exception e) {

      System.err.println("Could not send int: " + e.getMessage());
      connect(current);

    }
  }

  /**
   * Implements the shutDownRobot method from the ICE interface, which
   * sends the shutdown command to the robot.
   *
   * @param current    Information about the current method invocation.
   */
  public void shutDownRobot(Ice.Current current) {

    try {

      mCom.shutDownRobot();

    } catch (Exception e) {

      System.err.println("Could not shut down robot: " + e.getMessage());
      connect(current);

    }
  }

  /**
   * Attempts to open the bluetooth connection.
   *
   * @param current    Information about the current method invocation.
   */
  public void connect(Ice.Current current) {
    mCom.connect();
  }

  /** 
   * Reports if the robot is moving or not. Currently unimplemented.
   *
   * @param current     Information about the current method invocation.
   *
   * @return            True if the robot is moving, false otherwise.
   */
  public boolean isMoving(Ice.Current current) {
    return false;
  }

  /**
   * Attempts to close the bluetooth connection.
   *
   * @param current    Information about the current method invocation.
   */
  public void disconnect(Ice.Current current) {
    mCom.disconnect();
  }

  /**
   * Sets the robot's left motor speed. 
   *
   * @param speed       The speed to set the left motor to.
   * @param current     Information about the current method invocation.
   */
  public void setLeftMotorSpeed(int speed, Ice.Current current) {

    try {

      mCom.setLeftMotorSpeed(speed);

    } catch (Exception e) {

      System.err.println("Could not set left motor speed: " + e.getMessage());
      connect(current);

    }
  }
  
  /**
   * Sets the robot's right motor speed. 
   *
   * @param speed       The speed to set the right motor to.
   * @param current     Information about the current method invocation.
   */
  public void setRightMotorSpeed(int speed, Ice.Current current) {

    try {

      mCom.setRightMotorSpeed(speed);

    } catch (Exception e) {

      System.err.println("Could not set right motor speed: " + e.getMessage());
      connect(current);

    }
  }

  /**
   * Instructs the robot to drive forward.
   *
   * @param current   Information about the current method invocation.
   */
  public void driveForward(Ice.Current current) {

    try {

      mCom.forward();

    } catch (Exception e) {

      System.err.println("Could not drive forward:" + e.getMessage());
      connect(current);

    }
  }
  
  /**
   * Instructs the robot to drive forward at a certain speed.
   *
   * @param speed     The speed to drive at.
   * @param current   Information about the current method invocation.
   */
  public void driveForwardSpeed(int speed, Ice.Current current) {

    try {

      mCom.forward(speed);

    } catch (Exception e) {

      System.err.println("Could not drive forward:" + e.getMessage());
      connect(current);

    }
  }
  
  /**
   * Instructs the robot to drive backward.
   *
   * @param current   Information about the current method invocation.
   */
  public void driveBackward(Ice.Current current) {
    try {

      mCom.backward();

    } catch (Exception e) {

      System.err.println("Could not drive backward:" + e.getMessage());
      connect(current);

    }
  }

  /**
   * Instructs the robot to drive backward at a certain speed.
   *
   * @param speed     The speed to drive at.
   * @param current   Information about the current method invocation.
   */
  public void driveBackwardSpeed(int speed, Ice.Current current) {

    try {

      mCom.backward(speed);

    } catch (Exception e) {

      System.err.println("Could not drive backward:" + e.getMessage());
      connect(current);

    }
  }

  /**
   * Instructs the robot to stop.
   *
   * @param current   Information about the current method invocation.
   */
  public void driveStop(Ice.Current current) {

    try {

      mCom.stop();

    } catch (Exception e) {

      System.err.println("Could not stop robot:" + e.getMessage());
      connect(current);

    }
  }
  
  /**
   * Instructs the robot to turn left.
   *
   * @param current   Information about the current method invocation.
   */
  public void turnLeft(Ice.Current current) {

    try {

      mCom.left();

    } catch (Exception e) {

      System.err.println("Could not turn left:" + e.getMessage());
      connect(current);

    }
  }  
  
  /**
   * Instructs the robot to turn left at a certain speed.
   *
   * @param speed     The speed to turn at.
   * @param current   Information about the current method invocation.
   */
  public void turnLeftSpeed(int speed, Ice.Current current) {

    try {

      mCom.left(speed);

    } catch (Exception e) {

      System.err.println("Could not turn left:" + e.getMessage());
      connect(current);

    }
  }  
  
  /**
   * Instructs the robot to turn right.
   *
   * @param current   Information about the current method invocation.
   */
  public void turnRight(Ice.Current current) {

    try {

      mCom.right();

    } catch (Exception e) {

      System.err.println("Could not turn right:" + e.getMessage());
      connect(current);

    }
  }
  
  /**
   * Instructs the robot to turn right at a certain speed.
   *
   * @param speed     The speed to turn at.
   * @param current   Information about the current method invocation.
   */
  public void turnRightSpeed(int speed, Ice.Current current) {

    try {

      mCom.right(speed);

    } catch (Exception e) {

      System.err.println("Could not turn right:" + e.getMessage());
      connect(current);

    }
  }

  /**
   * Instructs the robot to kick.
   *
   * @param current   Information about the current method invocation.
   */
  public void kick(Ice.Current current) {

    try {

      mCom.shoot();

    } catch (Exception e) {

      System.err.println("Could not kick:" + e.getMessage());
      connect(current);

    }
  }
  
}
