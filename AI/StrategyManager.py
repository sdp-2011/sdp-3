"""
This class acts as an intermediate class between several of the main components to the system.
In some sense here is where all the main work is done - the strategy thread is spawed and managed here, user input is taken, and the interfaces are loaded.

The StrategyManager class takes commands from the UserInterface (which in turn takes commands from the user on the keyboard)
It uses these commands to manager the current strategy as well as connecting, disconnecting from the communication interfaces, robot etc.

The current strategy the system is using takes, at every iteration, data about the world state, and then returns back commands, which are then send to the control interface to be sent to the robot.
"""
import sys
import os
import copy
import time
import threading
import traceback

import ControlInterface
import VisionInterface

import WorldState
import Strategies
import Tactics
import Instructions

import Commander

from Logger import *
from AIMath import *

class StrategyManager:
    
    def __init__(self):
        
        OpenLogger()
        
        self.running = False
        self.reseting = False
        self.connected = False
        
        self.stepThrough = False
        self.step = False
        
        self.worldState = WorldState.WorldState()
        
        self.controlInterface = ControlInterface.ControlInterface()
        self.visionInterface = VisionInterface.VisionInterface()
        
        self.command_list = []
        self.commander = Commander.Commander(self.controlInterface)
        
        self.strategyClass = Strategies.MetaStrategy
        self.strategy = self.strategyClass()
        
        self.lastStrategyChange = os.stat("./Strategies.py").st_mtime    

        self.visionUpdateTimer = 0.0
        self.ballVelocities = []

        self.strategyThread = threading.Thread( name = "RunLoop", target = self.run )
        self.strategyThread.start()
        
        
    def sendCommand(self,command):
        self.command_list += command
        print self.command_list
    
    def exit(self):
        
        CloseLogger()
        
        self.reseting = True
        self.strategyThread.join()
        
        if self.connected:
            self.disconnect()
    
    def go(self):
    
        if not self.connected:
            self.connect()
        if not self.running:
            self.start()
    
    def start(self):
        """ Unpauses the AI """
        if self.running:
            print ">> AI already running"
        else:
            print ">> AI started"
            self.running = True
    
    def stop(self):
        """ Pauses the AI """
        if self.running:
            print ">> AI stopped"
            self.commander.clearQueue()
            self.commander.stop()
            self.running = False
        else:
            print ">> AI already stopped"
    
    def reset(self):
        """
        Set reset flag, wait for the thread to exit gracefully and join us.
        Then construct a new strategy and run thread.
        """
        
        print ">> Ending current routine"
        self.reseting = True
        self.strategyThread.join()
        self.reseting = False
        print ">> Done!"
        
        self.strategy = self.strategyClass()
        print ">> Building new Strategy of type "+self.strategy.__class__.__name__
        self.strategyThread = threading.Thread( name = "Strategy", target = self.run )
        self.strategyThread.start()
        print ">> Done!"
    
    def setStrategy(self,class_name):
        
        self.strategyClass = class_name
        self.reset()
    
    def connect(self):
        """ Connects to the interfaces at both sides """
        
        if self.connected == True:
            print ">> Interfaces already Connected"
            return
        
        try:
            print ">> Connecting to Vision Interface..."
            self.visionInterface.connect()
            
            print ">> Connecting to Controller Interface..."
            self.controlInterface.connect()
            
            self.connected = True
            
        except Exception as e:
            print ">> Error Connecting to Interfaces: "+str(e)
        
    def disconnect(self):
        """ Disconnects from both interfaces """
        
        if self.connected == False:
            print ">> Interfaces not connected"
            return
        
        try:
            if self.running:
                self.stop()
            
            self.connected = False
            
            print ">> Disconnecting from Control Interface"
            self.controlInterface.disconnect()     
            
            print ">> Disconnecting from Vision Interface"
            self.visionInterface.disconnect()
            
        except Exception as e:
            print ">> Error Disconnecting to Interfaces: "+str(e)
         
    def checkStrategyReload(self):
        
        Strategies.reloadTactics()
        
        stat = os.stat("./Strategies.py")
        mtime = stat.st_mtime
        if mtime != self.lastStrategyChange:
            self.lastStrategyChange = mtime
            print ">> Reloading Strategies"
            os.system("rm Strategies.pyc")
            reload(Strategies)
            strat_class_name = self.strategyClass.__name__
            del self.strategyClass
            del self.strategy
            self.strategyClass = Strategies.__dict__[strat_class_name]
            self.strategy = self.strategyClass()
            print ">> Building new Strategy of type "+self.strategy.__class__.__name__
            print ">> AI stopping"
            self.running = False
         
    def run(self):
        """
        This function is run in a separate thread.
        It represents the main "loop" of the AI.
            - Calculate Frame Time.
            - If connected, get new data about world state.
            - If running, get new high level instructions from strategy.
            - If connected, send instructions to the commander.
        """
        
        last_time = time.time()
        
        while (not self.reseting):
            
            if self.step or (self.stepThrough == False):
                new_instructions = []
                new_instructions += self.command_list
                self.command_list = []
            
                this_time = time.time()
                frame_time = this_time - last_time
                last_time = this_time
                
                if (self.connected):
                    self.updateWorldState(frame_time)
                
                self.checkStrategyReload()
                if (self.running):
                    try:
                        new_instructions += self.strategy.iterate(self.worldState,frame_time)
                    except Exception as e:
                        print ">> Error in Strategy "+self.strategyClass.__name__+": "+str(e)
                        print ">> "+str(traceback.print_exc(file=sys.stdout))
                        print ">> AI stopped"
                        self.running = False
                
                if (self.connected):
                    self.commander.iterate(new_instructions,self.worldState,frame_time)
                    
                self.step = False

        print "Finished strategyThread"
        
    def updateWorldState(self,frametime):
        """
        Pulls out the vision data from the vision interface.
        Updates the instance members.
        """
        
        self.visionUpdateTimer += frametime
        
        if self.worldState.counter < self.visionInterface.getCounter() and self.visionUpdateTimer != 0.0:
            
            self.worldState.counter = self.visionInterface.getCounter()
            
            self.worldState.shootingDirection = self.visionInterface.getShootingDirection()
            self.worldState.pitch = self.visionInterface.getPitch()
            self.worldState.color = self.visionInterface.getTeamColour()
            
            blue_robot = self.visionInterface.getBlueRobot()
            yellow_robot = self.visionInterface.getYellowRobot()
            
            # Update velocities before positions because it requires current position data.
            new_ball_vel = (V(self.visionInterface.getBallLocation()) - self.worldState.ballPos) / self.visionUpdateTimer

            self.ballVelocities.append(new_ball_vel)
            if len(self.ballVelocities) > 3 : self.ballVelocities.pop(0)
            
            vel_sum = V(0,0)
            for vec in self.ballVelocities : vel_sum += vec
            self.worldState.ballVel = vel_sum / len(self.ballVelocities)

            self.worldState.blueRobotVel = (V(blue_robot[0:2]) - self.worldState.blueRobotVel) / self.visionUpdateTimer
            self.worldState.yellowRobotVel = (V(yellow_robot[0:2]) - self.worldState.yellowRobotVel) / self.visionUpdateTimer
            
            self.worldState.ballPos = V(self.visionInterface.getBallLocation())
            
            self.worldState.yellowRobotPos = V(yellow_robot[0:2])
            self.worldState.yellowRobotRot = yellow_robot[2]
            
            self.worldState.blueRobotPos = V(blue_robot[0:2])
            self.worldState.blueRobotRot = blue_robot[2]
            
            self.visionUpdateTimer = 0.0
