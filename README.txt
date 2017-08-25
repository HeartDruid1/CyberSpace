################################
#                              #
#                              #
#       CYBERSPACE             #
#                              #
#                              #
#                              #
##    github/HeartDruid1       #
#                              #
#                              #
################################ 

August 24, 2017

--------------------------------

CyberSpace is currently released under the GPL 3.0 License


For more information please view the LICENSE.txt file


CyberSpace is also a heavily modified version of sentdex's 'A bit racey'

--------------------------------

Required Packages



CyberSpace is written in Python 3 using PyGame (I used version 1.9.2 I believe but it should work with other versions) so those two things are the only required dependencies.

--------------------------------

How To Run



Once Python3 and PyGame are installed simply run the CyberSpace.py file

--------------------------------

Known Bugs and Issues



1. None ;) Currently the most stable version!

--------------------------------

Plot/Story



You are a pilot aboard the Cyber-SpaceShip tasked with reaching record breaking Internet Speeds.

This is a task that only the bravest of Internet Surfers can achieve. 
While cruising at super high
speeds you must dodge clusters of data that are conveniently marked as 3 1/2 Inch Floppy Disks and Emails which
 are marked as regular snail mail.

--------------------------------

Controls



Use the up and down arrow keys to navigate the main menu (The cursor is green so whatever choice is green is your current selection)

and use the ENTER or RETURN key to make your menu selection

Use the left and right arrow keys to move from side to side avoiding the oncoming obstacles.

--------------------------------

Extra Details for the Extra Nerdy ;)



Scoring System:

The scoring system adds 1 to your score plus the current "Download Speed"




Collision Detection:

Every frame the 'collide' function checks the following conditions


-The (Player's X position) is less than (the obstacles X position plus its width)

-The (Player's Y position) is less than (the obstacles Y position plus its height)

-The (obstacle's X position) is less than (the Player's X position plus its width)

-The (obstacle's Y position) is less than (the Player's Y position plus its height)


If all of the above conditions return 'True' then it will register as a collision (and a game over ;) )




Falling Speed:

The falling speed of each object is indicated as the "Download Speed" after every loop the speed increases by 0.25

This number is the rate that the Y position increases.



------------------------------

Contact or Get Involved



If you wish to contact me you can either email me at fergusonnick74@gmail.com

or on twitter @sh0esbdriftin

or contribute to this project on GitHub ;)
