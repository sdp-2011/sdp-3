import sys

import StrategyManager
import Strategies
from Instructions import *

class UserInterface:
    """
    Interface for controlling the robot via user commands.
    """

    def __init__(self):
        
        self.strategyManager = StrategyManager.StrategyManager()

        # The "default" strategies that can be accessed through
        # the strategyID() command.
        self.strategies = [
            Strategies.Blank,
            Strategies.Penalty,
            Strategies.DefendPenalty,
            Strategies.MetaStrategy,
            Strategies.ChaseBall,
            Strategies.OneShotIntercept
        ]
        
    def stepThrough(self):
        self.strategyManager.stepThrough = True;
        
    def step(self):
        self.strategyManager.step = True
        
    def connect(self):
        self.strategyManager.connect()
        
    def disconnect(self):
        self.strategyManager.disconnect()
        
    def reconnect(self):
        self.disconnect()
        self.connect()

    def isConnected(self):
        print ">> "+str(self.strategyManager.connected)
    
    def isRunning(self):
        print ">> "+str(self.strategyManager.running)
    
    def start(self):
        self.strategyManager.start()
        
    def stop(self):
        self.strategyManager.stop()
    
    def reset(self):
        self.strategyManager.reset()
    
    def go(self):
        self.strategyManager.go()
    
    def strategyClass(self, strategy_type):
        self.strategyManager.setStrategy(strategy_type)

    def strategyIDs(self):
        print ">> Strategy IDs:"
        for i in range(0,len(self.strategies)):
            print ">>    "+str(i)+" - "+self.strategies[i].__name__
        
    def strategyID(self,id):
        self.strategyClass(self.strategies[id])

    def currentStrategy(self):
        print ">> The current strategy is "+self.strategyManager.strategyClass.__name__
        
    def sendCommand(self,command):
        self.strategyManager.sendCommand(command)
    
    def disableCharge(self):
        self.strategyManager.strategy.charge_state = "DONE"
    
    def enableCharge(self):
        self.strategyManager.strategy.charge_state = "ACTIVATE"
    
    def peek(self,message):
        print eval(message)
        
    def quit(self):
        self.exit()
        
    def exit(self):
        self.strategyManager.exit()
        sys.exit()
        
    def help(self):
        print ">> Commands:"
        print ""
        print "   connect()"
        print "   disconnect()"
        print "   reconnect()"
        print "   isConnected()"
        print ""
        print "   start()"
        print "   stop()"
        print "   go()"
        print "   isRunning()"
        print ""
        print "   stepThrough()"
        print "   step()"
        print ""
        print "   sendCommand(command/instruction)"
        print "   strategyIDs()"
        print "   strategyID(id)"
        print "   strategyClass(Strategies.StrategyClass)"
        print "   currentStrategy()"
        print "   reset()"
        print ""
        print "   peek(\"variable\")"
        print "   help()"
        print "   quit()"
        print "   exit()"
