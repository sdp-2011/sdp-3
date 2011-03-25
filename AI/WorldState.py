from AIMath import *

class WorldState:
    """
    Stores information about the current state of the pitch and how we
    should interact with it - our shooting direction, colour, etc.
    """
    
    def __init__(self):
        """
        Default world state data.
        """
        self.counter = 0
        
        # 0 indicates shooting 'right', 1 indicates shooting 'left'.
        self.shootingDirection = 0

        # 0 indicates the main pitch, 1 indicates the side room pitch.
        self.pitch = 0

        # 0 indicates that we are yellow, 1 indicates that we are blue.
        self.color = 0

        # The goal post locations on the pitch.
        self.goalpostLeftNorth = V(22, 172)
        self.goalpostLeftSouth = V(25, 330)
        self.goalpostRightNorth = V(620, 178)
        self.goalpostRightSouth = V(620, 332)
        
        # Ball position and velocity.
        self.ballPos = V(0,0)
        self.ballVel = V(0,0)
        
        # Blue robot position, orientation and velocity.
        self.blueRobotPos = V(0,0)
        self.blueRobotRot = 0.0
        self.blueRobotVel = V(0,0)
        
        # Yellow robot position, orientation and velocity.
        self.yellowRobotPos = V(0,0)
        self.yellowRobotRot = 0.0
        self.yellowRobotVel = V(0,0)

        # North = lowest Y value, South = max Y value,
        # Left = lowest X value, Right = max X value
        self.pitchNorth = 100.0
        self.pitchSouth = 400.0
        self.pitchLeft = 23.0
        self.pitchRight = 620.0
        
        self.meMoving = False

        # Control vars set by UI.
        self.obstacleAvoidanceDist = 125.0
        self.robotRadius = 40.0
        self.kickDistance = 80.0
    
    @property
    def oppGoalMidpoint(self):
        if self.shootingDirection == 0:
            return (self.goalpostRightNorth + self.goalpostRightSouth) / 2
        else:
            return (self.goalpostLeftNorth + self.goalpostLeftSouth) / 2
    
    @property
    def ourGoalMidpoint(self):
        if self.shootingDirection == 0:
            return (self.goalpostLeftNorth + self.goalpostLeftSouth) / 2
        else:
            return (self.goalpostRightNorth + self.goalpostRightSouth) / 2

    @property
    def goalpostAttackNorth(self):
        if self.shootingDirection == 0:
            return self.goalpostRightNorth
        else:
            return self.goalpostLeftNorth

    @property
    def goalpostAttackSouth(self):
        if self.shootingDirection == 0:
            return self.goalpostRightSouth
        else:
            return self.goalpostLeftSouth
    
    @property
    def goalpostDefendNorth(self):
        if self.shootingDirection == 0:
            return self.goalpostLeftNorth
        else:
            return self.goalpostRightNorth

    @property
    def goalpostDefendSouth(self):
        if self.shootingDirection == 0:
            return self.goalpostLeftSouth
        else:
            return self.goalpostRightSouth

    @property
    def myPos(self):
        if self.color == 0:
            return self.yellowRobotPos
        else:
            return self.blueRobotPos
        
    @property
    def oppPos(self):
        if self.color == 0:
            return self.blueRobotPos
        else:
            return self.yellowRobotPos
           
    @property
    def myRot(self):
        if self.color == 0:
            return self.yellowRobotRot
        else:
            return self.blueRobotRot
            
    @property
    def oppRot(self):
        if self.color == 0:
            return self.blueRobotRot
        else:
            return self.yellowRobotRot
    
    @property
    def myVel(self):
        if self.color == 0:
            return self.yellowRobotVel
        else:
            return self.blueRobotVel
    
    @property
    def oppVel(self):
        if self.color == 0:
            return self.blueRobotVel
        else:
            return self.yellowRobotVel
            
    @property
    def meMoving(self):
        if size(self.myVel) > 0.1:
            return True
        else:
            return False
    
    @property
    def oppMoving(self):
        if size(self.oppVel) > 0.1:
            return True
        else:
            return False
