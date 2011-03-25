
	-- Overview --

There are three classes here, Communicator, Controller and ControllerI.

Communicator deals with sending messages to the robot via bluetooth, as such it is compiled with nxjc.

Controller and ControllerI deal with Recieving messages via Ice and using these messages to call some function in the Communicator. Controller is largely about setting up the connection to the Ice topic, where as CommunicatorI is an implementation of the "Control" interface (in the ControlTopic module).
	
	
	-- Some things to check before you go ahead and try to compile --

1. Ice is added to your classpath (E.G -- C:\Program Files (x86)\ZeroC\Ice-3.4.1\lib\Ice.jar or /usr/share/java/Ice.java)

2. The Topics folder is added to your classpath (E.G -- C:\Robot\src\Topics or /home/username/Robot/src/Topics)

3. nxj is set up correctly and you can use "nxjpcc" as a command line tool.
