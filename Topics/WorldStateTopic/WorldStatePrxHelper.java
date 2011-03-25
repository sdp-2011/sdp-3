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


public final class WorldStatePrxHelper extends Ice.ObjectPrxHelperBase implements WorldStatePrx
{
    public Ball
    getBallPosition()
    {
        return getBallPosition(null, false);
    }

    public Ball
    getBallPosition(java.util.Map<String, String> __ctx)
    {
        return getBallPosition(__ctx, true);
    }

    private Ball
    getBallPosition(java.util.Map<String, String> __ctx, boolean __explicitCtx)
    {
        if(__explicitCtx && __ctx == null)
        {
            __ctx = _emptyContext;
        }
        int __cnt = 0;
        while(true)
        {
            Ice._ObjectDel __delBase = null;
            try
            {
                __checkTwowayOnly("getBallPosition");
                __delBase = __getDelegate(false);
                _WorldStateDel __del = (_WorldStateDel)__delBase;
                return __del.getBallPosition(__ctx);
            }
            catch(IceInternal.LocalExceptionWrapper __ex)
            {
                __handleExceptionWrapper(__delBase, __ex);
            }
            catch(Ice.LocalException __ex)
            {
                __cnt = __handleException(__delBase, __ex, null, __cnt);
            }
        }
    }

    private static final String __getBallPosition_name = "getBallPosition";

    public Ice.AsyncResult begin_getBallPosition()
    {
        return begin_getBallPosition(null, false, null);
    }

    public Ice.AsyncResult begin_getBallPosition(java.util.Map<String, String> __ctx)
    {
        return begin_getBallPosition(__ctx, true, null);
    }

    public Ice.AsyncResult begin_getBallPosition(Ice.Callback __cb)
    {
        return begin_getBallPosition(null, false, __cb);
    }

    public Ice.AsyncResult begin_getBallPosition(java.util.Map<String, String> __ctx, Ice.Callback __cb)
    {
        return begin_getBallPosition(__ctx, true, __cb);
    }

    public Ice.AsyncResult begin_getBallPosition(Callback_WorldState_getBallPosition __cb)
    {
        return begin_getBallPosition(null, false, __cb);
    }

    public Ice.AsyncResult begin_getBallPosition(java.util.Map<String, String> __ctx, Callback_WorldState_getBallPosition __cb)
    {
        return begin_getBallPosition(__ctx, true, __cb);
    }

    private Ice.AsyncResult begin_getBallPosition(java.util.Map<String, String> __ctx, boolean __explicitCtx, IceInternal.CallbackBase __cb)
    {
        __checkAsyncTwowayOnly(__getBallPosition_name);
        IceInternal.OutgoingAsync __result = new IceInternal.OutgoingAsync(this, __getBallPosition_name, __cb);
        try
        {
            __result.__prepare(__getBallPosition_name, Ice.OperationMode.Normal, __ctx, __explicitCtx);
            IceInternal.BasicStream __os = __result.__os();
            __os.endWriteEncaps();
            __result.__send(true);
        }
        catch(Ice.LocalException __ex)
        {
            __result.__exceptionAsync(__ex);
        }
        return __result;
    }

    public Ball end_getBallPosition(Ice.AsyncResult __result)
    {
        Ice.AsyncResult.__check(__result, this, __getBallPosition_name);
        if(!__result.__wait())
        {
            try
            {
                __result.__throwUserException();
            }
            catch(Ice.UserException __ex)
            {
                throw new Ice.UnknownUserException(__ex.ice_name());
            }
        }
        Ball __ret;
        IceInternal.BasicStream __is = __result.__is();
        __is.startReadEncaps();
        __ret = new Ball();
        __ret.__read(__is);
        __is.endReadEncaps();
        return __ret;
    }

    public Robot
    getBlueRobot()
    {
        return getBlueRobot(null, false);
    }

    public Robot
    getBlueRobot(java.util.Map<String, String> __ctx)
    {
        return getBlueRobot(__ctx, true);
    }

