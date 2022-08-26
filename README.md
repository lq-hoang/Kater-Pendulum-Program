# Kater-Pendulum-Program
Simple program that models collected data from a Kater pendulum

Taking real data recorded from a Kater Pendulum in the McLennan Physical Laboratories, the program 
produces a graph showing the data and the linear fits (y = mx + b). The program then gives the values to create the 
line equations along with the goodness of fit values. This data can then be used to find the point of
intersection for the lines, leading to the corresponding period (and therefore particular acceleration
due to gravity at the pendulum location).

## To Run
1. Download both the .py and txt files in the repository.
2. Open .py file on a Python IDE and run.

## To Acelaration Due to Gravity
1. Find the point of intersection of both lines and plug the x value into either equation to find T 
2. Given the length L from real_data.txt, we can find the the accelaration due to gravity g
   using the equation g = 4(pi^2)(L/T^2)
 
*note* the equation we use is the one for a simple pendulum. This is because the g equation
used for Kater pendulums can be reduced into this equation as we have the periods on both the upright
and flipped pendulums be the same and the sum of lengths from the centre of gravity of the pendulum to 
each side of the pendulum is equal to the total length of the pendulum.
