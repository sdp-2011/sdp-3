/*

This it the topic used by the controller and the AI to communicate.

Communication happens on port 10000 under the name ControlAdapter

This specification is planned to be fairly minimal, and match 
somewhat the commands we'd be directly sending to the bot, 
E.G "moveForward", "moveBackWard"

*/
module ControlTopic
{
    interface Control
	{
		void connect();
		void disconnect();

		void setLeftMotorSpeed(int speed);
		void setRightMotorSpeed(int speed);
		
		void driveForward();
		void driveForwardSpeed(int speed);
		void driveBackward();
		void driveBackwardSpeed(int speed);
		void driveStop();
		
		void turnLeft();
		void turnLeftSpeed(int speed);
		void turnRight();
		void turnRightSpeed(int speed);
		
		void kick();
		
		void sendInt(int i);
		
		void shutDownRobot();
		
		bool isMoving();
    };
};