    private Robot
    getBlueRobot(java.util.Map<String, String> __ctx, boolean __explicitCtx)
    {
        if(__explicitCtx && __ctx == null)
        {
            __ctx = _emptyContext;
        }
        int __cnt = 0;
        while(true)
        {
            Ice._ObjectDel __delBase = null;
            try
            {
                __checkTwowayOnly("getBlueRobot");
                __delBase = __getDelegate(false);
                _WorldStateDel __del = (_WorldStateDel)__delBase;
                return __del.getBlueRobot(__ctx);
            }
            catch(IceInternal.LocalExceptionWrapper __ex)
            {
                __handleExceptionWrapper(__delBase, __ex);
            }
            catch(Ice.LocalException __ex)
            {
                __cnt = __handleException(__delBase, __ex, null, __cnt);
            }
        }
    }

    private static final String __getBlueRobot_name = "getBlueRobot";

    public Ice.AsyncResult begin_getBlueRobot()
    {
        return begin_getBlueRobot(null, false, null);
    }

    public Ice.AsyncResult begin_getBlueRobot(java.util.Map<String, String> __ctx)
    {
        return begin_getBlueRobot(__ctx, true, null);
    }

    public Ice.AsyncResult begin_getBlueRobot(Ice.Callback __cb)
    {
        return begin_getBlueRobot(null, false, __cb);
    }

    public Ice.AsyncResult begin_getBlueRobot(java.util.Map<String, String> __ctx, Ice.Callback __cb)
    {
        return begin_getBlueRobot(__ctx, true, __cb);
    }

    public Ice.AsyncResult begin_getBlueRobot(Callback_WorldState_getBlueRobot __cb)
    {
        return begin_getBlueRobot(null, false, __cb);
    }

    public Ice.AsyncResult begin_getBlueRobot(java.util.Map<String, String> __ctx, Callback_WorldState_getBlueRobot __cb)
    {
        return begin_getBlueRobot(__ctx, true, __cb);
    }

    private Ice.AsyncResult begin_getBlueRobot(java.util.Map<String, String> __ctx, boolean __explicitCtx, IceInternal.CallbackBase __cb)
    {
        __checkAsyncTwowayOnly(__getBlueRobot_name);
        IceInternal.OutgoingAsync __result = new IceInternal.OutgoingAsync(this, __getBlueRobot_name, __cb);
        try
        {
            __result.__prepare(__getBlueRobot_name, Ice.OperationMode.Normal, __ctx, __explicitCtx);
            IceInternal.BasicStream __os = __result.__os();
            __os.endWriteEncaps();
            __result.__send(true);
        }
        catch(Ice.LocalException __ex)
        {
            __result.__exceptionAsync(__ex);
        }
        return __result;
    }

    public Robot end_getBlueRobot(Ice.AsyncResult __result)
    {
        Ice.AsyncResult.__check(__result, this, __getBlueRobot_name);
        if(!__result.__wait())
        {
            try
            {
                __result.__throwUserException();
            }
            catch(Ice.UserException __ex)
            {
                throw new Ice.UnknownUserException(__ex.ice_name());
            }
        }
        Robot __ret;
        IceInternal.BasicStream __is = __result.__is();
        __is.startReadEncaps();
        __ret = new Robot();
        __ret.__read(__is);
        __is.endReadEncaps();
        return __ret;
    }

    public int
    getPitch()
    {
        return getPitch(null, false);
    }

    public int
    getPitch(java.util.Map<String, String> __ctx)
    {
        return getPitch(__ctx, true);
    }

    private int
    getPitch(java.util.Map<String, String> __ctx, boolean __explicitCtx)
    {
        if(__explicitCtx && __ctx == null)
        {
            __ctx = _emptyContext;
        }
        int __cnt = 0;
        while(true)
        {
            Ice._ObjectDel __delBase = null;
            try
            {
                __checkTwowayOnly("getPitch");
                __delBase = __getDelegate(false);
                _WorldStateDel __del = (_WorldStateDel)__delBase;
                return __del.getPitch(__ctx);
            }
            catch(IceInternal.LocalExceptionWrapper __ex)
            {
                __handleExceptionWrapper(__delBase, __ex);
            }
            catch(Ice.LocalException __ex)
            {
                __cnt = __handleException(__delBase, __ex, null, __cnt);
            }
        }
    }

