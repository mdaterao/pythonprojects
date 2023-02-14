# -*- coding: utf-8 -*-
"""
Template code


1) Get the user inputs
2) Generate a window with the appropriate size based on the user inputs
3) Place the initial circle (ball) in the window as described in the instruction
4) Run the simulation and check when the ball hits the horizontal edge. Make the necessary adjustment
5) Termiunate the simulation when the stopping criteria is reached.



"""

from graphics import *
import time
import math

circle_radius = float(input('Enter Radius (a number between 10 and 20 inclusive): '))
initial_speed = float(input('Enter initial speed (a number between 30 and 80 inclusive) : '))
angle_degrees = float(input('Enter a number for initial trajectory angle in degrees (30-90 inclusive): '))
time_increment = float(input('Enter a value for the simulation time increment:  '))
g = 9.8

#window
angle_radians = math.radians(angle_degrees)
h = ((initial_speed**2 * (math.sin(angle_radians))**2) / (2*g))
r = (initial_speed**2 * (math.sin(2 * angle_radians)) / g)
xwindow = math.floor(2 * (r + (3 * circle_radius)))
ywindow = math.floor(h + (3 * circle_radius))
win = GraphWin('Trajectory', xwindow, ywindow)


print(xwindow, ywindow)




#circle
p1 = Point(circle_radius, ywindow - circle_radius)
# Define circle
C = Circle(p1, circle_radius)
# Set colors
C.setFill ("yellow")
# draw circle
C.draw(win)

'''
dx = circle_radius + (initial_speed * math.cos(angle_radians)) * time_increment
dy = (ywindow - circle_radius) + ((initial_speed * math.sin(angle_radians) - 9.8 * time_increment)) * time_increment
C.move(dx,dy)
'''
x_speed = initial_speed * math.cos(angle_radians)
y_speed = initial_speed * math.sin(angle_radians)
floor = ywindow - circle_radius
totalY = floor
floorCount = 0

time_of_flight = (y_speed * 2)/g
num_steps = 2* math.ceil(time_of_flight / time_increment)


for i in range(num_steps):
    dx = x_speed * time_increment
    dy = -(y_speed - (g*time_increment)) * time_increment
    y_speed = y_speed - (g*time_increment)
    totalY = totalY + dy
    if(totalY > floor):
        initial_speed = initial_speed * .56
        x_speed = initial_speed * math.cos(angle_radians)
        y_speed = initial_speed * math.sin(angle_radians)
        time_of_flight = (y_speed * 2)/g
        num_steps = 2* math.ceil(time_of_flight / time_increment)
        i = 0
        dx = x_speed * time_increment
        dy = -(y_speed - (g*time_increment)) * time_increment
        floorCount = floorCount + 1
    if(floorCount == 3):
        break
    C.move(dx,dy)
    time.sleep(time_increment)
    
    



""" DO NOT MODIFY OR WRITE ANYTHING BELOW """

# Close after mouse click
try:
    win.getMouse()    
    win.close()
except:
    pass
    
