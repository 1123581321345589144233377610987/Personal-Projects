alphabet=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
lower=("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")
upper=("A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z")
print("Enter text:")
#eqtt apwe gwc bw gwc vmfb xizb

ciphertext=list(input())
c=0
plaintexts=[]
while c<26:
    pt=[]
    for i in ciphertext:
        if i in lower:
            shift=(lower.index(i)+c)%26
            i=lower[shift]
        elif i in upper:
            i = upper[(upper.index(i)+c)%26]
        pt.append(i)
    pt="".join(pt)
    plaintexts.append(pt)
    c+=1
file = open("words.txt","r")
Words=file.readlines()
words=[]
for i in Words:
    words.append(i.strip("\n"))
file.close()
Scores=[]
pairs=("th","in", "er","es","ng","ti","re","te","ed","on","at","st","an","en","le","ri","ra","al","li","ar","is","qu","sh","ch","ck")
musketeers=("and","ing","ion","ent","est","one","thi","for","thr","tio","ine","ght","our","sto","ive","two","een","eve","ort","ati","tee","top","wen","fou","ort")
vowels=("a","e","i","o","u","y")
for j in plaintexts:
    j=j.split(" ")
    score=0
    for i in j:
        i=i.strip(",")
        i=i.strip(".")
        i=i.strip("!")
        i=i.strip("?")
        i=i.strip("#")
        i=i.strip("$")
        i=i.strip("'s")
        i=i.lower()
        if i in words:
            score+=20
        else:
            i=list(i)
            c=0
            v=0
            p=0
            for k in i:
                if k in vowels:
                    v+=1
                elif k==".":
                    p+=1
                elif k=="q":
                    try:
                        if i[c+1] != "u" and i[c+1]!=".":
                            score-=10
                    except:
                        score+=0
                try:
                    chunk=k+i[c+1]
                except:
                    chunk=k
                if chunk in pairs:
                    score+=1
                try:
                    chunk=k+i[c+1]+i[c+2]
                except:
                    chunk=k
                if chunk in musketeers:
                    score+=2
                c+=1
            if v==0 and p==0:
                score-=8
    Scores.append(score)
data=[]
c=0
for i in plaintexts:
    Data=[]
    Data.append(i)
    Data.append(Scores[c])
    data.append(Data)
    c+=1
Scores.sort(reverse=True)
for i in Scores:
    for j in data:
        if j[1]==i:
            print(j[0])
            data.remove(j)
