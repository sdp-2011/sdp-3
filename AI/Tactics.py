import math
from AIMath import *

def CheckKick(world_state):
    """
    Checks if the current world state means that any kick we take on the 
    ball would be within the correct angles to score a goal (i.e. meaning
    that the ball ends up below the north goalpost and above the south
    goalpost.)
    """

    # Draw a cone forward from the robot.
    cone_angle = (math.pi / 6)
    
    right_edge = Polar(world_state.robotRadius, \
            angleModulus(world_state.myRot + cone_angle), world_state.myPos)
    left_edge = Polar(world_state.robotRadius, \
            angleModulus(world_state.myRot - cone_angle), world_state.myPos)
    
    # The polar vector between our position and the ball.
    me_ball = Polar(world_state.ballPos, world_state.myPos)

    # check ball within the angle between the two edges.
    angle_edge_ball = diffAngles(me_ball.angle, right_edge.angle)
    angle_edges = diffAngles(left_edge.angle, right_edge.angle)
    if (angle_edge_ball > angle_edges) and \
            ( ((angle_edge_ball > 0 ) and (angle_edges > 0)) or \
              ((angle_edge_ball < 0 ) and (angle_edges < 0))):
        print "ball not in cone (angles only)"
        return False
    
    right_edge = right_edge.toCartesian()
    left_edge = left_edge.toCartesian()

    # Check range of shot 
    if world_state.shootingDirection == 1:
        
        # shooting Right so want right edge to south goalpost
        right_to_goal = Polar(world_state.goalpostAttackNorth, right_edge)
        left_to_goal = Polar(world_state.goalpostAttackSouth, left_edge)
        #print "right_to_goal " + str(right_to_goal.angle)
        #print "left_to_goal " + str(left_to_goal.angle) 

    else:
        #print "Right"
        # shooting Left so want right edge to north goalpost
        right_to_goal = Polar(world_state.goalpostAttackSouth, right_edge)
        left_to_goal = Polar(world_state.goalpostAttackNorth, left_edge)
        #print "right_to_goal " + str(right_to_goal.angle)
        #print "left_to_goal " + str(left_to_goal.angle) 
    
    # check if our facing is between the two angles.
    angle_posts = angleRotDiff(left_to_goal.angle, right_to_goal.angle)
    #print "angle_posts: " + str(angle_posts)

    # angle between the left post and my facing.
    angle_post_facing = angleRotDiff(left_to_goal.angle, world_state.myRot)
    #print "angle_post_facing " + str(angle_post_facing)
    
    if ((angle_posts + (math.pi/10)) > angle_post_facing ) and (((angle_posts >0 ) and \
            (angle_post_facing > 0)) or ((angle_posts < 0 ) and (angle_post_facing < 0))) : 
        print "angle_posts " + str(angle_posts) + " angle_post_facing " + str(angle_post_facing)
        return True
        # Relaxed the rules for this.
    else: 
        #print "angle_posts: " + str(angle_posts)
        #print "angle_post_facing " + str(angle_post_facing)
        return False


def FindShootingPosition(world_state):
    """
    Returns a position for the robot to go to from where he can take a shot.
    """

    northpost_me = Polar(world_state.goalpostAttackNorth, world_state.ballPos)
    southpost_me = Polar(world_state.goalpostAttackSouth, world_state.ballPos)
    opp_position = Polar(world_state.oppPos, world_state.ballPos)
    northpost_angle = northpost_me.angle
    southpost_angle = southpost_me.angle

    target_angle = FindShootingAngle(opp_position,northpost_angle,southpost_angle, world_state)

    target_angle_from_goal = angleModulus(target_angle - math.pi)

    target_extension = world_state.robotRadius + 50
    target_point = Polar(target_extension, target_angle_from_goal, world_state.ballPos)
    target_point = target_point.toCartesian()

    # Check to see if shooting position is off the pitch
    if target_point.y < world_state.pitchNorth or \
       target_point.y > world_state.pitchSouth or \
       target_point.x < world_state.pitchLeft or \
       target_point.x > world_state.pitchRight :
        
        return None

    return target_point
    
    
