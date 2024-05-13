# File: Cotroneo_p2_excredit.py
# Author: Raist Cotroneo
# Date: 12/8/2022
# Section: 1001-1
# E-mail: vincent.cotroneo@maine.edu
# Description:
# Extra credit for P2 where I include circles with the painting
# Collaboration:
# No one collaborated with

# THE "NamedColors.txt" FILE IS NEEDED FOR THIS TO WORK

from graphics import *
from random import *


COLOR_1 = 1
COLOR_2 = 0.33
COLOR_3 = 0.2
COLOR_4 = 0.3
COLOR_5 = 0.66
COLOR_6 = 0.98
MIN_SPLIT = 0.25
MAX_SPLIT = 0.75
RECT_MIN = 20
CANVAS_WIDTH = 1920
CANVAS_HEIGHT = 1080

# Function that determines if the rectangle's dimension (width/height) needs to be split
# Returns the new dimension (if possible) and a boolean that tells the program whether or not it could be split
def splitter(dimension, canD):
    if dimension > RECT_MIN:
        if (dimension > (canD // 2)) and (dimension % 2 == 0):
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
def makePainting(rect, window, colors):
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
            return makePainting(r1, window, colors), makePainting(r2, window, colors), makePainting(r3, window, colors), makePainting(r4, window, colors)
        elif newX != width:
            r5 = [rect[0], rect[1], newX, rect[3]]
            r6 = [newX, rect[1], rect[2], rect[3]]
            Rect5 = Rectangle(Point(r5[0], r5[1]), Point(r5[2], r5[3]))
            Rect6 = Rectangle(Point(r6[0], r6[1]), Point(r6[2], r6[3]))
            Rect5.setOutline("black")
            Rect5.draw(window)
            Rect6.setOutline("black")
            Rect6.draw(window)
            return makePainting(r5, window, colors), makePainting(r6, window, colors)
        elif newY != height:
            r7 = [rect[0], rect[1], rect[2], newY]
            r8 = [rect[0], newY, rect[2], rect[3]]
            Rect7 = Rectangle(Point(r7[0], r7[1]), Point(r7[2], r7[3]))
            Rect8 = Rectangle(Point(r8[0], r8[1]), Point(r8[2], r8[3]))
            Rect7.setOutline("black")
            Rect7.draw(window)
            Rect8.setOutline("black")
            Rect8.draw(window)
            return makePainting(r7, window, colors), makePainting(r8, window, colors)

    # Base case which draws the final shapes of the recursive call and colors them in
    else:
        # Creating rectangles
        theRect = Rectangle(Point(rect[0], rect[1]), Point(rect[2], rect[3]))
        theRect.setOutline(colors[8])
        color1 = uniform(0, 2)
        if color1 < COLOR_3:
            theRect.setFill(colors[0])
        elif color1 < COLOR_2:
            theRect.setFill(colors[1])
        elif color1 < COLOR_1:
            theRect.setFill(colors[2])
        else:
            theRect.setFill(colors[3])

        # Creating circles inside of rectangles
        xCenter = rect[0] + (width // 2)
        yCenter = rect[1] + (height // 2)
        if height <= width:
            cRadius = height // 4
        else:
            cRadius = width // 4
        aCircle = Circle(center=Point(xCenter, yCenter), radius=cRadius)
        aCircle.setOutline(colors[8])
        color2 = uniform(0, 2)
        if color2 < COLOR_4:
            aCircle.setFill(colors[4])
        elif color2 < COLOR_5:
            aCircle.setFill(colors[5])
        elif color2 < COLOR_6:
            aCircle.setFill(colors[6])
        else:
            aCircle.setFill(colors[7])
        
        theRect.draw(window)
        aCircle.draw(window)
        return
    

def main():
    # Obtaining a list of valid color names
    colorFile = open("NamedColors.txt", "r")
    file = colorFile.readlines()
    colors = []
    for i in file:
        line = i.strip()
        colors.append(line.lower())

    # Getting user colors
    listOfColors = []
    i = 0
    while i < 4:
        color = input("Enter a color name for rectangles: ")
        while (color.lower() in colors) != True:
            print("Invalid Input")
            color = input("Enter a color name for rectangles: ")
        listOfColors.append(color)
        i += 1
    j = 0
    while j < 4:
        color = input("Enter a color name for circles: ")
        while (color.lower() in colors) != True:
            print("Invalid Input")
            color = input("Enter a color name for circles: ")
        listOfColors.append(color)
        j += 1
    color = input("Enter a color name for the outline: ")
    while (color.lower() in colors) != True:
        print("Invalid Input")
        color = input("Enter a color name for the outline: ")
    listOfColors.append(color)

    # Creating the canvas
    canvas = GraphWin("The Canvas", CANVAS_WIDTH, CANVAS_HEIGHT)
    theRect = [0, 0, CANVAS_WIDTH, CANVAS_HEIGHT]
    makePainting(theRect, canvas, listOfColors)
    canvas.getMouse()
    canvas.close()
main()
