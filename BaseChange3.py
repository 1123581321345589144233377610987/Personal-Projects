#!/usr/bin/env python3
# py Desktop\Notepad++\SnakeLessons\BaseChange3.py
#dictionaries
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
#functions
def TenConvert(num1, base2):
    num1=list(num1)
    num1=num1[::-1]
    num=0
    Count=0
    while Count != len(num1):
        num1[Count] = Symbols[num1[Count]]
        piece=(int(num1[Count]))*(base2**Count)
        if int(num1[Count])>=base2:
            print("ERROR. Your number cannot be written in the base you claimed it was written in. Digits cannot be equal to or larger than the base a number is written in. For example, base ten uses the digits 0 through 9. There is no 'ten' digit, no 'eleven' digit, etc.") 
            break
        num += piece
        Count+=1
    return(num)
def SecondChance(answer, num):
    answer=(answer[::-1])
    answer=list(answer)
    for i in answer:
        i=int(Symbols[i])
    answer2 = "0"
    place=1
    TryAgain=0
    while num>0:
        digit=(num%(base**place))
        result2= str(digit//(base**(place-1)))
        result2=Symbols2[result2]
        answer2+=result2
        num-= digit*(base**(place-1))
        place+=1
        if num<(base**(place-1)) and num>0:
            TryAgain=1
    answer2=list(answer2)
    answer2=answer2[::-1]
    for i in answer2:
        i=Symbols[i]
        i=int(i)
    count=0
    for i in answer:
        i = answer[count] + answer2[count]
        count+=1
    answer=(answer[::-1])
    del answer[0]
    for i in answer:
        i=Symbols2[i]
    if TryAgain==1:
        SecondChance(answer, num)
def BaseChange(num, base):
    place=1
    answer="0"
    while num>0:
        digit=(num%(base**place))
        result= str(digit//(base**(place-1)))
        num-= int(result)*(base**(place-1))
        result=Symbols2[result]
        answer+= result
        place+=1
        if num<(base**(place)) and num>0:
            SecondChance(answer, num)
    answer=str(answer)
    answer=list(answer)
    answer=(answer[::-1])
    del answer[-1]
    answer= "".join(answer)
    return(answer)
    
#actual program
x="yes"
while x=="yes"or "Yes" or "YES":
    num1 = input("Enter the number you would like to convert:")
    base2=int(input("Enter the base your number is written in:"))
    base = int(input("Enter the base you would like to convert your number to:"))
    num=TenConvert(num1, base2)
    answer=BaseChange(num, base)
    print("answer", answer)
    x=input("Would you like to convert another number? Yes/No:")
    if x=="no" or x=="No" or x=="NO" or x=="n" or x=="N":
        break
    elif x=="yes" or x=="Yes" or x=="YES" or x=="y" or x=="Y":
        continue
    else:
        print("ERROR2")