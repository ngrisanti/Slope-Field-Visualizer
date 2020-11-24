#Authors: Nick Grisanti, Eric Corona

import numpy as np
import sympy as sp
import matplotlib.pyplot as plt

x, y = sp.symbols(('x', 'y'))

############################################################
################     BACKEND FUNCTIONS     #################
############################################################

# Sample slope field expressions for testing plotSlopeField
dydx = lambda x, y: x*y - y + 2*x
dydz = lambda z, y: z**3 - y**2 -y*z

# Plots slope field of (dy/dx = expression) over given intervals
def plotSlopeField(expression, xmin, xmax, ymin, ymax):
    xAxis = [range(xmin, xmax + 1)]
    yAxis = [range(ymin, ymax + 1)]
    xScale = abs(xmin) + abs(xmax)
    yScale = abs(ymin) + abs(ymax)

    plt.rcParams["figure.facecolor"] = "yellow"
    plt.rcParams["figure.figsize"] = [(xScale * 8) / yScale ,8]
    graph = plt.subplots()
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            plotLineSeg(expression(x,y), (x, y))
    plt.grid(color = "black")
    plt.show()
    return graph

# Helper function for plotSlopeField
# Plots a line segment of length 0.6667 of given slope at given point on given graph
def plotLineSeg(slope, point):
    length = 0.6667 / 2
    theta = np.arctan(slope)
    x0 = length * np.cos(theta)
    y0 = length * np.sin(theta)
    xCoords = (point[0] - x0, point[0] + x0)
    yCoords = (point[1] - y0, point[1] + y0)
    plt.plot(xCoords, yCoords, color = "blue")

############################################################
###############     INTERFACE FUNCTIONS     ################
############################################################

# Main function for interface
def main():
    while True:
        print("Welcome to Slope Field Visualizer!")
        field = getField()
        xRange = getXRange()
        yRange = getYRange()
        plotSlopeField(field, xRange[0], xRange[1], yRange[0], yRange[1])

# Helper function for main
# Returns two-parameter lambda expression
def getField():
    while True:
        userInput = str(input("Enter a slope field to graph: dy/dx = "))
        try: 
            field = eval("lambda x, y:" + userInput)
            return field
        except (SyntaxError, NameError, TypeError, ZeroDivisionError):
            print("Invalid slope field. Try again.")
            getField()

# Helper function for main
# Returns 2-tuple of user-provided inputs
def getXRange():
    userInput = str(input("Enter an interval for x: (min, max) = "))
    try: 
        xRange = eval(userInput)
        xRange[0]
        xRange[1]
        return xRange
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        print("Invalid x-interval. Try again.")
        getField()
        
# Helper function for main
# Returns 2-tuple of user-provided inputs
def getYRange():
    userInput = str(input("Enter an interval for y: (min, max) = "))
    try: 
        yRange = eval(userInput)
        yRange[0]
        yRange[1]
        return yRange
    except (SyntaxError, NameError, TypeError, ZeroDivisionError):
        print("Invalid y-interval. Try again.")
        getField()

main()