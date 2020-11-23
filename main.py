import math
import numpy as np
import matplotlib.pyplot as plt

# Expressions for testing plotSlopeField
dydx = lambda x, y: x*y - y + 2*x
dydz = lambda z, y: z**3 - y**2 -y*z

# Plots slope field of (dy/dx = expression) over given intervals
def plotSlopeField(expression, xmin, xmax, ymin, ymax):
    xAxis = [range(xmin, xmax + 1)]
    yAxis = [range(ymin, ymax + 1)]
    graph = plt.subplots()
    for x in range(xmin, xmax + 1):
        for y in range(ymin, ymax + 1):
            plotLineSeg(expression(x,y), (x, y))
    plt.grid()
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

plotSlopeField(dydz, -3, 3, -5, 5)
plotSlopeField(dydx, -3, 3, -5, 5)