
def zirku(arr,item,elem):
    i=0
    while i<item:
        arr.append(elem)
        i+=1
    return arr

val=input("Your value: ")

con=False
try:
    val=int(val)
    con=True
except:
    print('Wrong input')
    
if val%2==0 or val<0:
    print('Wrong input')
    con=False
    
if con:
    res=''
    myArr=[]
    inArr=[]
    a,b=0,0
    myArr=zirku(myArr,val,zirku(inArr,val,'* '))
    inArr=tuple(inArr)
    for i in myArr:
        a=list(inArr)
        a[b],a[-b-1]='  ','  '
        if b==int(val/2):
            a[b]='* '
        i=a
        b+=1
        for j in i:
            res+=j
        res+='\n'
    print (res)
    print(inArr)