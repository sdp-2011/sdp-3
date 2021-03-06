// **********************************************************************
//
// Copyright (c) 2003-2010 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

// Ice version 3.4.1

package WorldStateTopic;

// <auto-generated>
//
// Generated from file `WorldState.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>


public interface WorldStatePrx extends Ice.ObjectPrx
{
    public long getUpdateID();

    public long getUpdateID(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getUpdateID();

    public Ice.AsyncResult begin_getUpdateID(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getUpdateID(Ice.Callback __cb);

    public Ice.AsyncResult begin_getUpdateID(java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_getUpdateID(Callback_WorldState_getUpdateID __cb);

    public Ice.AsyncResult begin_getUpdateID(java.util.Map<String, String> __ctx, Callback_WorldState_getUpdateID __cb);

    public long end_getUpdateID(Ice.AsyncResult __result);

    public Ball getBallPosition();

    public Ball getBallPosition(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getBallPosition();

    public Ice.AsyncResult begin_getBallPosition(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getBallPosition(Ice.Callback __cb);

    public Ice.AsyncResult begin_getBallPosition(java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_getBallPosition(Callback_WorldState_getBallPosition __cb);

    public Ice.AsyncResult begin_getBallPosition(java.util.Map<String, String> __ctx, Callback_WorldState_getBallPosition __cb);

    public Ball end_getBallPosition(Ice.AsyncResult __result);

    public Robot getYellowRobot();

    public Robot getYellowRobot(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getYellowRobot();

    public Ice.AsyncResult begin_getYellowRobot(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getYellowRobot(Ice.Callback __cb);

    public Ice.AsyncResult begin_getYellowRobot(java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_getYellowRobot(Callback_WorldState_getYellowRobot __cb);

    public Ice.AsyncResult begin_getYellowRobot(java.util.Map<String, String> __ctx, Callback_WorldState_getYellowRobot __cb);

    public Robot end_getYellowRobot(Ice.AsyncResult __result);

    public Robot getBlueRobot();

    public Robot getBlueRobot(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getBlueRobot();

    public Ice.AsyncResult begin_getBlueRobot(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getBlueRobot(Ice.Callback __cb);

    public Ice.AsyncResult begin_getBlueRobot(java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_getBlueRobot(Callback_WorldState_getBlueRobot __cb);

    public Ice.AsyncResult begin_getBlueRobot(java.util.Map<String, String> __ctx, Callback_WorldState_getBlueRobot __cb);

    public Robot end_getBlueRobot(Ice.AsyncResult __result);

    public int getPitch();

    public int getPitch(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getPitch();

    public Ice.AsyncResult begin_getPitch(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getPitch(Ice.Callback __cb);

    public Ice.AsyncResult begin_getPitch(java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_getPitch(Callback_WorldState_getPitch __cb);

    public Ice.AsyncResult begin_getPitch(java.util.Map<String, String> __ctx, Callback_WorldState_getPitch __cb);

    public int end_getPitch(Ice.AsyncResult __result);

    public int getShootingDirection();

    public int getShootingDirection(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getShootingDirection();

    public Ice.AsyncResult begin_getShootingDirection(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getShootingDirection(Ice.Callback __cb);

    public Ice.AsyncResult begin_getShootingDirection(java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_getShootingDirection(Callback_WorldState_getShootingDirection __cb);

    public Ice.AsyncResult begin_getShootingDirection(java.util.Map<String, String> __ctx, Callback_WorldState_getShootingDirection __cb);

    public int end_getShootingDirection(Ice.AsyncResult __result);

    public int getTeamColour();

    public int getTeamColour(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getTeamColour();

    public Ice.AsyncResult begin_getTeamColour(java.util.Map<String, String> __ctx);

    public Ice.AsyncResult begin_getTeamColour(Ice.Callback __cb);

    public Ice.AsyncResult begin_getTeamColour(java.util.Map<String, String> __ctx, Ice.Callback __cb);

    public Ice.AsyncResult begin_getTeamColour(Callback_WorldState_getTeamColour __cb);

    public Ice.AsyncResult begin_getTeamColour(java.util.Map<String, String> __ctx, Callback_WorldState_getTeamColour __cb);

    public int end_getTeamColour(Ice.AsyncResult __result);
}
