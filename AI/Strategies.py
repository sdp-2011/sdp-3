import math
import os
import random

import Tactics
import Predictions

from Instructions import *
from AIMath import *
from Logger import *

lastTacticsChange = os.stat("./Tactics.py").st_mtime

def reloadTactics():
    global lastTacticsChange
    
    stat = os.stat("./Tactics.py")
    mtime = stat.st_mtime
    if mtime != lastTacticsChange:
        lastTacticsChange = mtime
        print ">> Reloading Tactics"
        os.system("rm Tactics.pyc")
        reload(Tactics)


class Strategy(object):
    """
    An abstract class representing an AI strategy. All strategies should 
    subclass this class.

    A strategy is fairly simple:
        At each frame the 'iterate' method is called:
            * It is sent data about the world state and the time since the
              last frame.
            * It then returns a list of instructions or commands to be sent
              to the robot. This can be empty.
        
    This is all for now. In future there might also be support for adding 
    an event handler for events on the robot.
    """
    
    def iterate(self, world_state, frametime):
        """
        Given a current world state and the time since the last frame,
        returns a list of instructions for the robot.

        Sub-classes should override this abstract method.
        """
        pass


        
class MetaStrategy(Strategy):
    """ 
    Main strategy, decides on what actions to take.
    """
    
    def __init__(self):
        """
        Initialise the MetaStrategy.
        Creates a driver to use and some of the hardcoded charge instructions.
        """
        
        self.driver = Driver()
        #self.driver.arc = True
        
        self.charge_state = "TURNING"
        #self.charge_state = "DONE"
        self.charge_timer = 0.0
        
        self.vision_update_timer = 0.0
        self.vision_counter = 0

        self.kick_timer = 0.0

    def iterate(self,world_state,frametime):
        """
        Strategy: Get to the ball then get into a shooting situation.
        
        This method controls the in game strategy by assesing the situation and
        following our game plan:

        """
        
        # I've Pulled all the charge stuff outside of the vision stuff for accuracy on timings.

        self.charge_timer += frametime
        self.vision_update_timer += frametime
        self.kick_timer += frametime
        
        charge_time = 2.75
        turn_time = 0.3
        end_of_charge = self.charge_timer > charge_time
        begin_charge = self.charge_timer > turn_time 

        if self.charge_state == "TURNING":
            print "Turning..."
            self.charge_state = "ACTIVATE"
            return [Command("TurnRight")]

        # Check for if we must return charge based instructions.
        if self.charge_state == "ACTIVATE" and begin_charge:
            print "Charging!"
            self.charge_state = "DRIVING"
            return [Command("Stop"),Command("LeftMotorSpeed",900),Command("RightMotorSpeed",800),Command("Forward")]


        if self.charge_state == "DRIVING" and not end_of_charge:
            return []
            
        if self.charge_state == "DRIVING" and end_of_charge:
            self.charge_state = "DONE"
            return [Command("Stop"),Command("Kick")]



        
        # Wait for vision Update
        if world_state.counter == self.vision_counter:
            return []
        else:
            self.vision_counter = world_state.counter
            self.vision_update_timer = 0.0
        
        # ------------------------- #
        #       Begin Tactics       #
        # ------------------------- #
        
       
        # Check if it is possible for us to shoot at the goal.
        shot_angle_possible = Tactics.CheckKick(world_state)
        shot_distance_possible = distance(world_state.myPos, world_state.ballPos) < (world_state.robotRadius + 10)
        
        if shot_angle_possible and shot_distance_possible:
            print "Kick!!"
            if self.kick_timer > 1.0:
                self.kick_timer = 0.0        
                return [Command("Kick")]
            else:
                return []
        
        if shot_angle_possible and not shot_distance_possible:
            print "Driving To Kick"
            self.driver.target = world_state.ballPos
            self.driver.state = "STOPPED"
            return self.driver.iterate(world_state, self.vision_update_timer)
        
        # Check if we need to defend.
        opponent_has_ball = distance(world_state.oppPos, world_state.ballPos) < world_state.kickDistance
        opponent_nearer_ball = distance( world_state.myPos, world_state.ballPos ) > distance(world_state.oppPos, world_state.ballPos)
        defend_position = Tactics.FindDefencePosition(world_state)
        
        if opponent_has_ball and opponent_nearer_ball and defend_position:
            print "Defending"
            self.driver.target = defend_position
            return self.driver.iterate(world_state, self.vision_update_timer)        

        # Otherwise find a good shooting position
        setup_position = Tactics.FindShootingPosition(world_state)

        if setup_position is None:
            defend_goal_point = Tactics.FindGoalDefencePoint(world_state)
            print "Invalid Setup point " + str(defend_goal_point)
            self.driver.target = world_state.ballPos # defend_goal_point
            return self.driver.iterate(world_state, self.vision_update_timer)
        
        at_setup = distance( setup_position, world_state.myPos ) < self.driver.min_distance + 15
        
        if at_setup:
            print "At Setup"
            self.driver.target = world_state.ballPos
            return self.driver.iterate(world_state, self.vision_update_timer)
       
        print "Setting Up Shot " + str(setup_position)
        self.driver.target = setup_position
        return self.driver.iterate(world_state, self.vision_update_timer)
        
        # ------------------------- #
        #        End Tactics        #
        # ------------------------- #
        

