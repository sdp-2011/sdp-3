import Communicator

class VisionInterface:
    """
    This is the interface which connects to the world state topic and reads off
    information from the vision system.
    """

    def __init__(self):
        self.communicator = Communicator.Communicator("WorldStateTopic","WorldState","WorldState",10012)
        self.controller = None
    
    def connect(self):
        self.communicator.connect()
        self.controller = self.communicator.interface
    
    def disconnect(self):
        self.communicator.disconnect()
    
    def getBallLocation(self):
        ball = self.controller.getBallPosition()
        position = ball.pos
        return (position.x,position.y)    
    
    def getYellowRobot(self):
        robot = self.controller.getYellowRobot()
        position = robot.pos
        rotation = robot.rot
        return (position.x,position.y, rotation)

    def getBlueRobot(self):
        robot = self.controller.getBlueRobot()
        position = robot.pos
        rotation = robot.rot
        return (position.x,position.y,rotation)

    def getPitch(self):
        return self.controller.getPitch()
        
    def getShootingDirection(self):
        return self.controller.getShootingDirection()
        
    def getTeamColour(self):
        return self.controller.getTeamColour()
        
    def getCounter(self):
        return self.controller.getUpdateID()