    private static final String __getPitch_name = "getPitch";

    public Ice.AsyncResult begin_getPitch()
    {
        return begin_getPitch(null, false, null);
    }

    public Ice.AsyncResult begin_getPitch(java.util.Map<String, String> __ctx)
    {
        return begin_getPitch(__ctx, true, null);
    }

    public Ice.AsyncResult begin_getPitch(Ice.Callback __cb)
    {
        return begin_getPitch(null, false, __cb);
    }

    public Ice.AsyncResult begin_getPitch(java.util.Map<String, String> __ctx, Ice.Callback __cb)
    {
        return begin_getPitch(__ctx, true, __cb);
    }

    public Ice.AsyncResult begin_getPitch(Callback_WorldState_getPitch __cb)
    {
        return begin_getPitch(null, false, __cb);
    }

    public Ice.AsyncResult begin_getPitch(java.util.Map<String, String> __ctx, Callback_WorldState_getPitch __cb)
    {
        return begin_getPitch(__ctx, true, __cb);
    }

    private Ice.AsyncResult begin_getPitch(java.util.Map<String, String> __ctx, boolean __explicitCtx, IceInternal.CallbackBase __cb)
    {
        __checkAsyncTwowayOnly(__getPitch_name);
        IceInternal.OutgoingAsync __result = new IceInternal.OutgoingAsync(this, __getPitch_name, __cb);
        try
        {
            __result.__prepare(__getPitch_name, Ice.OperationMode.Normal, __ctx, __explicitCtx);
            IceInternal.BasicStream __os = __result.__os();
            __os.endWriteEncaps();
            __result.__send(true);
        }
        catch(Ice.LocalException __ex)
        {
            __result.__exceptionAsync(__ex);
        }
        return __result;
    }

    public int end_getPitch(Ice.AsyncResult __result)
    {
        Ice.AsyncResult.__check(__result, this, __getPitch_name);
        if(!__result.__wait())
        {
            try
            {
                __result.__throwUserException();
            }
            catch(Ice.UserException __ex)
            {
                throw new Ice.UnknownUserException(__ex.ice_name());
            }
        }
        int __ret;
        IceInternal.BasicStream __is = __result.__is();
        __is.startReadEncaps();
        __ret = __is.readInt();
        __is.endReadEncaps();
        return __ret;
    }

    public int
    getShootingDirection()
    {
        return getShootingDirection(null, false);
    }

    public int
    getShootingDirection(java.util.Map<String, String> __ctx)
    {
        return getShootingDirection(__ctx, true);
    }

    private int
    getShootingDirection(java.util.Map<String, String> __ctx, boolean __explicitCtx)
    {
        if(__explicitCtx && __ctx == null)
        {
            __ctx = _emptyContext;
        }
        int __cnt = 0;
        while(true)
        {
            Ice._ObjectDel __delBase = null;
            try
            {
                __checkTwowayOnly("getShootingDirection");
                __delBase = __getDelegate(false);
                _WorldStateDel __del = (_WorldStateDel)__delBase;
                return __del.getShootingDirection(__ctx);
            }
            catch(IceInternal.LocalExceptionWrapper __ex)
            {
                __handleExceptionWrapper(__delBase, __ex);
            }
            catch(Ice.LocalException __ex)
            {
                __cnt = __handleException(__delBase, __ex, null, __cnt);
            }
        }
    }

    private static final String __getShootingDirection_name = "getShootingDirection";

    public Ice.AsyncResult begin_getShootingDirection()
    {
        return begin_getShootingDirection(null, false, null);
    }

    public Ice.AsyncResult begin_getShootingDirection(java.util.Map<String, String> __ctx)
    {
        return begin_getShootingDirection(__ctx, true, null);
    }

    public Ice.AsyncResult begin_getShootingDirection(Ice.Callback __cb)
    {
        return begin_getShootingDirection(null, false, __cb);
    }