class Penalty(Strategy):
   
    def __init__(self):
        self.state = "SETUP"

        self.timer = 0.0

        self.meta = MetaStrategy()
        
    def iterate(self,world_state,frametime):

        self.timer += frametime

        if self.state == "META":
            return self.meta.iterate(world_state, frametime)

        if self.timer > 0.05:
            self.state = "META"
            return [Command("Kick")]

        if self.state != "TURN":

            self.state = "TURN"

            opponent_y = world_state.oppPos.y
            goal_midpoint_y = world_state.oppGoalMidpoint.y

            if world_state.shootingDirection == 0:

                if opponent_y > goal_midpoint_y:
                    return [Command("TurnLeft", 125)]
                else:
                    return [Command("TurnRight", 125)]
                
            else:

                if opponent_y > goal_midpoint_y:
                    return [Command("TurnRight", 125)]
                else:
                    return [Command("TurnLeft", 125)]

        return []

       

class DefendPenalty(Strategy):
    """
    Defends a Penalty kick.
    Calculates optimal defend position and moves the robot
    """
    def __init__(self):
        self.timer = 0.0
        self.state = "INIT"

        # Hack!
        self.meta = MetaStrategy()

    def iterate(self,world_state,frametime):
        """
        What it does:
            - checks where the opponent is in relation to ballPos
            - calculates opponent's shooting angle
            - calculates where we need to move to block the shot and goes there
        """

        self.timer += frametime

        if distance(world_state.ballPos, world_state.oppPos) > world_state.robotRadius + 50:
            self.state = "META"      
        
        if self.state == "META":
            return self.meta.iterate(world_state, frametime)
        
        time = 1.0

        if self.state == "INIT" and self.timer > (time/2):
            self.state = "BACKWARD"
            return [Command("Stop"),Instruction("ForwardSpeed", 700),Command("Backward")]

        if self.timer > time:
            
            if self.state == "FORWARD":
                self.state = "BACKWARD"
                self.timer = 0.0
                return [Command("Stop"),Command("Backward")]
            
            elif self.state == "BACKWARD":
                self.state = "FORWARD"
                self.timer = 0.0
                return [Command("Stop"),Command("Forward")]
        
        return []

        

             
class Blank(Strategy):
    """
    Does nothing. Just returns the empty list of instructions/commands.
    """
    def __init__(self):
        return
        
    def iterate(self,world_state,frametime):
        return []
     
       
