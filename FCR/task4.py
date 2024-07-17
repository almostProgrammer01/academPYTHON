
val =input("Enter your values please: ")
valList = val.split(' ')
valCorr=[]
con1=True
i=0
j=0

if len(valList)<3:
    print("It's not a polygon")
    con1=False

for i in valList:
    try:
        valList[j]=int(i)
    except:
        print(f'Incorrect argument {i}')
        con1=False
    j+=1
    
i=1
con2=False

if con1:
    while i<len(valList):
        if valList[i-1] == valList[i]:
            con2=True
        else:
            con2=False
            break
        i+=1
    if con2==True:
        print('Yes')
    else:
        print('No')
else:
    print('Wrong incoming argument')

