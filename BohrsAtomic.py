#!/usr/bin/env python3
# py Desktop\Notepad++\SnakeLessons\BohrsAtomic.py
Symbols = {
    "0":0,
    "1":1,
    "2":2,
    "3":3,
    "4":4,
    "5":5,
    "6":6,
    "7":7,
    "8":8,
    "9":9,
    "A":10,
    "B":11,
    "C":12,
    "D":13,
    "E":14,
    "F":15,
    "G":16,
    "H":17,
    "I":18,
    "J":19,
    "K":20,
    "L":21,
    "M":22,
    "N":23,
    "O":24,
    "P":25,
    "Q":26,
    "R":27,
    "S":28,
    "T":29,
    "U":30,
    "V":31,
    "W":32,
    "X":33,
    "Y":34,
    "Z":35
}
Symbols2 = {
    "0":"0",
    "1":"1",
    "2":"2",
    "3":"3",
    "4":"4",
    "5":"5",
    "6":"6",
    "7":"7",
    "8":"8",
    "9":"9",
    "10":"A",
    "11":"B",
    "12":"C",
    "13":"D",
    "14":"E",
    "15":"F",
    "16":"G",
    "17":"H",
    "18":"I",
    "19":"J",
    "20":"K",
    "21":"L",
    "22":"M",
    "23":"N",
    "24":"O",
    "25":"P",
    "26":"Q",
    "27":"R",
    "28":"S",
    "29":"T",
    "30":"U",
    "31":"V",
    "32":"W",
    "33":"X",
    "34":"Y",
    "35":"Z",
}
def SecondChance(a, se):
    a=(a[::-1])
    a=list(a)
    for i in a:
        i=int(Symbols[i])
    answer2 = "0"
    place=1
    TryAgain=0
    while se>0:
        digit=(se%(base**place))
        result2= str(digit//(base**(place-1)))
        result2=Symbols2[result2]
        answer2+=result2
        se-= digit*(base**(place-1))
        place+=1
        if se<(base**(place-1)) and se>0:
            TryAgain=1
    answer2=list(answer2)
    answer2=answer2[::-1]
    for i in answer2:
        i=Symbols[i]
        i=int(i)
    count=0
    for i in a:
        i = a[count] + answer2[count]
        count+=1
    a=(a[::-1])
    del a[0]
    for i in a:
        i=Symbols2[i]
    if TryAgain==1:
        SecondChance(a, se)
        
def BaseChange(se, base):
    place=1
    a="0"
    while se>0:
        digit=(se%(base**place))
        result= str(digit//(base**(place-1)))
        se-= int(result)*(base**(place-1))
        result=Symbols2[result]
        a+= result
        place+=1
        if se<(base**(place)) and se>0:
            SecondChance(a, se)
    a=str(a)
    a=list(a)
    a=(a[::-1])
    del a[-1]
    a= "".join(a)
    return(a)
    
num = int(input("Enter the integer (in base 10) that you would like to convert: "))
base = 16
a = "0"
if num == 1:
    answer = "01"
elif num == 2:
    answer = "02"
else:
    num -= 2
    if num>8:
        ve = num%8
        se = int((num - ve)/8)
        se = BaseChange(se, base)
    else:
        ve = num
        se = 0
    ve = str(ve)
    se = str(se)
    answer = ve+se
print(answer)