/*

This topic is published to by the Vision component and represents the world state.

Some notes on what the types of the variables mean.

Axis are measured from the top left, with positive going down and to the right.

 0 1 2 3 4 5 6 7 8 9
 1 +---------------+
 2 |           o   |
 3 | #           # |
 4 |               |
 5 +---------------+ 

So the ball in this example has the coordinates (7,2)

Rotations are measured in RADIANS from the X AXIS, CLOCKWISE.

*/
module WorldStateTopic
{
	/* Represents a position in the world */
    struct Position
    {
        float x;
        float y;
    };
	
	/* Represents the ball in the world */
	struct Ball
	{
		Position pos;
	};
	
	struct Robot
	{
		Position pos;
		float rot;
	};
	
	/*
	This is the interface, you define in here functions you would like, with their return type.
	I.E server fuctions you want someone to code, and the object you want them to return.
	*/
    interface WorldState
    {
		long getUpdateID();
	
		Ball getBallPosition();
		Robot getYellowRobot();
		Robot getBlueRobot();
		int getPitch();
		int getShootingDirection();
		int getTeamColour();
    };
};
