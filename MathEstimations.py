import math
from sympy import *
from sympy.parsing.sympy_parser import parse_expr

#Chris Chuck


######### mathmatical necesities #########
def rungeKutta(k1, k2, k3, k4, initialY) :
    return initialY + (1.0/6) * (k1 + 2*k2 + 2*k3 + k4)

def eulerMethod(y, f, h):
    return y + h*(f)

def buildFunction(funct) :
    x = Symbol("x")
    y = Symbol("y")
    e = Symbol("e")
    parsedFunct = sympify(funct.replace("^", "**"))
    return lambda q, t : parsedFunct.subs([(x, q),(y, t), (e, math.e)])


######### main logic in here #########
def main():
    funct = raw_input("What is your function in terms of x and y? ")
    initialY = float(input("What is the initial value for f(x)? "))
    initialX = float(input("What is the initial condition? "))
    xn = float(input("What is the endpoint? "))
    partition = int(input("What is the partition size? "))
    choice = raw_input("r for Runge Kutta or e for Euler? ").lower()
    print("")

    print(choice)
    funct = buildFunction(funct)

    stepSize = (xn - initialX)/partition
    
    if (choice == "r" or choice == "rk" or choice == "runge kutta"):
        for i in range(0, partition + 1) :

            print("x: %f | y: %.16f" % (initialX, initialY))
        
            k1 = stepSize * funct(initialX, initialY)
            k2 = stepSize * funct(initialX + (stepSize/2), initialY + k1/2)
            k3 = stepSize * funct(initialX + (stepSize/2), initialY + k2/2)
            k4 = stepSize * funct(initialX + stepSize, initialY + k3)

            initialY = rungeKutta(k1, k2, k3, k4, initialY)
            initialX += stepSize
            
    elif (choice == "e" or choice == "euler"):
        for i in range(0, partition + 1):
            
            print("x: %f | y: %.16f" % (initialX, initialY))
            f = funct(initialX, initialY)
            initialY = eulerMethod(initialY, f, stepSize)
            initialX += stepSize
    else:
        print("You broke it...")
        

######### start here ###########
startOver = True

while startOver:
    main()
    userInput = raw_input("\nPress 'y' to start over, anything to quit ")
    if userInput is not "y":
        startOver = False