def FindShootingAngle(opp_pos_polar, angle_north_post, angle_south_post, world_state):
    """
    Finds an angle from which there is a clear line between the origin position and the goal.

    - Checks if the center of mass of the opposing robot is within the angle between the
        posts. If this is true it calculates the difference between the obstacle and the goals, picks the largest
        one and returns a aimpoint which is the midpoint between that post and the edge of the robot. 

        theata is the calculation of half of the angle the obstacle ocupies using
        the tangent function and the max radius of the robot and the distance the robot is from
        the our location. Basic triangles stuff ;)
    - Finally if there are no obstacles it justs picks the midpoint of the goal as the aimpoint.
    
    - If there are obstacles it picks an angle heading straight toward the goal
    """
    
    inbetween = False
    difference_angles = 0.0
    angle_between_post = angleRotDiff(angle_north_post, angle_south_post)
    angle_between_northpost_opp = angleRotDiff(angle_north_post, opp_pos_polar.angle)

    if (angle_between_post < 0.0) and (angle_between_northpost_opp < 0.0):
        if (angle_between_post < angle_between_northpost_opp):
            inbetween = True
    elif (angle_between_post > 0.0) and (angle_between_northpost_opp > 0.0):
        if (angle_between_post > angle_between_northpost_opp):
            inbetween = True    

    if inbetween:
        theata = math.atan(world_state.robotRadius/opp_pos_polar.distance)             
        difference_bottom_south = diffAngles(angle_south_post, opp_pos_polar.angle)
        difference_top_north = diffAngles(angle_north_post, opp_pos_polar.angle)
        if (difference_top_north > difference_bottom_south) and (difference_top_north > theata):
        #    print "Opponent closer to South post"
            if (angle_between_post < 0.0):
                obs = angleModulus(opp_pos_polar.angle + theata)
            else:
                obs = angleModulus(opp_pos_polar.angle - theata)

            difference_angles = angleRotDiff(angle_north_post, obs)
            return angleModulus(angle_north_post + difference_angles/2.0)
        elif (difference_top_north < difference_bottom_south) and (difference_bottom_south > theata):
         #   print "Opponent closer to North post"
            if (angle_between_post < 0.0):
                obs = angleModulus(opp_pos_polar.angle - theata)
            else:
                obs = angleModulus(opp_pos_polar.angle + theata)

            obs = angleModulus(opp_pos_polar.angle + theata)
            difference_angles = angleRotDiff(angle_south_post, obs)
            return angleModulus(angle_south_post + difference_angles/2.0)

    difference_angles = angleRotDiff(angle_north_post, angle_south_post)
    return angleModulus(angle_north_post + difference_angles/2.0)

    
def FindDefencePosition(world_state):
        """
        Looks for a shooting angle from the ball's position.
        """
        northpost_me = Polar(world_state.goalpostDefendNorth, world_state.ballPos)
        southpost_me = Polar(world_state.goalpostDefendSouth, world_state.ballPos)
        northpost_angle = northpost_me.angle
        southpost_angle = southpost_me.angle
        opp_position = Polar(northpost_me.distance, angleModulus(northpost_angle + math.pi) ,world_state.ballPos)
        
        angle = FindShootingAngle(opp_position,northpost_angle,southpost_angle, world_state)
        if angle:
            target_point = Polar(40, angle, world_state.ballPos)
            target_point = target_point.toCartesian()
            return target_point
        else:
            return None
            
            
def CheckForObstacle(world_state):
    """
    Checks if the ball or the robot are obstacles
    Returns a Boolean

    - Obstacle has to be in front of the robot and within the obstacleAvoidanceDist in worldState for True to be returned
    """
    opp_position = Polar(world_state.oppPos, world_state.myPos)
    me_ball = Polar(world_state.ballPos, world_state.myPos)
    angle_me_opp = diffAngles(world_state.myRot, opp_position.angle) 
    angle_me_ball = diffAngles(world_state.myRot, me_ball.angle)
    avoid_angle = math.pi/3.0        

    #print "op pos " + str(opp_position)
    #print "ball pos" + str(me_ball)

    if self.avoiding:
        avoid_angle = math.pi/2.0 

    #if ((opp_position.distance - world_state.robotRadius) < world_state.obstacleAvoidanceDist) and (angle_me_opp < avoid_angle):
    #    print "! o_o opp obstacle"
    #    self.driver.enabled = True
    #    return True
    if (me_ball.distance < world_state.obstacleAvoidanceDist) and \
            (angle_me_ball < avoid_angle):

        if (distance(world_state.ballPos, world_state.oppGoalMidpoint)) > \
                (distance(world_state.myPos, world_state.oppGoalMidpoint)):
            print "! o=o=o ball obstacle"
            self.state = "AVOID_BALL"
            self.driver.enabled = True
            return True

    self.driver.enabled = True
    self.avoiding = False