    public Ice.AsyncResult begin_getShootingDirection(java.util.Map<String, String> __ctx, Ice.Callback __cb)
    {
        return begin_getShootingDirection(__ctx, true, __cb);
    }

    public Ice.AsyncResult begin_getShootingDirection(Callback_WorldState_getShootingDirection __cb)
    {
        return begin_getShootingDirection(null, false, __cb);
    }

    public Ice.AsyncResult begin_getShootingDirection(java.util.Map<String, String> __ctx, Callback_WorldState_getShootingDirection __cb)
    {
        return begin_getShootingDirection(__ctx, true, __cb);
    }

    private Ice.AsyncResult begin_getShootingDirection(java.util.Map<String, String> __ctx, boolean __explicitCtx, IceInternal.CallbackBase __cb)
    {
        __checkAsyncTwowayOnly(__getShootingDirection_name);
        IceInternal.OutgoingAsync __result = new IceInternal.OutgoingAsync(this, __getShootingDirection_name, __cb);
        try
        {
            __result.__prepare(__getShootingDirection_name, Ice.OperationMode.Normal, __ctx, __explicitCtx);
            IceInternal.BasicStream __os = __result.__os();
            __os.endWriteEncaps();
            __result.__send(true);
        }
        catch(Ice.LocalException __ex)
        {
            __result.__exceptionAsync(__ex);
        }
        return __result;
    }

    public int end_getShootingDirection(Ice.AsyncResult __result)
    {
        Ice.AsyncResult.__check(__result, this, __getShootingDirection_name);
        if(!__result.__wait())
        {
            try
            {
                __result.__throwUserException();
            }
            catch(Ice.UserException __ex)
            {
                throw new Ice.UnknownUserException(__ex.ice_name());
            }
        }
        int __ret;
        IceInternal.BasicStream __is = __result.__is();
        __is.startReadEncaps();
        __ret = __is.readInt();
        __is.endReadEncaps();
        return __ret;
    }

    public int
    getTeamColour()
    {
        return getTeamColour(null, false);
    }

    public int
    getTeamColour(java.util.Map<String, String> __ctx)
    {
        return getTeamColour(__ctx, true);
    }

    private int
    getTeamColour(java.util.Map<String, String> __ctx, boolean __explicitCtx)
    {
        if(__explicitCtx && __ctx == null)
        {
            __ctx = _emptyContext;
        }
        int __cnt = 0;
        while(true)
        {
            Ice._ObjectDel __delBase = null;
            try
            {
                __checkTwowayOnly("getTeamColour");
                __delBase = __getDelegate(false);
                _WorldStateDel __del = (_WorldStateDel)__delBase;
                return __del.getTeamColour(__ctx);
            }
            catch(IceInternal.LocalExceptionWrapper __ex)
            {
                __handleExceptionWrapper(__delBase, __ex);
            }
            catch(Ice.LocalException __ex)
            {
                __cnt = __handleException(__delBase, __ex, null, __cnt);
            }
        }
    }

    private static final String __getTeamColour_name = "getTeamColour";

    public Ice.AsyncResult begin_getTeamColour()
    {
        return begin_getTeamColour(null, false, null);
    }

    public Ice.AsyncResult begin_getTeamColour(java.util.Map<String, String> __ctx)
    {
        return begin_getTeamColour(__ctx, true, null);
    }

    public Ice.AsyncResult begin_getTeamColour(Ice.Callback __cb)
    {
        return begin_getTeamColour(null, false, __cb);
    }

    public Ice.AsyncResult begin_getTeamColour(java.util.Map<String, String> __ctx, Ice.Callback __cb)
    {
        return begin_getTeamColour(__ctx, true, __cb);
    }

    public Ice.AsyncResult begin_getTeamColour(Callback_WorldState_getTeamColour __cb)
    {
        return begin_getTeamColour(null, false, __cb);
    }

    public Ice.AsyncResult begin_getTeamColour(java.util.Map<String, String> __ctx, Callback_WorldState_getTeamColour __cb)
    {
        return begin_getTeamColour(__ctx, true, __cb);
    }

