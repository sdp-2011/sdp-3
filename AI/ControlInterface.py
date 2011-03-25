import Communicator

class ControlInterface:
    """
    This is a friendly interface to the Communicator which uses Ice to 
    communicate to the controller component.
    
    As you can see this basically acts as a wrapper class. It simply 
    constructs a communicator and pulls the Ice interface from it.
    """
    def __init__(self):
        
        self.communicator = Communicator.Communicator("ControlTopic",
                "Control", "ControlPython", 10000)
        self.controller = None
        
    def isConnected(self):
        return self.communicator.isConnected
        
    def connect(self):
        """
        Connects to control interface topic, which then connects to the robot.
        """
        self.communicator.connect()
        self.controller = self.communicator.interface

        self.controller.connect()
        
    def disconnect(self):
        """
        Commands the java controller to disconnect the robot, then disconnects
        to the control interface topic itself.
        """
        
        self.controller.disconnect()
        self.communicator.disconnect()
   
    def setLeftMotorSpeed(self, speed = 700):
        self.controller.setLeftMotorSpeed(speed)

    def setRightMotorSpeed(self, speed = 700):
        self.controller.setRightMotorSpeed(speed)

    def driveForward(self, speed=None):
        if speed != None:
            self.controller.driveForwardSpeed(speed)
        else:
            self.controller.driveForward()

    def driveBackward(self, speed=None):
        if speed != None:
            self.controller.driveBackwardSpeed(speed)
        else:
            self.controller.driveBackward()
        
    def driveStop(self):
        self.controller.driveStop()
        
    def turnLeft(self, speed=None):
        if speed != None:
            self.controller.turnLeftSpeed(speed)
        else:
            self.controller.turnLeft()
        
    def turnRight(self, speed=None):
        if speed != None:
            self.controller.turnRightSpeed(speed)
        else:
            self.controller.turnRight()
        
    def kick(self):
        self.controller.kick()
        
    def sendInt(self,i):
        self.controller.sendInt(i)
    
    def shutDownRobot(self):
        self.controller.shutDownRobot()
        
    def isMoving(self):
        return self.controller.isMoving()
