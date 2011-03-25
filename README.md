System Design Project

Team 3 -- Legoal

Members

* Fraser Cormack
* Daniel Holden
* Chun-Hao Hu (Andy Hu)
* Ewan Jones
* Craig Lawrie
* Michael Li Yan Hui
* David Mark 
* Brian McMahon
* Stephen McGruer
* Karol Pogonowski

Tutor: Joseph Henry

Installation Requirements:

You will need the ICE framework installed (http://www.zeroc.com/ice.html) - if
you're doing SDP there should be a guide to doing this up on the forums. You
will also need LeJOS (http://lejos.sourceforge.net/) installed - again, there
should be a guide on the forums. Everything else should be here.

Notes:

* Be aware that our code is not perfect - far from it. We suggest that you do
  not follow our Strategy code, as it doesn't really work too tell, although
  you may find some use from reading it. The Vision and Communication (ICE)
  systems may be useful though - we think they're quite good. 

* One known bug is that occasionally (such as on the final tournament day for
  us...) the Controller will be sending commands to the Robot, and the Robot
  will just... not pick them up, and will also not throw any sort of
  IOException. Yay. No idea why it happens - might be worth replacing some
  Thread.yield()'s with Thread.sleep()
