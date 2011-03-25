"""
Simple logging. Very simple to use.
Just import and then call the "Log" function anywhere, passing it the log name 
and the message.

Logs are stored in the logs sub folder.

from Logger import *

Log("Debug","Hello! I am a debug message!")
"""

import datetime

logs = {}

def OpenLogger():
    """ Opens the log files for writing. Note, this will clear the current logs. """
    global logs
    logs["Command"] = open('./logs/command.log', 'w')
    logs["Debug"] = open('./logs/debug.log','w')
    logs["Strategy"] = open('./logs/strategy.log','w')
    logs["Intercept"] = open('./logs/intercept.log','w')

def CloseLogger():
    global logs
    map(lambda x : x.close() , logs.values())
    
def Log(log,msg):
    global logs
    timestamp = str(datetime.datetime.now().time())
    logs[log].write(timestamp + " || " + str(msg) + "\n")
