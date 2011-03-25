"""
This is a simple test script, which uses the communication interface
to send some basic commands to the robot.
"""

import time
import ControlInterface
#import VisionInterface


# Show off the vision interface.

#vi = VisionInterface.VisionInterface()


raw_input("Ready to move onto demonstrating basic controls?")

# Show off the control interface.
ci = ControlInterface.ControlInterface()

ci.connect()

print "Original positions:"

print "Requesting ball position from server:"
#print vi.getBallLocation()
print 
print "Requesting our position from server:"
#print vi.getMyLocation()
print 
print "Requesting the opponent position from server:"
#print vi.getOpponentLocation()
print
time.sleep(0.5)

print "Forward..."
ci.driveForward(10.5)
time.sleep(2.5)

ci.driveStop()
time.sleep(1)

print "Current positions:"

print "Requesting ball position from server:"
#print vi.getBallLocation()
print 
print "Requesting our position from server:"
#print vi.getMyLocation()
print 
print "Requesting the opponent position from server:"
#print vi.getOpponentLocation()
print
time.sleep(0.5)

print "And back..."
ci.driveBackward(10.5)
time.sleep(2)

ci.driveStop()
time.sleep(1)

print "Current positions:"

print "Requesting ball position from server:"
#print vi.getBallLocation()
print 
print "Requesting our position from server:"
#print vi.getMyLocation()
print 
print "Requesting the opponent position from server:"
#print vi.getOpponentLocation()
print
time.sleep(0.5)

print "Left..."
ci.turnLeft(180.5)
time.sleep(2)

ci.driveStop()
time.sleep(1)

print "Current positions:"

print "Requesting ball position from server:"
#print vi.getBallLocation()
print 
print "Requesting our position from server:"
#print vi.getMyLocation()
print 
print "Requesting the opponent position from server:"
#print vi.getOpponentLocation()
print
time.sleep(0.5)

print "And right..."
ci.turnRight(180.5)
time.sleep(2)

ci.driveStop()
time.sleep(1)

print "Current positions:"

print "Requesting ball position from server:"
#print vi.getBallLocation()
print 
print "Requesting our position from server:"
#print vi.getMyLocation()
print 
print "Requesting the opponent position from server:"
#print vi.getOpponentLocation()
print
time.sleep(0.5)

print "Kick!"

ci.kick()

print "Final positions:"

print "Requesting ball position from server:"
#print vi.getBallLocation()
print 
print "Requesting our position from server:"
#print vi.getMyLocation()
print 
print "Requesting the opponent position from server:"
#print vi.getOpponentLocation()
print
time.sleep(0.5)

raw_input("Ready to take penalty kick?")

time.sleep(1)
ci.kick()

print "Finished: Disconnecting..."
ci.disconnect()
print "Disconnected!"
