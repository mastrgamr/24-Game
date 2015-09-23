'''
Created on May 19, 2013

@author: Stuart Smith
'''

from random import randrange

def brute_force(x1, x2, x3, x4):
    numList = [x1, x2, x3, x4]
    opList = ["+", "-", "*", "/"]
    parenth = ["(", ")"]
    
    x = "" #string to have the equation built

    for i in range(4):
        for j in range(4):
            for k in range(4):
                for p in range(len(parenth)*3):
                    if p == 0:
                        x +=  parenth[0]
                        x += str(numList[0]) + opList[i] + str(numList[1]) + parenth[1] + opList[j] \
                         + str(numList[2]) + opList[k] + str(numList[3])
                    if p == 1:
                        x += parenth[0]
                        x += str(numList[0]) + opList[i] + str(numList[1]) + opList[j] + str(numList[2]) + parenth[1] \
                         + opList[k] + str(numList[3])
                    if p == 2:
                        x += str(numList[0]) + opList[i] + parenth[0] + str(numList[1]) + opList[j] + str(numList[2]) \
                         + opList[k] + str(numList[3]) + parenth[1]
                    if p == 3:
                        x += str(numList[0]) + opList[i] + str(numList[1]) + opList[j] + parenth[0] + str(numList[2]) \
                         + opList[k] + str(numList[3]) + parenth[1]
                    if p == 4:
                        x += str(numList[0]) + opList[i] + parenth[0] + str(numList[1]) + opList[j] + str(numList[2]) \
                         + parenth[1] + opList[k] + str(numList[3])
                    if p == 5:
                        x +=  parenth[0]
                        x += str(numList[0]) + opList[i] + str(numList[1]) + parenth[1] + opList[j] \
                         + parenth[0] + str(numList[2]) + opList[k] + str(numList[3]) + parenth[1]
                    
                    try:
                        if eval(x) == 24:
                            #print(x, "= 24!") #shows one solution for the equation
                            return True
                        else:
                            x = ""
                    except ZeroDivisionError:
                        x = ""
                        pass
                    
            try: #try for possible non-parenthesis solution
                x += str(numList[0]) + opList[i] + str(numList[1]) + opList[j] \
                    + str(numList[2]) + opList[k] + str(numList[3])
                if eval(x) == 24:
                    #print(x, "= 24!") #shows one solution for the equation
                    return True
                else:
                    x = ""
            except ZeroDivisionError:
                x = ""
                pass     
    
    #print(x1, x2, x3, x4) #DEBUG: To see if numbers don't actually make 24                
    return False

def main():
    x = False
    
    while x is False:
        x1 = randrange(1, 9)
        x2 = randrange(1, 9)
        x3 = randrange(1, 9)
        x4 = randrange(1, 9)
        x = brute_force(x1, x2, x3, x4)
        
    print("Your numbers are: [", x1, x2, x3, x4, "]. Make 24!")
    
    c = input(">> ")
    
    while eval(c) is not 24:
        print("That's not it, try again!")
        c = input(">> ")
    
    print("You found the solution!")
        
main()
