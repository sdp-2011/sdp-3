import ControlInterface
from Instructions import Convertor
from Logger import *

class Commander:
    """
    This class acts as an intermediate between the control interface and the AI.
    It stores a list of commands or instructions to be issued to the robot.
    It gets these from some strategy class, converts everything to commands, 
    and maps these to functions, either to change internal state or to send 
    something to the robot.
    """
    def __init__(self,controller):
        
        self.controller = controller
        self.convertor = Convertor()
        self.commands = []
        
        self.waiting = False
        self.waitFinish = False
        
        self.waitTimer = None
        self.timer = None
        
        self.rateTimer = 0.0
        self.commandRate = 0.1
        
        self.maxCommands = 10
        
        self.warningTimer = 0.0
        
        self.CommandFunctions = {
            "Blank"             :self.blank,
            "Forward"           :self.controller.driveForward,
            "Backward"          :self.controller.driveBackward,
            "Stop"              :self.controller.driveStop,
            "TurnLeft"          :self.controller.turnLeft,
            "TurnRight"         :self.controller.turnRight,
            "Kick"              :self.controller.kick,
            "SendInt"           :self.controller.sendInt,
            "Wait"              :self.wait,
            "WaitForFinish"     :self.waitForFinish,
            "ClearQueue"        :self.clearQueue,
            "LeftMotorSpeed"    :self.controller.setLeftMotorSpeed,
            "RightMotorSpeed"   :self.controller.setRightMotorSpeed,
        }
    
    def executeCommand(self,command):
        
        name = command.name
        args = command.args
        
        Log("Command",command)
        
        try:
            function = self.CommandFunctions[name]
            function(*args)
        except Exception as e:
            print ">> Unknown low level robot Command: "+name
        
    def iterate(self,new_instructions,world_state,frametime):
        """
        Called every frame. Does the following:
            - Converts any passed instructions into command lists.
            - Appends these to the internal command list.
            - Checks for a clear instruction in list.
            - If clear instruction exists loops over and clears everything 
              before it.
            - Loops over command list. If waiting, or waiting to finish, will
              skip commands. Otherwise executes.
        """
        if new_instructions is None:
            new_instructions = []

        command_lists = map( lambda x : self.convertor.convert(x,world_state,frametime) , new_instructions )

        for command_list in command_lists: self.commands += command_list
        
        self.warningTimer += frametime
        
        if len(self.commands) > self.maxCommands:
            if self.warningTimer > 2.0: 
                print ">> Recieving Commands too fast! Queue full - Commands discarded."
                self.warningTimer = 0.0
            for i in range(0,len(self.commands) - self.maxCommands) : self.commands.pop()        
        
        clear_found = False
        for command in self.commands:
            if command.name == "ClearQueue":
                clear_found = True
        
        if clear_found:
            cleared_list = []
            past_clear = False
            for command in self.commands:
                if past_clear:
                    cleared_list.append(command)
                if command.name == "ClearQueue":
                    cleared_list.append(command)
                    past_clear = True
            self.commands = cleared_list
        
        self.rateTimer += frametime
        num_commands = int(self.rateTimer // self.commandRate)
        self.rateTimer = self.rateTimer % self.commandRate
        
        num_commands = min(num_commands, len(self.commands))
        for i in range(0,num_commands ):
            if self.waiting:
                self.timer += frametime
                if self.timer > self.waitTime:
                    self.resume()
            elif self.waitFinish:
                self.waitFinish = self.controller.isMoving()
            else:
                command = self.commands.pop(0)
                self.executeCommand(command)
    
    def blank(self,*args):
        return

    def stop(self):
        self.controller.driveStop()
        
    def clearQueue(self,*args):
        self.commands = []
        
    def wait(self,*args):
        try:
            self.waitTime = args[0]
            self.waiting = True
            self.timer = 0.0
        except Exception as e:
            print ">> Wait command cannot be issued - passed without parameter."
    
    def resume(self):
        self.waiting = False
        self.timer = None
        self.waitTime = None
            
    def waitForFinish(self):
        self.waitFinish = True
        
