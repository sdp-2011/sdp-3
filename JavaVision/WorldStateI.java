import Ice.Current;

/**
 * The WorldStateI class represents the topic interface.
 * It must implement all the functions listed in WorldState.ice.
 *
 * It reads from the vision class and blah etc.
 *
 * @author Stephen McGruer
 */
@SuppressWarnings("serial")
public class WorldStateI extends WorldStateTopic._WorldStateDisp {

  WorldState ws;
  
  public WorldStateI() {
    ws = new WorldState();
  }

  public WorldStateI(WorldState ws) {
    this.ws = ws;
  }

  public WorldStateTopic.Ball getBallPosition(Ice.Current current) {
    float x = ws.getBallX();
    float y = ws.getBallY();
    return new WorldStateTopic.Ball(new WorldStateTopic.Position(x,y));
  }

  public WorldStateTopic.Robot getBlueRobot(Ice.Current current) {
    float x = ws.getBlueX();
    float y = ws.getBlueY();
    float orientation = ws.getBlueOrientation();
    return new WorldStateTopic.Robot(new WorldStateTopic.Position(x,y), orientation);
  }

  public WorldStateTopic.Robot getYellowRobot(Ice.Current current) {
    float x = ws.getYellowX();
    float y = ws.getYellowY();
    float orientation = ws.getYellowOrientation();
    return new WorldStateTopic.Robot(new WorldStateTopic.Position(x,y), orientation);
  }

  public int getPitch(Current current) {
	  return ws.getPitch();
  }

  public int getShootingDirection(Current current) {
	  return ws.getDirection();
  }

  public int getTeamColour(Current current) {
	  return ws.getColour();
  }
  
  public long getUpdateID(Current current) {
    return ws.getCounter();
  }

}

