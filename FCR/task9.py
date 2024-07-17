
def gen(end):
    i=1
    while i<=end:
        res=i
        if i %3==0:
            res='Fizz'
        if i%5==0:
            if type(res)==int:
                res=''
            res+='Buzz'
        yield res
        i+=1
        

print(list(gen(16)))
        
            