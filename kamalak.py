# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 13:10:15 2021

@author: turgu
"""
import turtle
sc = turtle.Screen()
pen = turtle.Turtle()
def semi_circle(col,rad,val):
    pen.color(col)
    pen.circle(rad, -180)
    pen.up()
    pen.setpos(val, 0)
    pen.down()
    pen.right(180)
col = ['violet','indigo', 'black','green','yellow','orange','red']
sc.setup(600,600)
sc.bgcolor('blue')
pen.right(90)
pen.width(10)
pen.speed(7)
for i in range(7):
    semi_circle(col[i], 10*(i+8), -10*(i+1))
pen.hideturtle()       