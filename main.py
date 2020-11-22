# Authors: Nick Grisanti, Eric Corona

#%%
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
plt.switch_backend('agg')

#Goal: given ODE, plot slope field
#calculate dy/dx for all (x, y) in given range
#plot all slopes on graph

yourmom = 69

x= sp.Symbol('x')
x= sp.Symbol('y')

dydx = lambda x, y: x*y - y + 2*x

def takeDerivative(coeffArray):
  "coeffArray starts with zero-order term, works up"
  returnArray = []
  for i in range(len(coeffArray)):
    returnArray.append(i * coeffArray[i])
  return returnArray[1:]

def evaluateAtPointPolynomial(coeffArray, x):
  "coeffArray starts with zero-order term, works up"
  sum = 0
  for i in range(len(coeffArray)):
    sum += coeffArray[i]*(x**i)
  return sum

def derivativeMatrix(expression, xmin, xmax, ymin, ymax):
  M = []
  for x in range(xmin, xmax):
    xArray = []
    for y in range(ymin, ymax):
      xArray.append(expression(x, y))
    M.append(xArray)
  return M

def plotSlopeField(expression, xmin, xmax, ymin, ymax):
  #make axes
  xAxis = [0, 1, 2, 3]
  yAxis = [0, 1, 2, 3]
  # for x in range(xmin, xmax):
  #   xAxis.append(x)
  # for y in range(ymin, ymax):
  #   xAxis.append(y)

  plt.plot(xAxis, yAxis)
  # plt.show()

  for x in range(xmin, xmax):
    for y in range(ymin, ymax):
      #plot a line of slope y/x, passing through point (x, y)
      #each line has length 0.66667
      pass

xAxis = [0, 1, 2, 3]
yAxis = [0, 1, 2, 3]
# for x in range(xmin, xmax):
#   xAxis.append(x)
# for y in range(ymin, ymax):
#   xAxis.append(y)

plt.plot(xAxis, yAxis)
plt.show()

# %%
