# Python_Demo


Author :: Charles C. Stevenson
Date :: 14.02.2019


A current non-comprehensive demo of my python code

I wrote this program keeping in mind that it may be developed further into a fully fledged pacman clone.
It consist of three static elements:
	
	Floor
	Wall
	Dot

and 1 dynamic element:

	Pacman

I refer to these elements as actors as that make up the scene that is casted by the theatre.
The actors each have their separate classes. Though the interface for the static elements
is very similar to one another. They all consist of three different functions

	1) a constructor
	2) a collision response
	3) a render

This was very convienant so when I iterated through objects and routed responses I didn't need
to care about which object was being called. It was a little time-consuming to setup like this.
However; it paid off when it came to adding features in that I only needed to worry about the actor itself.
The core of this is keeping api's similar to one another but also building an iterator to pass custom objects through
one for loop. I did this with a TYPE : String dictionary. I didn't want to pass around types because I was worried about
circular dependancies so I decided to pass around strings that represented types instead. You can see this dictionary
in the Level's constructor.


To parse the level(s) I used a kind of bitmap in which integers represented actors. Therefore, almost any configuration
of map could be made out of these config files. I decided to try to replicate that original level from pacman. 


Testing::

As far as testing went, I actually tested second and wrote my code first. The testing is not as comprehensive
as it should be but systematically tests some of the easier cases in the code. It still needs a file parsing test,
collision tests, and level tests. I chose not to implement these tests mainly because I'm out of time and still
feel it delivers a representation of my abilities. 


If this fails to run, let me know. Hope you enjoy.


**IN ORDER TO MOVE**
use the arrow keys!
