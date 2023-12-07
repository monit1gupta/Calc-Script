#Simple Calculator Script in Python
#Take n variables from user, ask for operation, and do the operation and return the result
import sys
print("Hello, welcome to the calculator")

print("Hello, please enter your variables that you would like to perform an operation on!")

#Take input into a list
varForOps = []
count= 0
while count < 2:
    print("Enter a number:")
    varEntered = input()
    varForOps.append(int(varEntered))
    count += 1

print(varForOps)


#Ask for operation to be performed
while True:
    print("Please entered the operation you would like to perform today:")
    opInput = input()
    if opInput in ['+', '-', '*', '/']:
        break
    print("That's not a valid operation, choose one from +, -, *, /")

#Functions
def addVars(varList):
    print (varList[0]+varList[1])

def subVars(varList):
    print (varList[0]-varList[1])

def mulVars(varList):
    print(varList[0]*varList[1]) 

def divVars(varList):
    print(varList[0]/varList[1]) 


##driver
if varForOps[1] == 0 and opInput == '/':
     print("Can't divide by zero!")
     sys.exit()
print("Thanks, here is your result:")

if opInput == '+':
    #perform addition
    addVars(varForOps)
elif opInput == '-':
    subVars(varForOps)
    #perform subtraciton
elif opInput == '*':
    mulVars(varForOps)
    #perform multiplication
else:
    divVars(varForOps)
    #perform division
