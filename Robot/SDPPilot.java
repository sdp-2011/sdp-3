import lejos.robotics.navigation.TachoPilot;
import lejos.robotics.TachoMotor;

public class SDPPilot { 

  private TachoMotor leftMotor;
  private TachoMotor rightMotor;
  private TachoMotor kicker;
  private boolean reverse;

  public SDPPilot(float wheelDiameter, float trackWidth,
                  TachoMotor leftMotor, TachoMotor rightMotor,
                  TachoMotor kicker, boolean reverse) {

    this.leftMotor = leftMotor;
    this.rightMotor = rightMotor;

    this.leftMotor.regulateSpeed(true);
    this.rightMotor.regulateSpeed(true);
    this.leftMotor.smoothAcceleration(true);
    this.rightMotor.smoothAcceleration(true);

    this.kicker = kicker;

    this.reverse = reverse;

  }

  // Returns false if unable to set the speed.
  public boolean setKickerSpeed(int speed) {

    if (speed < 0 || speed > 1000) return false;

    kicker.setSpeed(speed);
    return true;

  }

  public void setSpeed(int speed) {
    setLeftMotorSpeed(speed);
    setRightMotorSpeed(speed);
  }

  public void forward() {
    if (reverse) {
      this.leftMotor.backward();
      this.rightMotor.backward();
    } else {
      this.leftMotor.forward();
      this.rightMotor.forward();
    }
       
  }

  public void forward(float distance) {
    this.forward();
  } 

  public void backward() {
    if (reverse) {
      this.leftMotor.forward();
      this.rightMotor.forward();
    } else {
      this.leftMotor.backward();
      this.rightMotor.backward();
    }
  }

  public void backward(float distance) {
    this.backward();
  }
  

  public void stop() {
    this.leftMotor.stop();
    this.rightMotor.stop();
  }

  public void left() {
    this.left(75);
  }

  public void left(int speed) {
    setLeftMotorSpeed(speed);
    setRightMotorSpeed(speed);
    if (reverse) {
      this.rightMotor.backward();
      this.leftMotor.forward();
    } else {
      this.rightMotor.forward();
      this.leftMotor.backward();
    }
  }

  public void right() {
    this.right(75);
  }

  public void right(int speed) {
    setLeftMotorSpeed(speed);
    setRightMotorSpeed(speed);
    if (reverse) {
      this.leftMotor.backward();
      this.rightMotor.forward();
    } else {
      this.leftMotor.forward();
      this.rightMotor.backward();
    }
  }

  public void shoot() {
    this.kicker.rotate(-144, true);
  }

  public void setLeftMotorSpeed(int speed) {
    if (!(speed < 0 || speed > 900)) {
      this.leftMotor.setSpeed(speed);
    }
  }

  public void setRightMotorSpeed(int speed) {
    if (!(speed < 0 || speed > 900)) {
      this.rightMotor.setSpeed(speed);
    }
  }

}
