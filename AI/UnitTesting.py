import unittest

from Instructions import *
from Strategies import *
from WorldState import *
from AIMath import *
from math import *

class TestStrategies(unittest.TestCase):
    
    def setUp(self):
    
        self.world_state = WorldState()
        self.world_state.ballPos = V(100,60)
        self.world_state.myPos = V(90,59)
        self.world_state.oppPos = V(120,60)

        self.world_state.goalpostAttackNorth = V(243,30)
        self.world_state.goalpostAttackSouth = V(243,90)
        self.world_state.goalpostDefendNorth = V(0, 30)
        self.world_state.goalpostDefendSouth = V(0, 90)

        self.world_state.myRot = math.pi
        self.world_state.oppRot = math.pi

        self.world_state.kickerDistance = 5.0
        self.world_state.kickerWidth = 10.0

        self.world_state.ballVelocity = V(0,0)
        self.world_state.meMoving = True
        
        #self.addTypeEqualityFunc(Command,lambda x, y: x.name == y.name and x.args == y.args )
    
    def testShooting(self):
        shootingTest = Shooting()
        output = shootingTest.iterate(self.world_state,0)
        
        self.assertEqual(output, [])

    def testCheckCurrentShot(self):
        shootingTest = Shooting()
        output = shootingTest.checkCurrentShot(self.world_state)
        
        self.assertEqual(output, V(243.0,75.3))

    def testObstacleAdvoidance(self):
        obsAv = ObstacleAdvoidance()
        #output = obsAv.iterate(self.world_state,0)
        #print "TEST3: "+str(output)

    def testMoveToBall(self):
        driver = Driver()
        driver.target = self.world_state.ballPos
        output = driver.iterate(self.world_state,0)
        
        self.assertEqual(output, [Command("Stop")] )

    """
    def testDefence(self):
        defend = Defend()
        output = defend.iterate(self.world_state,0)
        print output
        self.assertEqual(output, [])
    """

class TestMaths(unittest.TestCase):
    
    def testAngleBetween(self):
        a = []
        a.append(["O>2", angleRotDiff(2.0,1.0), " Expected -1"])
        a.append(["O<2", angleRotDiff(1.0,2.0), " Expected 1"])
        a.append(["O>2 round origin", angleRotDiff((1.75 * math.pi),(0.25 * math.pi)), " Expected pi/2"])
        a.append(["O<2 round origin", angleRotDiff((0.25 * math.pi),(1.75 * math.pi)), " Expected -pi/2"])
        #for b in a:
        #    print b[0] + ": " + str(b[1]) + b[2]
            
    def testPolars(self):
        a = []
        a.append(["TL", Polar(V(1,1), V(2,2))])
        a.append(["TC", Polar(V(2,1), V(2,2))])
        a.append(["TR", Polar(V(3,1), V(2,2))])
        a.append(["CL", Polar(V(1,2), V(2,2))])
        a.append(["CC",  Polar(V(2,2), V(2,2))])
        a.append(["CR",  Polar(V(3,2), V(2,2))])
        a.append(["BL",  Polar(V(1,3), V(2,2))])
        a.append(["BC",  Polar(V(2,3), V(2,2))])
        a.append(["BR",  Polar(V(3,3), V(2,2))])

        #for b in a:
        #    print b[0] + ": " + str(b[1].angle/ math.pi)
        #    print "To Cartesian " + str(b[1].toCartesian())
    
    
unittest.main()