#        print "Obstacle check: False"
    return False
    
    
    
def AvoidObstacle(world_state):
    
    opp_position = Polar(world_state.oppPos, world_state.myPos)
    me_ball = Polar(world_state.ballPos, world_state.myPos)

    obstacle = opp_position
    if (opp_position.distance - world_state.robotRadius) < me_ball.distance:
        obstacle = opp_position
    else:
        obstacle = me_ball
    
    if angleRotDiff(world_state.myRot, obstacle.angle) > 0.0:
        target_angle = angleModulus(obstacle.angle - (math.pi/3))
        #print "obstacle to left at angle " + str(obstacle.angle) + " Target angle " + str(target_angle) + " My angle " + str(world_state.myRot) + " angle diff" + str(angleRotDiff(world_state.myRot, obstacle.angle)) 
    else:
        target_angle = angleModulus(obstacle.angle + (math.pi/3))
        #print "opponent to right at angle " str(obstacle.angle) + " Target angle " + str(target_angle) + " My angle " + str(world_state.myRot) + " angle diff" + str(angleRotDiff(world_state.myRot, obstacle.angle)) 
    
    target_dist_add = 75.0
    target_point = V(-1.0,-1.0)
    # prevents target point being negative
#        print "Entering while"
    while (target_point.x < 0) or (target_point.y < 0):
        target_point = Polar((obstacle.distance + target_dist_add), target_angle, world_state.myPos)
        target_point = target_point.toCartesian()
        target_dist_add -= 5.0
#        print "Exited while"
    
    return target_point
    
    
    
def CalculateWaypoint(target, world_state, frametime):
    """
    Draws virtual polygon between target and each point exactly 1 radius away from center robot.
    Lines are of length 2*radius, tan(radius/robot_to_target_distance)
    """
    
    #print "Going Through"

    global last_time
    this_time = time.time()
    if (last_time + 1) > this_time:
        return target
    else:
        last_time = this_time
    
    print "Checking Waypoint"

    me_ball = Polar(world_state.ballPos, world_state.myPos)
    me_target = Polar(target, world_state.myPos)
    
    angle_target_ball = angleRotDiff(me_ball.angle, me_target.angle)
    
    if (angle_target_ball > 0):
        # Ball is on the left of the target
        ball_distance = me_ball.distance * math.sin(angle_target_ball)
        if ball_distance < world_state.robotRadius * 1.5:
            print 'Avoiding target on the left'
            # We're fucked, need to find a new waypoint
            turn_distance = math.sqrt((me_ball.distance ** 2) - (ball_distance ** 2))
            avoidance_point = Polar(turn_distance, me_target.angle, world_state.myPos).toCartesian()
            extend_distance = world_state.robotRadius * 2 - ball_distance
            avoidance_vector = Polar(extend_distance, Polar(avoidance_point, world_state.ballPos).angle, world_state.ballPos).toCartesian()

            # Now we can tell the driver to find a new target point
            print 'Chosen vector: ' + str(world_state.ballPos + avoidance_vector)
            return world_state.ballPos + avoidance_vector
        else:
            # We good, robot won't touch
            print 'Avoidance not needed'
            return target	
    elif (angle_target_ball < 0):
        # Ball is on the right of the target
        ball_distance = me_ball.distance * math.sin(angleModulus(angle_target_ball))
        if ball_distance < world_state.robotRadius * 1.5:
            print 'Avoiding target on the right'
            # We're fucked, need to find a new waypoint
            turn_distance = math.sqrt((me_ball.distance ** 2) - (ball_distance ** 2))
            avoidance_point = Polar(turn_distance, me_target.angle, world_state.myPos).toCartesian()
            extendDistance = world_state.robotRadius * 2 - ball_distance
            avoidance_vector = Polar(extendDistance, Polar(avoidance_point, world_state.ballPos).angle, world_state.ballPos).toCartesian()

            # Now we can tell the driver to find a new target point
            print 'Chosen vector: ' + str(world_state.ballPos + avoidance_vector)
            return world_state.ballPos + avoidance_vector
        else:
            # We good, robot won't touch
            print 'Avoidance not needed'
            return target	
    else:
        print 'Avoiding target on our direct path'
        # Ball is in direct path to the target, we're fucked
        # Get perpendicular vector to the ball position
        perp_vector = Vector(-world_state.ballPos.y, world_state.ballPos.x)
        # Extend it by 3 times robot radius
        avoidance_vector = Polar(world_state.robotRadius * 3, Polar(perp_vector, world_state.ballPos).angle, world_state.ballPos).toCartesian()

        print 'Chosen vector: ' + str(world_state.ballPos + avoidance_vector)
        return world_state.ballPos + avoidance_vector
      
    # Didn't get anything, return original target
    return target


