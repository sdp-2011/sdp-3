// **********************************************************************
//
// Copyright (c) 2003-2010 ZeroC, Inc. All rights reserved.
//
// This copy of Ice is licensed to you under the terms described in the
// ICE_LICENSE file included in this distribution.
//
// **********************************************************************

// Ice version 3.4.1

package ControlTopic;

// <auto-generated>
//
// Generated from file `Control.ice'
//
// Warning: do not edit this file.
//
// </auto-generated>


public interface _ControlDel extends Ice._ObjectDel
{
    void connect(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void disconnect(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void setLeftMotorSpeed(int speed, java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void setRightMotorSpeed(int speed, java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void driveForward(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void driveForwardSpeed(int speed, java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void driveBackward(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void driveBackwardSpeed(int speed, java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void driveStop(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void turnLeft(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void turnLeftSpeed(int speed, java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void turnRight(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void turnRightSpeed(int speed, java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void kick(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void sendInt(int i, java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    void shutDownRobot(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;

    boolean isMoving(java.util.Map<String, String> __ctx)
        throws IceInternal.LocalExceptionWrapper;
}
