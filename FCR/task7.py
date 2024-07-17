
def generator(start,end):
    while start<end:
        if start%2==0 or start%7==0:
            start+=1
            continue
        yield start
        start+=1
        
print("Below is definite numbers from 0 to 10 in list form")

    
print(list(generator(0,10)))