    private Ice.AsyncResult begin_getTeamColour(java.util.Map<String, String> __ctx, boolean __explicitCtx, IceInternal.CallbackBase __cb)
    {
        __checkAsyncTwowayOnly(__getTeamColour_name);
        IceInternal.OutgoingAsync __result = new IceInternal.OutgoingAsync(this, __getTeamColour_name, __cb);
        try
        {
            __result.__prepare(__getTeamColour_name, Ice.OperationMode.Normal, __ctx, __explicitCtx);
            IceInternal.BasicStream __os = __result.__os();
            __os.endWriteEncaps();
            __result.__send(true);
        }
        catch(Ice.LocalException __ex)
        {
            __result.__exceptionAsync(__ex);
        }
        return __result;
    }

    public int end_getTeamColour(Ice.AsyncResult __result)
    {
        Ice.AsyncResult.__check(__result, this, __getTeamColour_name);
        if(!__result.__wait())
        {
            try
            {
                __result.__throwUserException();
            }
            catch(Ice.UserException __ex)
            {
                throw new Ice.UnknownUserException(__ex.ice_name());
            }
        }
        int __ret;
        IceInternal.BasicStream __is = __result.__is();
        __is.startReadEncaps();
        __ret = __is.readInt();
        __is.endReadEncaps();
        return __ret;
    }

    public long
    getUpdateID()
    {
        return getUpdateID(null, false);
    }

    public long
    getUpdateID(java.util.Map<String, String> __ctx)
    {
        return getUpdateID(__ctx, true);
    }

    private long
    getUpdateID(java.util.Map<String, String> __ctx, boolean __explicitCtx)
    {
        if(__explicitCtx && __ctx == null)
        {
            __ctx = _emptyContext;
        }
        int __cnt = 0;
        while(true)
        {
            Ice._ObjectDel __delBase = null;
            try
            {
                __checkTwowayOnly("getUpdateID");
                __delBase = __getDelegate(false);
                _WorldStateDel __del = (_WorldStateDel)__delBase;
                return __del.getUpdateID(__ctx);
            }
            catch(IceInternal.LocalExceptionWrapper __ex)
            {
                __handleExceptionWrapper(__delBase, __ex);
            }
            catch(Ice.LocalException __ex)
            {
                __cnt = __handleException(__delBase, __ex, null, __cnt);
            }
        }
    }

    private static final String __getUpdateID_name = "getUpdateID";

    public Ice.AsyncResult begin_getUpdateID()
    {
        return begin_getUpdateID(null, false, null);
    }

    public Ice.AsyncResult begin_getUpdateID(java.util.Map<String, String> __ctx)
    {
        return begin_getUpdateID(__ctx, true, null);
    }

    public Ice.AsyncResult begin_getUpdateID(Ice.Callback __cb)
    {
        return begin_getUpdateID(null, false, __cb);
    }

    public Ice.AsyncResult begin_getUpdateID(java.util.Map<String, String> __ctx, Ice.Callback __cb)
    {
        return begin_getUpdateID(__ctx, true, __cb);
    }

    public Ice.AsyncResult begin_getUpdateID(Callback_WorldState_getUpdateID __cb)
    {
        return begin_getUpdateID(null, false, __cb);
    }

    public Ice.AsyncResult begin_getUpdateID(java.util.Map<String, String> __ctx, Callback_WorldState_getUpdateID __cb)
    {
        return begin_getUpdateID(__ctx, true, __cb);
    }

    private Ice.AsyncResult begin_getUpdateID(java.util.Map<String, String> __ctx, boolean __explicitCtx, IceInternal.CallbackBase __cb)
    {
        __checkAsyncTwowayOnly(__getUpdateID_name);
        IceInternal.OutgoingAsync __result = new IceInternal.OutgoingAsync(this, __getUpdateID_name, __cb);
        try
        {
            __result.__prepare(__getUpdateID_name, Ice.OperationMode.Normal, __ctx, __explicitCtx);
            IceInternal.BasicStream __os = __result.__os();
            __os.endWriteEncaps();
            __result.__send(true);
        }
        catch(Ice.LocalException __ex)
        {
            __result.__exceptionAsync(__ex);
        }
        return __result;
    }

