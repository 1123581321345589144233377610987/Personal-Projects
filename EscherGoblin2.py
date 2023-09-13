x=0
c=0
instructions = []
Instructions=[]
clump=(3,4,5)

while x!=-42:
    print("Select an option:")
    print("1. Add instruction")
    print("2. Run simulation")
    print("3. Read list of current instructions")
    print("4. Edit an instruction")
    print("5. Delete an instruction")
    x=0
    while x==0:
        try:
            r = int(input())
            options = (1,2,3,4,5)
            right = ("right", "r", "R", "Right", "RIGHT", "Riiiiight", "correct")
            left = ("left", "l", "L", "Left", "LEFT", "sinister")
            if r in options:
                x=1
                if r==1:
                    while x==1:
                        direction = input("Input the direction of your movement (R/L): ")
                        if direction in right:
                            movement=1
                            instructions.append(movement)
                            Instructions.append("Right")
                            x=2
                        elif direction in left:
                            movement=-1
                            instructions.append(movement)
                            Instructions.append("Left")
                            x=2
                elif r in clump:
                    c=1
                    x=1
                    print("\nCurrent list of instructions:")
                    for i in Instructions:
                        print(f"{c}. {i}")
                        c+=1
                    print()
                    if r==4:
                        num = int(input("Enter the number of the instruction you would like to edit: "))
                        while x == 1:
                            direction = input("Input the direction of your movement (R/L): ")
                            if direction in right:
                                movement = 1
                                instructions[num-1] = movement
                                Instructions[num-1]="Right"
                                x = 2
                            elif direction in left:
                                movement = -1
                                instructions[num-1]=movement
                                Instructions[num-1]="Left"
                                x = 2
                    elif r==5:
                        num = int(input("Enter the number of the instruction you would like to delete: "))
                        del instructions[num-1]
                        del Instructions[num-1]
                elif r==2:
                    c=0
                    steps=1
                    position=0
                    C=1
                    Position=[]
                    Position1=[]
                    Position2=[]
                    while C != 0:
                        y=False
                        file=open("position.txt","w")
                        while -12 < position < 12 and y==False:
                            for i in instructions:
                                if -12<position<12 and y == False:
                                    if c%C==0:
                                        file.write(f"{position}\n")
                                        Position.append(position)
                                        position+=i
                                        print(f"{steps}. position: {position}")
                                        steps+=1
                                        if len(Position)%2==0:
                                            Position1=[]
                                            Position2=[]
                                            pcount=0
                                            for each in Position:
                                                pcount+=1
                                                if pcount<=(len(Position)/2):
                                                    Position1.append(each)
                                                else:
                                                    Position2.append(each)
                                            if Position1==Position2:
                                                y=True
                                    c+=1
                        if y==False:
                            print()
                            print("YOU LOST!")
                            print(f"Score: {steps-1} steps")
                            print(f"Level:{C}")
                            C=0
                            x=-42
                        else:
                            c=0
                            steps=1
                            position=0
                            Position=[]
                            Position1 = []
                            Position2 = []
                            NEXT = ("Next","NEXT","next","n","N","Next!")
                            AGAIN = ("AGAIN","Again","again","back","replay","A","a","Again!","REPLAY")
                            next="nope!"
                            print()
                            print(f"YOU WON LEVEL {C}")
                            while next not in NEXT and next not in AGAIN:
                                print(f"ENTER 'NEXT' TO CONTINUE TO LEVEL {C+1} OR ENTER 'AGAIN' TO REPLAY LEVEL {C}:")
                                next=input()
                            if next in NEXT:
                                C+=1
                            else:
                                C=0
                                x=5
        except:
            x=42
