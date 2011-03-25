

	-- How to Use --


First of all make sure you have ICE installed: http://www.zeroc.com/
Then make sure you have the binaries from the install in your system PATH variable.

You can then run CompileAll.bat or CompileAll.sh to compile all the topics. Make sure there are no errors.

What you then need to do is add this directory to the classpath of whatever language you're using.
In python it can be done like this:

import sys
sys.path.append(".../Path/To/This/Directory")

With java you must add it to the CLASS_PATH system variable.

You can then use these classes into your java/python/whatever code.


	-- Overview of Channels --
	

These are the communication channels we're going to be using.

Below is a diagram of how the communication is working, over what formats, components and languages.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	 Robot (Java)
		|
		| [Bluetooth Socket]
		|
	Controller (Java)
		|
		| [Control Topic]
		|
	   AI (Python?)
		| 
		| [WorldState Topic]
		|
	  Vision (Python)


Robot & World <----> Vision [Indirect]

	  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Because we're using ICE we can also use these communication topics to test the AI within the simulator.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


	Simulator (Python)
		|
		| [Control Topic]
		|
	   AI (Python?)
		| 
		| [WorldState Topic]
		|
	Simulator (Python)


Simulator <----> Simulator [Direct]
	
	
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	
	-- Description of Topics --
	

Hello.ice

	This is just an example channel to show the syntax.

	
WorldState.ice
	
	This channel is published to by the Visual component (or by the simulator). It specifies the locations of objects in the world. It is read by the AI.

	
Control.ice
	
	This channel is published to by the AI, it is read from by the Controller, which forwards commands to the robot in an understandable format.