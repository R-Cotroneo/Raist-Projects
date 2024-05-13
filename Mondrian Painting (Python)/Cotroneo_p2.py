# File: Cotroneo_p2.py
# Author: Raist Cotroneo
# Date: 11/22/2022
# Section: 1001-1
# E-mail: vincent.cotroneo@maine.edu
# Description:
# Creates a Piet Mondrian painting using recursion
# Collaboration:
# No one collaborated with

from graphics import *
from random import *


YELLOW = 0.9
RED = 0.25
BLUE = 0.15
MIN_SPLIT = 0.31
MAX_SPLIT = 0.68
RECT_MIN = 90
CANVAS_WIDTH = 800
CANVAS_HEIGHT = 800

# Function that determines if the rectangle's dimension (width/height) needs to be split
# Returns the new dimension (if possible) and a boolean that tells the program whether or not it could be split
def splitter(dimension, canD):
    if dimension > RECT_MIN:
        if dimension > (canD // 2):
            dimSplitter = uniform(MIN_SPLIT, MAX_SPLIT)
            newD = int(dimension * dimSplitter)
            isSplittable = True
        else:
            determineSplit = randrange(RECT_MIN, int(1.5 * dimension))
            if RECT_MIN < determineSplit < dimension:
                dimSplitter = uniform(MIN_SPLIT, MAX_SPLIT)
                newD = int(dimension * dimSplitter)
                isSplittable = True
            else:
                newD = dimension
                isSplittable = False
        return newD, isSplittable
    else:
        isSplittable = False
        return dimension, isSplittable

# Recursive function for painting
def makePainting(rect, window):
    width = rect[2] - rect[0]
    height = rect[3] - rect[1]
    xTuple = splitter(width, CANVAS_WIDTH)
    yTuple = splitter(height, CANVAS_HEIGHT)

    # As long as the splitter() function returns a true, the recursion will continue
    if (xTuple[1] == True) or (yTuple[1] == True):

        # Adds the dimension to the previous x/y coordinates to make new coordinates
        newX = rect[0] + xTuple[0]
        newY = rect[1] + yTuple[0]

        # 4 rectangles created if both dimensions could be split
        # 2 rectangles created if only one or the other is split
        if (newX != width) and (newY != height):
            r1 = [rect[0], rect[1], newX, newY]
            r2 = [rect[0], newY, newX, rect[3]]
            r3 = [newX, rect[1], rect[2], newY]
            r4 = [newX, newY, rect[2], rect[3]]
            Rect1 = Rectangle(Point(r1[0], r1[1]), Point(r1[2], r1[3]))
            Rect2 = Rectangle(Point(r2[0], r2[1]), Point(r2[2], r2[3]))
            Rect3 = Rectangle(Point(r3[0], r3[1]), Point(r3[2], r3[3]))
            Rect4 = Rectangle(Point(r4[0], r4[1]), Point(r4[2], r4[3]))
            Rect1.setOutline("black")
            Rect1.draw(window)
            Rect2.setOutline("black")
            Rect2.draw(window)
            Rect3.setOutline("black")
            Rect3.draw(window)
            Rect4.setOutline("black")
            Rect4.draw(window)
            return makePainting(r1, window), makePainting(r2, window), makePainting(r3, window), makePainting(r4, window)
        elif newX != width:
            r5 = [rect[0], rect[1], newX, rect[3]]
            r6 = [newX, rect[1], rect[2], rect[3]]
            Rect5 = Rectangle(Point(r5[0], r5[1]), Point(r5[2], r5[3]))
            Rect6 = Rectangle(Point(r6[0], r6[1]), Point(r6[2], r6[3]))
            Rect5.setOutline("black")
            Rect5.draw(window)
            Rect6.setOutline("black")
            Rect6.draw(window)
            return makePainting(r5, window), makePainting(r6, window)
        elif newY != height:
            r7 = [rect[0], rect[1], rect[2], newY]
            r8 = [rect[0], newY, rect[2], rect[3]]
            Rect7 = Rectangle(Point(r7[0], r7[1]), Point(r7[2], r7[3]))
            Rect8 = Rectangle(Point(r8[0], r8[1]), Point(r8[2], r8[3]))
            Rect7.setOutline("black")
            Rect7.draw(window)
            Rect8.setOutline("black")
            Rect8.draw(window)
            return makePainting(r7, window), makePainting(r8, window)

    # Base case which draws the final rectangle of the recursive call and colors it in
    else:
        theRect = Rectangle(Point(rect[0], rect[1]), Point(rect[2], rect[3]))
        theRect.setOutline("black")
        r = uniform(0, 2)
        if r < BLUE:
            theRect.setFill("blue")
        elif r < RED:
            theRect.setFill("red")
        elif r < YELLOW:
            theRect.setFill("yellow")
        else:
            theRect.setFill("white")
        theRect.draw(window)
        return
    

def main():
    canvas = GraphWin("The Canvas", CANVAS_WIDTH, CANVAS_HEIGHT)
    theRect = [0, 0, CANVAS_WIDTH, CANVAS_HEIGHT]
    makePainting(theRect, canvas)
    canvas.getMouse()
    canvas.close()
main()
