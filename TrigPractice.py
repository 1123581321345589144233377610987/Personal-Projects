#!/usr/bin/env python3
# py Desktop\Notepad++\SnakeLessons\TrigPractice.py

import random 

#dictionaries
TrigFunctions = {
    1:"sin",
    2:"cos",
    3:"tan",
    4:"sin",
    5:"cos",
    6:"tan",
}
Degrees = {
    1:"0",
    2:"30",
    3:"45",
    4:"60",
    5:"90",
    6:"120",
    7:"135",
    8:"150",
    9:"180",
    10:"210",
    11:"225",
    12:"240",
    13:"270",
    14:"300",
    15:"315",
    16:"330",
    17:"360",
}
Radians = {
    1:"0",
    2:"pi/6",
    3:"pi/4",
    4:"pi/3",
    5:"pi/2",
    6:"2pi/3",
    7:"3pi/4",
    8:"5pi/6",
    9:"pi",
    10:"7pi/6",
    11:"5pi/4",
    12:"4pi/3",
    13:"3pi/2",
    14:"5pi/3",
    15:"7pi/4",
    16:"11pi/6",
    17:"2pi",
}
SinDeg = {
    "0":"0",
    "30":"1/2",
    "45":"sqr2/2",
    "60":"sqr3/2",
    "90":"1",
    "120":"sqr3/2",
    "135":"sqr2/2",
    "150":"1/2",
    "180":"0",
    "210":"-1/2",
    "225":"-sqr2/2",
    "240":"-sqr3/2",
    "270":"-1",
    "300":"-sqr3/2",
    "315":"-sqr2/2",
    "330":"-1/2",
    "360":"0",
}
CosDeg = {
    "0":"1",
    "30":"sqr3/2",
    "45":"sqr2/2",
    "60":"1/2",
    "90":"0",
    "120":"-1/2",
    "135":"-sqr2/2",
    "150":"-sqr3/2",
    "180":"-1",
    "210":"-sqr3/2",
    "225":"-sqr2/2",
    "240":"-1/2",
    "270":"0",
    "300":"1/2",
    "315":"sqr2/2",
    "330":"sqr3/2",
    "360":"1",
}
TanDeg = {
    "0":"0",
    "30":"sqr3/3",
    "45":"1",
    "60":"sqr3",
    "90":"undefined",
    "120":"-sqr3",
    "135":"-1",
    "150":"-sqr3/3",
    "180":"0",
    "210":"sqr3/3",
    "225":"1",
    "240":"sqr3",
    "270":"undefined",
    "300":"-sqr3",
    "315":"-1",
    "330":"-sqr3/3",
    "360":"0",
}
SinRad = {
    "0":"0",
    "pi/6":"1/2",
    "pi/4":"sqr2/2",
    "pi/3":"sqr3/2",
    "pi/2":"1",
    "2pi/3":"sqr3/2",
    "3pi/4":"sqr2/2",
    "5pi/6":"1/2",
    "pi":"0",
    "7pi/6":"-1/2",
    "5pi/4":"-sqr2/2",
    "4pi/3":"-sqr3/2",
    "3pi/2":"-1",
    "5pi/3":"-sqr3/2",
    "7pi/4":"-sqr2/2",
    "11pi/6":"-1/2",
    "2pi":"0",
}
CosRad = {
    "0":"1",
    "pi/6":"sqr3/2",
    "pi/4":"sqr2/2",
    "pi/3":"1/2",
    "pi/2":"0",
    "2pi/3":"-1/2",
    "3pi/4":"-sqr2/2",
    "5pi/6":"1/2",
    "pi":"0",
    "7pi/6":"-1/2",
    "5pi/4":"-sqr2/2",
    "4pi/3":"-sqr3/2",
    "3pi/2":"0",
    "5pi/3":"1/2",
    "7pi/4":"sqr2/2",
    "11pi/6":"sqr3/2",
    "2pi":"1",
}
TanRad = {
    "0":"0",
    "pi/6":"sqr3/3",
    "pi/4":"1",
    "pi/3":"sqr3",
    "pi/2":"undefined",
    "2pi/3":"-sqr3",
    "3pi/4":"-1",
    "5pi/6":"-sqr3/3",
    "pi":"0",
    "7pi/6":"sqr3/3",
    "5pi/4":"1",
    "4pi/3":"sqr3",
    "3pi/2":"undefined",
    "5pi/3":"-sqr3",
    "7pi/4":"-1",
    "11pi/6":"-sqr3/3",
    "2pi":"0",
}

#functions
def MENU():
    print("")
    print("Welcome to TrigPractice! At any time you may access this menu by entering 'menu', view your stats by entering 'stats', or exit by entering 'exit'.")
    print("Please select a practice mode by entering the corresponding number:")
    print("1. Trig values of angles in degrees")
    print("2. Trig values of angles in radians")
    print("3. Mixed")
def DEGREES():
    return Degrees[random.randrange(1,18)]
def RADIANS ():
    return Radians[random.randrange(1,18)]
def MIXED (coinflip):
    if coinflip == 1:
        return DEGREES()
    else:
        return RADIANS()
def ANSWER (mode, coinflip, tf, q):
    if mode == "1":
        if tf == 1:
            return SinDeg[q]
        elif tf == 2:
            return CosDeg[q]
        elif tf == 3:
            return TanDeg[q]
        else:
            print("ANSWER ERROR mode1")
    elif mode == "2":
        if tf == 4:
            return SinRad[q]
        elif tf == 5:
            return CosRad[q]
        elif tf == 6:
            return TanRad[q]
        else:
            print("ANSWER ERROR mode2")
            print ("tf=", tf)
    elif mode=="3":
        if coinflip == 1:
            if tf == 1:
                return SinDeg[q]
            elif tf == 2:
                return CosDeg[q]
            elif tf == 3:
                return TanDeg[q]
            else:
                print("ANSWER ERROR mode3 c1")
        elif coinflip == 2:
            if tf == 4:
                return SinRad[q]
            elif tf == 5:
                return CosRad[q]
            elif tf == 6:
                return TanRad[q]
            else:
                print("ANSWER ERROR mode3 c2")
        else:
            print("ANSWER coinflip ERROR")
    else:
        print("ANSWER mode ERROR")

#actual program
MENU()
mode = input("")
total = 1
correct = 0
streak = 0
x = "starting value"

while x != "exit":
    coinflip = random.randrange(1,3)
    if mode == "1":
        q = DEGREES()
        tf = random.randrange(1,4)
    elif mode == "2":
        q = RADIANS()
        tf = random.randrange(4,7)
    elif mode == "3":
        q = MIXED(coinflip)
        if coinflip == 1:
            tf = random.randrange(1,4)
        elif coinflip ==2:
            tf = random.randrange(4,7)
        else:
            print("CODE coinflip ERROR")
    else:
            print ("CODE mode ERROR")
        
    print("")
    print(TrigFunctions[tf], "of", q, ":")
    x = input("")
    if x == ANSWER (mode, coinflip, tf, q):
        print("Correct!")
        correct += 1
        total += 1
        streak += 1
    elif x=="stats":
        print("")
        print("Total:", total-1)
        print("Correct:", correct)
        if total==1:
            print("Percent Correct:", (correct/total)*100,"%")
        else:
            print("Percent Correct:", (correct/(total-1))*100,"%")
        print("Streak:",streak)
    elif x=="exit":
        break
    elif x=="menu":
        MENU()
        mode=input("")
    else:
        print("Incorrect!")
        print("The answer was:", ANSWER (mode, coinflip, tf, q))
        total += 1
        streak = 0