import lejos.nxt.*;

public class QuickTest {

  public static void main(String[] args) {

    SDPPilot pilot = new SDPPilot(0.0f,0.0f,Motor.B, Motor.A, Motor.C, true);
    TouchSensor frontLeftSensor = new TouchSensor(SensorPort.S1);
    TouchSensor frontRightSensor = new TouchSensor(SensorPort.S2);

    pilot.setKickerSpeed(600);

    pilot.shoot();

    pilot.stop();

  }

}
