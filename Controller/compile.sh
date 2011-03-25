#!/bin/sh

# Classpath
export CLASSPATH=$CLASSPATH:../Topics

echo "---------------------------------"
echo "   Compiling NXJ Communicator"
echo "---------------------------------"
nxjpcc Communicator.java
echo ""
echo "---------------------------------"
echo "Compiling Ice Controller Classes"
echo "---------------------------------"
nxjpcc ControllerI.java
nxjpcc Controller.java
echo "Done!"
