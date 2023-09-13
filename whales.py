#!/usr/bin/env python3
# py Desktop\Notepad++\SnakeLessons\Whales.py
import math
whales = 1
years = 0
j = [0,0,0,0,0]
jtemp=[]
whalevol = .0866
fillvol = 51000*(10**24)
file = open('whales.txt', 'w')
file2 = open('years.txt', 'w')
#while whales < (4.85*(10**10)):
while whales < fillvol/whalevol:
    whales+=j[4]
    j[4]=0
    jtemp=tuple(j)
    count=0
    while count != 5:
        j[(count+1)%5]=jtemp[count]
        count+=1
    years+=1
    j[0] = math.ceil(whales/2)
    print("\n",j)
    print(f"Adult Whales: {whales:,}")
    print(f"Years: {years*2}")
    file.write(f"{whales}\n")
    file2.write(f"{years*2}\n")
file.close()
file2.close()
print("\nGiven:")
print(f"Whale Volume: {whalevol} cubic kilometers")
print(f"Volume of Atmosphere: {fillvol:E} cubic kilometers")