import sys
import traceback

import Ice
sys.path.append("../Topics")

class Communicator(Ice.Application):
    """
    This is the communicator class, it acts as a Ice Client.
    """
    
    def __init__(self,moduleName,interfaceName,adapterName,portNum):
        """
        Contructs an Ice communicator to a certain modules's interface.
        If you're wondering why we're using __import__() and eval() it's
        because Ice constructs an actual module, which we need to import
        and perform operations on.
        """
        
        self.moduleName = moduleName
        self.interfaceName = interfaceName
        self.adapterName = adapterName
        self.portNum = portNum
        self.interface = None
        
        self.isConnected = False
        self.module = __import__(self.moduleName)
        
    def connect(self):
        self.ic = Ice.initialize()
        self.base = self.ic.stringToProxy(self.adapterName+":default -p "+str(self.portNum))
        self.interface = eval("self.module."+self.interfaceName+"Prx.checkedCast(self.base)")
        
        if not self.interface:
            raise RuntimeError("Invalid proxy")
        
        self.isConnected = True
            
    def disconnect(self):
        self.ic.destroy()
        self.isConnected = False
