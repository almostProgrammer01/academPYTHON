a=input('Enter a string please: ')
b=input('Enter a number please: ')


def func(arg1,arg2):
    if not isinstance(arg1,str):
        return 'The first argument is wrong'
    if not isinstance(arg2,int):
        return 'The second argument is wrong'
    i=0
    c=''
    while i<arg2:
        c=c+arg1
        i=i+1
    return c
try:
    b=int(b)
    res=func(a,b)
    print (res)
except:
    print('Wrong input')