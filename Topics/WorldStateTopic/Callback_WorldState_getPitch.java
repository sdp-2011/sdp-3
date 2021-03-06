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


public abstract class Callback_WorldState_getPitch extends Ice.TwowayCallback
{
    public abstract void response(int __ret);

    public final void __completed(Ice.AsyncResult __result)
    {
        WorldStatePrx __proxy = (WorldStatePrx)__result.getProxy();
        int __ret = 0;
        try
        {
            __ret = __proxy.end_getPitch(__result);
        }
        catch(Ice.LocalException __ex)
        {
            exception(__ex);
            return;
        }
        response(__ret);
    }
}