class Driver(Strategy):
    """
    This is a stategy class meant to be used as a sub-stategy for more 
    complicated strategies.
    What it will do is move the robot toward whatever you pass into the 
    "target" member. This must be a point vector!
    
    To use this you must instantiate it as a sub-stategy and then update the 
    'target' member when you want it to drive somewhere.
    See the ChaseBall Stategy for an example of it's use.
    
    """
    
    def __init__(self):

        # Don't change
        self.state = "STOPPED"
        
        # Change these to control how the strategy works.
        self.arc = False
        
        self.target = None
        self.enabled = True
        
        self.kick_target = False
        
        self.arc_boost = 0.25 

        self.current_speed = self.max_speed
        
    def getarc(self):
        """
        Returns whether or not arcing is enabled. If enabled the robot
        will attempt to move and turn by setting wheel speeds instead
        of the traditional stop-and-turn movement.
        """
        return self._arc

    def setarc(self, value):
        """
        Sets whether or not arcing is enabled. If enabled the robot
        will attempt to move and turn by setting wheel speeds instead
        of the traditional stop-and-turn movement.
        """

        if value is True:
            
            print "Arcing enabled"
            self._arc = True
            self.min_angle = 0.0
            self.turn_on_spot = math.pi
            self.max_speed = 400
            self.min_distance = 35
        
        elif value is False:
    
            print "Arcing disabled"
            self._arc = False
            self.min_angle = 0.30
            self.turn_on_spot = math.pi/2
            self.max_speed = 500
            self.min_distance = 40
        
    # Arcing can be treated as a variable so the user can just
    # do Driver.arc = True/False etc.
    arc = property(getarc,setarc)

    def iterate(self, world_state, frametime):
        """
        What this strategy does each time you call it.
            - Check how close the robot it is to the target, if close enough stop
            - Check angle between target and self.
                - If angle is small enough, continue forward
                - Otherwise bear toward it.
        """
        
        if self.target != None and self.enabled:
            
            self.target = Tactics.AvoidBall(world_state, self.target)
            self.target = Tactics.ClampPositionY(world_state, self.target)
            
            if distance(self.target, world_state.myPos) < world_state.robotRadius + 50:
                self.current_speed = self.max_speed / 2
            else:
                self.current_speed = self.max_speed

            vector = self.target - world_state.myPos
            angle = math.atan2(vector[1], vector[0])
            turn_angle = angle - world_state.myRot

            while ( turn_angle < -math.pi ):
                turn_angle += 2 * math.pi
            while ( turn_angle > math.pi ):
                turn_angle -= 2 * math.pi

            # Constrain the turn angle to attempt to compensate for camera lag.
            turn_angle *= 0.75
            
            # turn_angle = (math.pi/2), ratio should be 0
            # turn_angle = 0, ratio should be 1
            if self._arc:
                #self.ratio = (math.pi/2 - abs(turn_angle)) / (math.pi/2) - self.arc_boost
                #self.ratio = max(self.ratio , 0.0)
                if turn_angle < math.pi/3:
                    self.ratio = 0.5
                else:
                    self.ratio = 0.3


            buffer_distance = self.min_distance
            if self.kick_target : buffer_distance += 25

            if distance(world_state.myPos,self.target) < buffer_distance:
                if self.state != "AT_TARGET":
                    print ">> At target. " + str(self.target) + " | " + str(world_state.myPos) + " Stopping"
                    self.state = "AT_TARGET"
                    if self.kick_target:
                        print "kick stop"
                        return [Command("Kick"),Command("Stop")]
                    else:
                        return [Command("Stop")]
                return []
                    
            if abs(turn_angle) < self.min_angle:            
                if self.state != "FORWARD":

                    print ">> Target is in front (" + str(math.degrees(turn_angle)) + " degrees), moving forward"
                    self.state = "FORWARD"
                    if self._arc:
                        return [Command("Stop"), Instruction("ForwardSpeed", self.current_speed), Command("Forward")]
                    else:
                        return [Command("Stop"), Instruction("ForwardSpeed", self.current_speed), Command("Forward")]
                return []
                    
            if turn_angle < 0.0:
                if abs(turn_angle) < self.turn_on_spot and self.state != "BEAR_LEFT":

                    print ">> Target is slow left (" + str(math.degrees(turn_angle)) + " degrees, " + str(distance(world_state.myPos, self.target)) + ")"
                    self.state = "BEAR_LEFT"
                    if self._arc:
                        return [Command("Forward"), Command("LeftMotorSpeed",self.max_speed * self.ratio),Command("RightMotorSpeed",self.max_speed)]
                    else:
                        return [Command("Stop"), Command("TurnLeft", 100)]
                    
                if abs(turn_angle) > self.turn_on_spot and self.state != "LEFT":
                
                    print ">> Target is sharp left (" + str(math.degrees(turn_angle)) + " degrees)"
                    self.state = "LEFT"
                    return [Command("Stop"), Command("TurnLeft", 150)]
                return []
                    
            if turn_angle > 0.0:

                if abs(turn_angle) < self.turn_on_spot and self.state != "BEAR_RIGHT":

                    print ">> Target is slow right (" + str(math.degrees(turn_angle)) + " degrees, " + str(distance(world_state.myPos, self.target)) + ")"
                    self.state = "BEAR_RIGHT"
                    if self._arc:
                        return [Command("Forward"), Command("LeftMotorSpeed",self.max_speed),Command("RightMotorSpeed",self.max_speed * self.ratio)]
                    else:
                        return [Command("Stop"), Command("TurnRight", 100)]
                    
                if abs(turn_angle) > self.turn_on_spot and self.state != "RIGHT":
      
                    print ">> Target is sharp right (" + str(math.degrees(turn_angle)) + " degrees)"
                    self.state = "RIGHT"
                    return [Command("Stop"), Command("TurnRight", 150)]
                return []
                
        print "DRIVER: Fell through!"
        return []


