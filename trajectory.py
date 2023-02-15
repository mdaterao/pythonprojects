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

'''
user input defined parameters: circle radius, initial speed of the ball,
angle relative to horizontal line, time increment
'''
circle_radius = float(
    input('Enter Radius (a number between 10 and 20 inclusive): '))
initial_speed = float(
    input('Enter initial speed (a number between 30 and 80 inclusive) : '))
angle_degrees = float(input(
    'Enter a number for initial trajectory angle in degrees (30-90 inclusive): '))
time_increment = float(
    input('Enter a value for the simulation time increment:  '))

# gravitational acceleration = 9.8 meters per second squared
g = 9.8

#angle in radians
angle_radians = math.radians(angle_degrees)
#maximum height and range of the ball
h = ((initial_speed**2 * (math.sin(angle_radians))**2) / (2*g))
r = (initial_speed**2 * (math.sin(2 * angle_radians)) / g)
#display window
xwindow = math.floor(2 * (r + (3 * circle_radius)))
ywindow = math.floor(h + (3 * circle_radius))
win = GraphWin('Trajectory', xwindow, ywindow)


#circle
p1 = Point(circle_radius, ywindow - circle_radius)
# Define circle
C = Circle(p1, circle_radius)
# Set colors
C.setFill("yellow")
# draw circle
C.draw(win)

#speed in y direction, speed in x direction
x_speed = initial_speed * math.cos(angle_radians)
y_speed = initial_speed * math.sin(angle_radians)
#horizontal edge of display window
floor = ywindow - circle_radius
#total y displacement of the ball
totalY = floor

#Time of flight and number of steps required for ball to hit the ground
time_of_flight = (y_speed * 2)/g
num_steps = 2 * math.ceil(time_of_flight / time_increment)

#For loop calculates the trajectory of the ball, and ensures that it stays in the frame
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
        num_steps = 2 * math.ceil(time_of_flight / time_increment)
        i = 0
        dx = x_speed * time_increment
        dy = -(y_speed - (g*time_increment)) * time_increment
    C.move(dx, dy)
    time.sleep(time_increment)
    print(f'interation, {i + 1} dx = {dx:.3f}, dy = {dy:.3f}')


""" DO NOT MODIFY OR WRITE ANYTHING BELOW """

# Close after mouse click
try:
    win.getMouse()
    win.close()
except:
    pass
