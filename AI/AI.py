"""
This is the main running class.
It creates a UserInterface then waits for user commands via keyboard.

I've been mega lazy and I've got it set up so it just uses the "exec" function
on the UserInterface class. This means it just executes what you type as a 
function defined in UserInterface.
"""

import signal
import os, sys

if sys.platform != 'win32':
    import readline
else:
    sys.path.append("../Library/IcePython")
    
import UserInterface
import Strategies
from Instructions import *

# The UserInterface class handles most of the interaction with the 
# user - we merely pass their input to it.
userInterface = UserInterface.UserInterface()

print ">> WELCOME TO THE SUPER DUPER ROBOT AI CONTROLLER (Made by Dan)"
print ">> Type 'help()' for a list of commands"

while True:

    # Get the user's next line of input.
    try:
        command = raw_input("- ")
    except KeyboardInterrupt, Exception:
        print "\n>> Exiting cleanly..."
        userInterface.exit()
        sys.exit(0)
        
    # Try and run the command.
    try:
        command = command.strip()
        exec "userInterface."+command
    except Exception as e:
        # The user has mistyped the command.
        print ">> Error executing command: "+str(e)
