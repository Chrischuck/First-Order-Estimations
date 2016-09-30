import math
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

#Chris Chuck

def rungeKutta(k1, k2, k3, k4, initialY) :
    return initialY + (1.0/6) * (k1 + 2*k2 + 2*k3 + k4)

def buildFunction(funct) :
    x = Symbol("x")
    y = Symbol("y")
    e = Symbol("e")
    parsedFunct = sympify(funct.replace("^", "**"))
    return lambda q, t : parsedFunct.subs([(x, q),(y, t), (e, math.e)])

def main():
    funct = raw_input("What is your function in terms of x and y? ")
    initialY = float(input("What is the initial value for f(x)? "))
    initialX = float(input("What is the initial condition? "))
    xn = float(input("What is the endpoint? "))
    partition = int(input("What is the partition size? "))
    print("")

    xDot = buildFunction(funct)

    stepSize = (xn - initialX)/partition

    for i in range(0, partition + 1) :

        print("x: %f | y: %.16f" % (initialX, initialY))
    
        k1 = stepSize * xDot(initialX, initialY)
        k2 = stepSize * xDot(initialX + (stepSize/2), initialY + k1/2)
        k3 = stepSize * xDot(initialX + (stepSize/2), initialY + k2/2)
        k4 = stepSize * xDot(initialX + stepSize, initialY + k3)

        initialY = rungeKutta(k1, k2, k3, k4, initialY)
        initialX += stepSize

startOver = True

while startOver:
    main()
    userInput = raw_input("\nPress 'y' to start over, anything to quit ")
    if userInput is not "y":
        startOver = False

