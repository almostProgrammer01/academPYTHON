
arg1=input('Enter number please: ')
arr=[]

def func(arg,j=0):
        val1=arg%16
        val2=int(arg/16)
        j+=1
        #print(val1)
        if val1==10:
            val1="a"
        elif val1==11:
            arr.append('b')
        elif val1==12:
            arr.append('c')
        elif val1==13:
            arr.append('d')
        elif val1==14:
            arr.append('e')
        elif val1==15:
            arr.append('f')
        else:
            arr.append(val1)
            
        if val2>=16:            
            func(int(val2),j)
        else:
            if val2==10:
                val2="a"
            elif val2==11:
                val2=="b"
            elif val2==12:
                val2=='c'
            elif val2==13:
                val2=='d'
            elif val2==14:
                val2='e'
            elif val2==15:
                val2=='f'
            arr.append(val2)
            return 0
        
con = True
try:
    arg1=int(arg1)
except:
    print('Wrong input')
    con=False

if con:
    if arg1>=0:
        func(arg1) 
        arr.reverse()
        #print (arr)
        i=0
        res=''
        while i<len(arr):
            try:
                str(arr[i])
            except:
                print("Something wrong\(")
                break
            res=res+str(arr[i])
            i+=1
        print(res)
    else:
        print('Wrong input')

        
