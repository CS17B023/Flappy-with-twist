
from tkinter import *
from random import *
from turtle import *
import tkinter as tk

from freegames import vector
from math import *
from module import *
state = {'score': 0}
cnt = {'count':1}
bird = vector(0, 0)
balls = []
writer = Turtle(visible=False)


def tap(x, y):
    "Move bird up in response to screen tap."
    up = vector(0, 30)
    bird.move(up)

def inside(point):
    "Return True if point on screen."
    return -200 < point.x < 200 and -200 < point.y < 200

def draw(alive):
    "Draw screen objects."
    clear()

    goto(bird.x, bird.y)

    if alive:
        dot(10, 'green')
    else:
        dot(10, 'red')

    for ball in balls:
        goto(ball.x, ball.y)
        dot(20, 'black')

    update()

    

def move():
    "Update object positions."
    writer.undo()
    writer.write(state['score'])
    state['score'] += 1


    bird.y -= 5   
    for ball in balls:
        ball.x -= 3

    if randrange(10) == 0:
        y = randrange(-199, 199)
        ball = vector(199, y)
        balls.append(ball)

    while len(balls) > 0 and not inside(balls[0]):
        balls.pop(0)

    if not inside(bird):
        draw(False)

        if cnt['count'] == 1:
            cnt['count']=0
            bird.x =0
            bird.y =0
            del balls[:]

            dialog()
            #textinput("123","wee")
            move()
        return

    for ball in balls:
        if abs(ball - bird) < 15:
            draw(False)
            if cnt['count'] == 1:
                cnt['count']=0
                bird.x =0
                bird.y =0
                del balls[:]
                dialog()
                move()
            return

    draw(True)
    ontimer(move, 50)

setup(420, 420, 370, 0)
hideturtle()
up()
tracer(False)

writer.setx(160)
writer.sety(180)
writer.clear()
writer.color('black')
writer.write(state['score'])
onscreenclick(tap)
move()
done()