def FindGoalDefencePoint(world_state):
    
    mid_point = world_state.ourGoalMidpoint

    if world_state.shootingDirection == 0: # Shooting right
        mid_point.x += world_state.robotRadius + 30
    else: # Shooting left
        mid_point.x -= world_state.robotRadius + 30
    
    return mid_point

        


def AvoidBall(world_state, target):
    """
    If the ball is between us, our goal and our waypoint then we need to move around it.
    Otherwise we'll end up scoring own goals.
    
    To do this, finds the angle between the vector to the ball and the vector to the waypoint
    If this angle is small enough, returns the ball position with an increment or decrement on the y axis.    
    """    
    
    robot_to_target = normalize(target - world_state.myPos)
    robot_to_ball = normalize(world_state.ballPos - world_state.myPos)
    dot_angle_between = dot(robot_to_target, robot_to_ball)
    
    # Dotted angle has to be clamped due to float rounding errors.
    dot_angle_between = min(dot_angle_between, 1.0)
    dot_angle_between = max(dot_angle_between, 0.0)
    
    angle_between_ball_target = math.acos(dot_angle_between)

    #print "Ball Pos: " + str(world_state.ballPos) + " Robot Pos: " + str(world_state.myPos) + " Target Pos: "+ str(target)
    #print "Angle between ball vector and target vector: "+ str(math.degrees(angle_between_ball_target))

    # Shooting Right, ball behind us, target behind ball. OR
    # Shooting Left, ball behind us, target behind ball.
    if ((world_state.shootingDirection == 1) and (target.x > world_state.ballPos.x) and (world_state.ballPos.x > world_state.myPos.x)) or \
       ((world_state.shootingDirection == 0) and (target.x < world_state.ballPos.x) and (world_state.ballPos.x < world_state.myPos.x)):
        
        if abs(angle_between_ball_target) < (math.pi/10):
            print "Need Waypoint!"
            top_waypoint = world_state.ballPos - V(0, world_state.robotRadius + 50)
            bottom_waypoint = world_state.ballPos + V(0, world_state.robotRadius + 50)

            top_distance = distance(top_waypoint, world_state.myPos)
            bottom_distance = distance(bottom_waypoint, world_state.myPos)
            
            if top_distance < bottom_distance:
                print "Using Top Waypoint"
                return top_waypoint
            else:
                print "Using Bottom Waypoint"
                return bottom_waypoint
    
    return target


def ClampPositionY(world_state, position, edge_buffer = 30):
    """
    Clamps a Position's Y component onto the pitch, given a certain buffer.
    """

    top_bound = world_state.pitchNorth + edge_buffer
    bottom_bound = world_state.pitchSouth - edge_buffer
    
    position.y  = max( position.y, top_bound)
    position.y  = min( position.y, bottom_bound)

    return position


def ClampPositionX(world_state, position, edge_buffer = 30):
    """
    Clamps a Position's X component onto the pitch, given a certain buffer.
    """

    left_bound = world_state.pitchLeft + edge_buffer
    right_bound = world_state.pitchRight - edge_buffer
    
    position.x  = max( position.x, left_bound)
    position.x  = min( position.x, right_bound)

    return position

def checkIntersectGoal(self, world_state):
    """
    Checks if there is a clear line between the robot the ball and the goal
    returns True or false.
    """

    me_ball_vec = vectorFrom(world_state.myPos, world_state.ballPos)
    
    if me_ball_vec.y == 0.0 or me_ball_vec.x == 0.0:
        return False
    
    lamda = (world_state.goalpostAttackNorth.x - world_state.myPos.x) / \
            me_ball_vec.x # x intersection when lamda is this value
    y_intersect = world_state.ballPos.y + (lamda * me_ball_vec.y) # substitute to find y 

    if (y_intersect > world_state.goalpostAttackNorth.y - 15) and (y_intersect < world_state.goalpostAttackSouth.y + 15) and (lamda >= 0): 
         #return V(world_state.goalpostAttackNorth.x, y_intersect)
        print "checkIntersectGoal line on goal"
        return True
    else:
        print "checkIntersectGoal NO line on goal"
        return False 
