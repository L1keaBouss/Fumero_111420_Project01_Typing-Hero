import subprocess
import time
import string
import sys
from os import path
from graphics import *
from random import *

width = 400
length = 600

lives = 3
def game():
    win = GraphWin("Jimbo Defense", length, width)
    protect = Image(Point(50, 200),"jimbo.gif")
    protect.draw(win)
    projectiles(win,lives)


def projectiles(win, lives):
    score = 0
    textBox = Text(Point(320,200), "Type or Perish: ")
    textBox.draw(win)
    while(lives != 0):
        livesTxt = Text(Point(560,25),"Lives: " + str(lives))
        livesTxt.draw(win)
        timer = 0
        timelimit = 3 #change here to make it harder/easier
        spawn = randrange(380)
        projectiles = Text(Point(400,200),choice(string.ascii_lowercase))
        projectiles.draw(win)
        projectiles.setSize(20)
        while(timer <= timelimit):
            time.sleep(0.5)
            timer = timer + 1
            update(100)
            x = win.checkKey()
            if(x == projectiles.getText()):
                projectiles.setTextColor("green")
                score += 1
                time.sleep(2)                
                livesTxt.setText("Lives: " + str(lives))
                projectiles.setText(choice(string.ascii_lowercase))
                projectiles.setTextColor("black")
                timer = 0

            livesTxt.setText("Lives: " + str(lives))
            projectiles.setTextColor("black")

            if(timer >= timelimit):
                lives = lives - 1
                projectiles.setTextColor("red")
                time.sleep(2)
                projectiles.setTextColor("black")
                projectiles.setText(choice(string.ascii_lowercase))
                timer = 0
                livesTxt.setText("Lives: " + str(lives))
            if (lives <= 0):
                projectiles.setText(choice("PERISHED X-X"))
                textBox.setText("Score: " + str(score) + "\n Click To Exit")
                win.getMouse()
                win.close()
def main():
     game()
     pass
main()
    