    public long end_getUpdateID(Ice.AsyncResult __result)
    {
        Ice.AsyncResult.__check(__result, this, __getUpdateID_name);
        if(!__result.__wait())
        {
            try
            {
                __result.__throwUserException();
            }
            catch(Ice.UserException __ex)
            {
                throw new Ice.UnknownUserException(__ex.ice_name());
            }
        }
        long __ret;
        IceInternal.BasicStream __is = __result.__is();
        __is.startReadEncaps();
        __ret = __is.readLong();
        __is.endReadEncaps();
        return __ret;
    }

    public Robot
    getYellowRobot()
    {
        return getYellowRobot(null, false);
    }

    public Robot
    getYellowRobot(java.util.Map<String, String> __ctx)
    {
        return getYellowRobot(__ctx, true);
    }

    private Robot
    getYellowRobot(java.util.Map<String, String> __ctx, boolean __explicitCtx)
    {
        if(__explicitCtx && __ctx == null)
        {
            __ctx = _emptyContext;
        }
        int __cnt = 0;
        while(true)
        {
            Ice._ObjectDel __delBase = null;
            try
            {
                __checkTwowayOnly("getYellowRobot");
                __delBase = __getDelegate(false);
                _WorldStateDel __del = (_WorldStateDel)__delBase;
                return __del.getYellowRobot(__ctx);
            }
            catch(IceInternal.LocalExceptionWrapper __ex)
            {
                __handleExceptionWrapper(__delBase, __ex);
            }
            catch(Ice.LocalException __ex)
            {
                __cnt = __handleException(__delBase, __ex, null, __cnt);
            }
        }
    }

    private static final String __getYellowRobot_name = "getYellowRobot";

    public Ice.AsyncResult begin_getYellowRobot()
    {
        return begin_getYellowRobot(null, false, null);
    }

    public Ice.AsyncResult begin_getYellowRobot(java.util.Map<String, String> __ctx)
    {
        return begin_getYellowRobot(__ctx, true, null);
    }

    public Ice.AsyncResult begin_getYellowRobot(Ice.Callback __cb)
    {
        return begin_getYellowRobot(null, false, __cb);
    }

    public Ice.AsyncResult begin_getYellowRobot(java.util.Map<String, String> __ctx, Ice.Callback __cb)
    {
        return begin_getYellowRobot(__ctx, true, __cb);
    }

    public Ice.AsyncResult begin_getYellowRobot(Callback_WorldState_getYellowRobot __cb)
    {
        return begin_getYellowRobot(null, false, __cb);
    }

    public Ice.AsyncResult begin_getYellowRobot(java.util.Map<String, String> __ctx, Callback_WorldState_getYellowRobot __cb)
    {
        return begin_getYellowRobot(__ctx, true, __cb);
    }

    private Ice.AsyncResult begin_getYellowRobot(java.util.Map<String, String> __ctx, boolean __explicitCtx, IceInternal.CallbackBase __cb)
    {
        __checkAsyncTwowayOnly(__getYellowRobot_name);
        IceInternal.OutgoingAsync __result = new IceInternal.OutgoingAsync(this, __getYellowRobot_name, __cb);
        try
        {
            __result.__prepare(__getYellowRobot_name, Ice.OperationMode.Normal, __ctx, __explicitCtx);
            IceInternal.BasicStream __os = __result.__os();
            __os.endWriteEncaps();
            __result.__send(true);
        }
        catch(Ice.LocalException __ex)
        {
            __result.__exceptionAsync(__ex);
        }
        return __result;
    }

    public Robot end_getYellowRobot(Ice.AsyncResult __result)
    {
        Ice.AsyncResult.__check(__result, this, __getYellowRobot_name);
        if(!__result.__wait())
        {
            try
            {
                __result.__throwUserException();
            }
            catch(Ice.UserException __ex)
            {
                throw new Ice.UnknownUserException(__ex.ice_name());
            }
        }
        Robot __ret;
        IceInternal.BasicStream __is = __result.__is();
        __is.startReadEncaps();
        __ret = new Robot();
        __ret.__read(__is);
        __is.endReadEncaps();
        return __ret;
    }

