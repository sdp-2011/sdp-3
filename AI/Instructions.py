from AIMath import *
import math

class Instruction:
    """
    Represents a high level instruction in the system.
    """
    def __init__(self,name,*args):
        self.name = name
        self.args = args
    def __str__(self):
        if len(self.args) > 0:
            return "Instruction(\""+self.name+"\", "+str(self.args)+")"
        else:
            return "Instruction(\""+self.name+"\")"
        
    def __repr__(self):
        return str(self)
        
    def __eq__(self,other):
        return (self.name == other.name and self.args == other.args)
        
    def __ne__(self,other):
        return not (self == other)

class Command:
    """
    Represents a low level instruction in the system.
    """
    def __init__(self,name,*args):
        self.name = name
        self.args = args
    def __str__(self):
        if len(self.args) > 0:
            return "Command(\""+self.name+"\", "+str(self.args)+")"
        else:
            return "Command(\""+self.name+"\")"
        
    def __repr__(self):
        return str(self)
        
    def __eq__(self,other):
        return (self.name == other.name and self.args == other.args)
        
    def __ne__(self,other):
        return not (self == other)
     
class Convertor:
    """
    This does the conversions between high level and low level instructions.
    """
    
    def __init__(self):
        
        # This should be in vision, not in AI.
        # Each cm is 2.54 pixels
        self.CAMERA_PIXEL_RATIO = 2.54
        
        self.convertFunction = {
            "MoveToPoint"       :self.moveToPoint,
            "MoveShortOfPoint"  :self.moveShortOfPoint,
            "BearRight"         :self.bearRight,
            "BearLeft"          :self.bearLeft,
            "ForwardSpeed"      :self.forwardSpeed,
            "Turn"              :self.robotTurntoAngle,
        }
    
    def convert(self,instruction,world_state,frametime):
        """
        Converts an Instruction object into a list of Command objects. 
        """
        #print instruction
        
        if instruction.__class__ is Command:
            return [instruction]
        else:
            try:
                function = self.convertFunction[instruction.name]
            except Exception as e:
                print ">> Unknown high level robot Instruction: "+instruction.name
                return []
            instructions = function(world_state,frametime, instruction.args)
            return instructions
           
            
    def moveShortOfPoint(self,world_state,frametime,args):
        """
        Sends a series of commands to move the robot to a position just short of a point.
        """
        
        point = args[0]
        dist_short = args[1]
        
        dist = distance(point, world_state.myPos) - dist_short
        turn = self.robotAngleToPoint(world_state,point)
        turn = math.degrees(turn)
        
        if turn < 0:
            instructions = [Command("Stop"),Command("TurnLeft",-turn),Command("Forward",dist/self.CAMERA_PIXEL_RATIO)]
        else:
            instructions = [Command("Stop"),Command("TurnRight",turn),Command("Forward",dist/self.CAMERA_PIXEL_RATIO)]
     
        return instructions
        
    def moveToPoint(self,world_state,frametime,args):
        """
        First calculates the angle between a point and the x axis using atan2.
        Takes the robot rotation away from this and maps between -pi and pi.
        Finds the distance, and sends these as a series of commands to the robot.
        """
        
        point = args[0]
        
        turn = self.robotAngleToPoint(world_state,point)
        turn = math.degrees(turn)
        dist = distance(point, world_state.myPos)
        
        if turn < 0:
            instructions = [Command("Stop"),Command("TurnLeft",-turn),Command("Forward",dist/self.CAMERA_PIXEL_RATIO)]
        else:
            instructions = [Command("Stop"),Command("TurnRight",turn),Command("Forward",dist/self.CAMERA_PIXEL_RATIO)]
     
        return instructions
    
    def bearRight(self,world_state,frametime,args):
        if args[0] is None:
            amount = 700
        else:
            amount = args[0]
        
        if amount > 700 or amount < 0:
            print ">> Cannot Bear Right with amount: "+str(amount)+" Amount must be between 0 and 700"
            return []
        
        right_speed = 700-amount
        left_speed = 700
        
        return [Command("LeftMotorSpeed",left_speed),Command("RightMotorSpeed",right_speed)]
                
        
    def bearLeft(self,world_state,frametime,args):
        if args[0] is None:
            amount = 700
        else:
            amount = args[0]
        
        if amount > 700 or amount < 0:
            print ">> Cannot Bear Left with amount: "+str(amount)+" Amount must be between 0 and 700"
            return []
        
        right_speed = 700
        left_speed = 700-amount
        
        return [Command("LeftMotorSpeed",left_speed),Command("RightMotorSpeed",right_speed)]
                
    
    def forwardSpeed(self,world_state,frametime,args):
        if args[0] is None:
            speed = 10
        else:
            speed = args[0]
        return [Command("LeftMotorSpeed",speed),Command("RightMotorSpeed",speed)]
    
    def robotAngleToPoint(self,world_state,point):
        
        vector = point - world_state.myPos
        angle = math.atan2(vector[1], vector[0])
        turn = angle - world_state.myRot

        while ( turn < -math.pi ):
            turn += math.pi
        while ( turn > math.pi ):
            turn -= math.pi
        
        return turn
        
        
    def robotTurntoAngle(self,world_state,angle):
        """
        Turns robot onto angle once it has stopped the robot.
        """
    
        turn = angleBetweenAngle(world_state.myRot, angle) # anti clockwise

        if turn > 0:
            instructions = [Command("Stop"),Command("TurnLeft",-turn)]
        else:
            instructions = [Command("Stop"),Command("TurnRight",turn)]
     
        return instructions
        