class ChaseBall(Strategy):
    """
    Uses the driver class to simply chase the ball.
    Will kick ball once it gets to it.
    """
    def __init__(self):
        self.driver = Driver()
        self.driver.enabled = True
        
        #self.driver.kick_target = True
        #self.driver.arc = True
        
    def iterate(self,world_state, frametime):
        self.driver.target = world_state.ballPos
        instructions = self.driver.iterate(world_state,frametime)
            
        return instructions


class OneShotIntercept(Strategy):

    def __init__(self):
        self.driver = Driver()
        self.driver.arc = True
        self.driver.min_distance = 25
        self.timer = 0.0
        self.timer2 = 0.0
        self.timer3 = 0.0
        self.go = 0

    def iterate(self, world_state, frametime):
        """
        Finds a predicted point of the ball in the future to drive to based upon distance from robot to ball.
        """
        
        self.timer += frametime
        self.timer2 += frametime

        instructions = self.driver.iterate(world_state, frametime)

        if self.timer2 > 0.1:
            self.timer2 = 0.0

            # Get distance between ball and robot. Predict some time in future based on this
            # For a full span of the pitch (640 pixels) predict 3 seconds in the future.
            # Shrink this based on distance to the ball
            dist = distance(world_state.ballPos, world_state.myPos)# + 30
            time = (3/640.0) * dist
            print "Current ball position is: " + str(world_state.ballPos)
            predicted_ball_pos = Predictions.predictBallPos(world_state, time)
            print "Target position is: " + str(predicted_ball_pos)
            if length(world_state.ballVel) > 20:
                self.go += 1
                if self.go >= 3:
                    self.driver.target = predicted_ball_pos
                else:
                    self.driver.target = world_state.myPos
            else:
                self.driver.target = world_state.myPos

        return instructions

class CheapIntercept(Strategy):
    
    def __init__(self):
        self.driver = Driver()
        self.driver.arc = True
        self.timer = 0.0    

    def iterate(self, world_state, frametime):
        
        if self.timer > 0.2:
            self.timer = 0.0
        else:
            self.timer += frametime
            return []

        if length(world_state.ballPos) > 20:
            self.driver.target = V(world_state.myPos.x, world_state.ballPos.y)
        #else:
        #    self.driver.target = world_state.myPos
        
        return self.driver.iterate(world_state, frametime)

class Intercept(Strategy):
    """
    Uses times & positions returned from functions defined in Predictions to calculate and drive to where the ball will be.
    """
    
    def __init__(self):
        self.driver = Driver()
        self.driver.arc = False
        
        self.timer = 0.0
        self.point_timer = 0.0
        self.interception = False        

    def iterate(self, world_state, frametime):
        """
        Every 3 seconds revaluates and gets a new point to intercept
        This only happens if the ball is also going fast enough.
        """
        
        self.point_timer += frametime

        if self.timer > 0.2:
            self.timer = 0.0
        else:
            self.timer += frametime
            return []
        
        if self.point_timer > 2 or not self.interception:

            self.point_timer = 0.0
      
            #print "Ball velocity: " + str(world_state.ballVel)
            if length(world_state.ballVel) > 30:
                self.newInterceptionPoint(world_state)
            else:
                self.interception = False
                self.driver.target = world_state.myPos

        # Use the driver class to navigate to the interception point.
        return self.driver.iterate(world_state, frametime)

    def newInterceptionPoint(self,world_state):
        """
        For times 1 to 20 (in seconds)
            - finds the ball's position at this time
            - finds the robot travel time to this point
            - if the travel time plus some buffer is less than the ball time
                - Then new interception at this point. Sets driver target.
        """
        
        # How many seconds ahead of the ball the robot has to arrive at
        # a point for it to be an 'intercept' point.
        travel_buffer = 1.0
        
        found = False
        
        print "Finding new Interception"
        for ball_time in [x * 0.1 for x in range(1,50)]:
            
            if not found:
                ball_pos = Predictions.predictBallPos(world_state, ball_time)
                travel_time = predictRobotMovementTime(world_state, ball_pos)
                if (travel_time + travel_buffer < ball_time):
                    interceptstring = "Interception at " + str(ball_pos) + " from " + str(world_state.myPos)
                    timestring = "Robot time: " + str(travel_time) + " Ball Time " + str(ball_time)
                    print interceptstring
                    print timestring
                    Log("Intercept",interceptstring)

                    Log("Intercept",timestring)
                    self.driver.target = ball_pos
                    self.interception = True
                    found = True

        if not found:
            print "Could not find interception"


class MoveToPoint(Strategy):
    
    def __init__(self):
        self.target = V(300,200)
        self.driver = Driver()
        self.driver.arc = True

    def iterate(self, world_state, frametime):
        self.driver.target = self.target
        return self.driver.iterate(world_state, frametime)

