import math

from Strategies import Strategy

from Logger import *
from Instructions import *
from AIMath import *

class Trigger:
    """
    Represents a trigger for a trigger strategy
    """
    def __init__(self,name,function,timer):
        
        self.name = name
        
        self.function = function
        self.timer = timer
        
        self.enabled = True
        self.once = False
        
        self.done = False
        
        self.clock = 0.0
        
        self.updateOnVision = False
        
class TriggerStrategy(Strategy):
    """
    This is an extension to the Strategy class which allows you to ignore the iterate function and program using triggers.
    Triggers are just a function which is passed the world state and called on a timer.
    There are also certain other things such as allowing a trigger to only be fired once.
    """
    def __init__(self):
        self.triggers = {}
        self.worldCounter = 0
        
    def addTrigger(self,function,timer):
        name = function.__name__
        self.triggers[name] = Trigger(name,function,timer)
    
    def setTriggerOnce(self,function):
        name = function.__name__
        self.triggers[name].once = True
    
    def setTriggerDelay(self,function,delay):
        name = function.__name__
        self.triggers[name].clock = -delay
    
    def setUpdateOnVision(self,function,updates):
        name = function.__name__
        self.triggers[name].updateOnVision = updates
    
    def removeTrigger(self,function):
        name = function.__name__
        del(self.triggers[name])
    
    def disableTrigger(self,function):
        name = function.__name__
        self.tiggers[name].enabled = False
    
    def enableTrigger(self,function):
        name = function.__name__
        self.tiggers[name].enabled = True
        
    def iterate(self,world_state,frametime):
        """
        If vision has updated then run through triggers that update on vision.
        Then run through triggers and
            - Updates clock with frametime
            - If clock is over time execute trigger and reset clock
            - If trigger is to fire once then set to done.
        """
        instructions = []
        if self.worldCounter < world_state:
            for t in self.triggers.values():
                if t.updateOnVision and t.enabled and (not t.done):
                    instructions += t.function(world_state)        
            self.worldCounter += 1
        
        for t in self.triggers.values():
            t.clock += frametime
            if t.clock > t.timer  and t.enabled and (not t.done) and (not t.updateOnVision):
                instructions += t.function(world_state)
                t.clock = 0.0
                if t.once:
                    t.done = True
                        
        return instructions
    
class ShuffleTriggers(TriggerStrategy):
    """
    Just a silly strategy to show how trigger strategies can be formed.
    Adds three triggers:
        - Logs the balls position every 4 seconds
        - Sends a backward command every 1 second
        - Sends a forward command every 1 second, with an initial delay of 0.5 so that they alternate
        - Prints "Hello!" after 3 seconds then never again.
    """
    def __init__(self):
    
        self.triggers = {}
    
        self.addTrigger(self.logBallPosition, 4.0)
        
        self.addTrigger(self.goBackward, 1.0)
        self.addTrigger(self.goForward, 1.0)
        self.setTriggerDelay(self.goForward,0.5)
        
        self.addTrigger(self.printHello,0.0)
        self.setTriggerOnce(self.printHello)
        self.setTriggerDelay(self.printHello,3.0)
    
        self.addTrigger(self.newVisionData,0.0)
        self.setUpdateOnVision(self.newVisionData,True)
    
    def logBallPosition(self, world_state):
        Log("Strategy","THE BALL IS HERE: "+str(world_state.ballPos))
        return []
        
    def goBackward(self, world_state):
        Log("Strategy","Now going backward!")
        return [Command("Backward")]
        
    def goForward(self, world_state):
        Log("Strategy","Now going forward!")
        return [Command("Forward")]
        
    def printHello(self,world_state):
        print "Hello!"
        return []
    
    def newVisionData(self,world_state):
        print Log("Debug","New Vision Data. Yays!")
        return []