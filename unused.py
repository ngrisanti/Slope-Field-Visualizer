# Authors: Nick Grisanti, Eric Corona

def takeDerivative(coeffArray):
  # coeffArray starts with zero-order term, works up
  returnArray = []
  for i in range(len(coeffArray)):
    returnArray.append(i * coeffArray[i])
  return returnArray[1:]

def evaluateAtPointPolynomial(coeffArray, x):
  # coeffArray starts with zero-order term, works up
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