    public static WorldStatePrx
    checkedCast(Ice.ObjectPrx __obj)
    {
        WorldStatePrx __d = null;
        if(__obj != null)
        {
            try
            {
                __d = (WorldStatePrx)__obj;
            }
            catch(ClassCastException ex)
            {
                if(__obj.ice_isA("::WorldStateTopic::WorldState"))
                {
                    WorldStatePrxHelper __h = new WorldStatePrxHelper();
                    __h.__copyFrom(__obj);
                    __d = __h;
                }
            }
        }
        return __d;
    }

    public static WorldStatePrx
    checkedCast(Ice.ObjectPrx __obj, java.util.Map<String, String> __ctx)
    {
        WorldStatePrx __d = null;
        if(__obj != null)
        {
            try
            {
                __d = (WorldStatePrx)__obj;
            }
            catch(ClassCastException ex)
            {
                if(__obj.ice_isA("::WorldStateTopic::WorldState", __ctx))
                {
                    WorldStatePrxHelper __h = new WorldStatePrxHelper();
                    __h.__copyFrom(__obj);
                    __d = __h;
                }
            }
        }
        return __d;
    }

    public static WorldStatePrx
    checkedCast(Ice.ObjectPrx __obj, String __facet)
    {
        WorldStatePrx __d = null;
        if(__obj != null)
        {
            Ice.ObjectPrx __bb = __obj.ice_facet(__facet);
            try
            {
                if(__bb.ice_isA("::WorldStateTopic::WorldState"))
                {
                    WorldStatePrxHelper __h = new WorldStatePrxHelper();
                    __h.__copyFrom(__bb);
                    __d = __h;
                }
            }
            catch(Ice.FacetNotExistException ex)
            {
            }
        }
        return __d;
    }

    public static WorldStatePrx
    checkedCast(Ice.ObjectPrx __obj, String __facet, java.util.Map<String, String> __ctx)
    {
        WorldStatePrx __d = null;
        if(__obj != null)
        {
            Ice.ObjectPrx __bb = __obj.ice_facet(__facet);
            try
            {
                if(__bb.ice_isA("::WorldStateTopic::WorldState", __ctx))
                {
                    WorldStatePrxHelper __h = new WorldStatePrxHelper();
                    __h.__copyFrom(__bb);
                    __d = __h;
                }
            }
            catch(Ice.FacetNotExistException ex)
            {
            }
        }
        return __d;
    }

    public static WorldStatePrx
    uncheckedCast(Ice.ObjectPrx __obj)
    {
        WorldStatePrx __d = null;
        if(__obj != null)
        {
            try
            {
                __d = (WorldStatePrx)__obj;
            }
            catch(ClassCastException ex)
            {
                WorldStatePrxHelper __h = new WorldStatePrxHelper();
                __h.__copyFrom(__obj);
                __d = __h;
            }
        }
        return __d;
    }

    public static WorldStatePrx
    uncheckedCast(Ice.ObjectPrx __obj, String __facet)
    {
        WorldStatePrx __d = null;
        if(__obj != null)
        {
            Ice.ObjectPrx __bb = __obj.ice_facet(__facet);
            WorldStatePrxHelper __h = new WorldStatePrxHelper();
            __h.__copyFrom(__bb);
            __d = __h;
        }
        return __d;
    }

    protected Ice._ObjectDelM
    __createDelegateM()
    {
        return new _WorldStateDelM();
    }

    protected Ice._ObjectDelD
    __createDelegateD()
    {
        return new _WorldStateDelD();
    }

    public static void
    __write(IceInternal.BasicStream __os, WorldStatePrx v)
    {
        __os.writeProxy(v);
    }

    public static WorldStatePrx
    __read(IceInternal.BasicStream __is)
    {
        Ice.ObjectPrx proxy = __is.readProxy();
        if(proxy != null)
        {
            WorldStatePrxHelper result = new WorldStatePrxHelper();
            result.__copyFrom(proxy);
            return result;
        }
        return null;
    }
}