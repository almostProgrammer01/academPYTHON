import re

pattern = '\d{2}\:\d{2}\:*\d*\d*\.*\d*\d*'

k= input("Input: ")

f = re.findall(pattern,k)

def myFunc(str):
    mylist=re.findall('\d{2}',str)
    if len(mylist)>4 or len(mylist)<2:
        return(f'Input of {i} is incorrect')
    j=0
    h=0
    while j<len(mylist):
        try:
            mylist[j]=int(mylist[j])
        except:
            return "Something wrong" 
        j+=1
    if mylist[0]>24:
        return(f'Ours in {i} is wrong')
    if mylist[1]>60:
        return(f'Minutes in {i} is wrong')
    h+=(mylist[0]*3600+mylist[1]*60)
    if len(mylist)>2 :
        if mylist[2]>60:
            return(f'Secondss in {i} is wrong')
        h+=mylist[2]
    if len(mylist)>3: 
        mylist[3]=10/float(mylist[3])      
        h+=mylist[3]
    return(h)
    
con=False
try:
    a=f[0]
    con=True
except:
    print("Wrong input")
    
if con:
    for i in f:
        print(myFunc(i))
        #print(mylist)
    #print(f)
    #print(k)