#!/bin/bash

export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:./lib

javac -cp $HOME/SDP/Ice-3.4.1/lib/Ice.jar:./lib/v4l4j.jar:../Topics:. *.java
