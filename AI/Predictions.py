import math
import copy

from AIMath import *
from Logger import *

def predictBallPos(world_state, time):
    """
    Predicts the position of the ball for some time in future.
    TODO: wall bounce.
    """
    friction = 0.9

    loc = world_state.ballPos
    proj = (world_state.ballVel * time)
    
    #point = loc + (proj * friction)
    point = clamp( point, V(world_state.pitchLeft,world_state.pitchNorth), V(world_state.pitchRight, world_state.pitchSouth) )

    # uncomment following lines for no bouncing.
    return point
        
    prev_loc = copy.copy(loc)
    loc, proj = bounceVectorOnWall(proj, loc, world_state.pitchNorth, "Y-")
    loc, proj = bounceVectorOnWall(proj, loc, world_state.pitchSouth, "Y+")
    loc, proj = bounceVectorOnWall(proj, loc, world_state.pitchLeft,  "X-")
    loc, proj = bounceVectorOnWall(proj, loc, world_state.pitchRight, "X+") 

    if proj.x < world_state.pitchLeft : print "Reflected off pitch "+str(proj)
    if proj.x > world_state.pitchRight : print "Reflected off pitch "+str(proj)
    if proj.y < world_state.pitchNorth : print "Reflected off pitch "+str(proj)
    if proj.y > world_state.pitchSouth : print "Reflected off pitch "+str(proj)

    return loc + proj
    
    while prev_loc != loc:
        prev_loc = copy.copy(loc)
        loc, proj = bounceVectorOnWall(proj, loc, world_state.pitchNorth, "Y-")
        loc, proj = bounceVectorOnWall(proj, loc, world_state.pitchSouth, "Y+")
        loc, proj = bounceVectorOnWall(proj, loc, world_state.pitchLeft,  "X-")
        loc, proj = bounceVectorOnWall(proj, loc, world_state.pitchRight, "X+") 
    
    return loc + proj
        
def bounceVectorOnWall(vector, loc, wall_pos, wall_type):
    
    dampening = 0.9

    if length(vector) == 0.0:
        return (loc, vector)
    
    if wall_type == "Y-" or wall_type == "Y+":
        diff = wall_pos - loc.y
        scale = diff / vector.y
        wall_dir = V(1,0)
    elif wall_type == "X-" or wall_type == "X+":
        diff = wall_pos - loc.x
        scale = diff / vector.x
        wall_dir = V(0,1)
        
    if scale > 0.0 and scale < 1.0: # hits a wall
        wall_v = vector * scale
        ext_v = vector * (1 - scale) * dampening
        
        # Sometimes, due to float rounding errors, this is greater than 1.0 or less than -1.0 (which dot shouldn't be)
        clamped = dot( normalize(wall_dir) , normalize(vector) )
        clamped = min(clamped,1.0)
        clamped = max(clamped,-1.0)
        
        # If angle greater than 90, then sub from 180 to find actual incident angle.
        hit_angle = math.acos(clamped)
        
        if hit_angle > math.pi/2:
            hit_angle = (math.pi - hit_angle)

        # For X wall type, if signs are different then rotation must be in opposite direction
        if wall_type == "X":
            if (vector.x > 0 and vector.y > 0) or (vector.x < 0 and vector.y < 0):
                hit_angle = -hit_angle

        # For Y wall type, if signs are same then rotation must be in opposite direction.
        elif wall_type == "Y":
            if (vector.x < 0 and vector.y > 0) or (vector.x > 0 and vector.y < 0):
                hit_angle = -hit_angle
        
        ext_v = rotate2D(ext_v, 2 * hit_angle)
        
        newloc = loc + wall_v
        newproj = -ext_v
        if wall_type == "Y+":
            newproj = V(-newproj.x,-newproj.y)
        if wall_type == "X+":
            newproj.x = -newproj.x
        return (newloc, newproj)
    
    return (loc, vector)
    

def predictRobotMovementTime(world_state, pos):
    """    
    Speed predictions, turn 50 maps to 0.5 and 150 maps to 1.55
    """
    FAST_ROT_SPEED = 1.55
    SLOW_ROT_SPEED = 0.5
    
    FORWARD_SPEED = 30

    me_target = Polar(pos,world_state.myPos)
    angle = abs(diffAngles(me_target.angle, world_state.myRot))
    
    if angle > 90:
        turn_time = ((angle - 90) / FAST_ROT_SPEED) + (90 / SLOW_ROT_SPEED)
    else:
        turn_time = (angle / SLOW_ROT_SPEED)
    
    forward_time = me_target.distance / FORWARD_SPEED
    
    return turn_time + forward_time
    
