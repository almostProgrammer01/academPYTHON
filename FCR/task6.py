

def dec(func):
    def myf(*e):
        def con(d):
            if d%3 == 0:
                return d
            else:
                print(f"Argument {d} is wrong")
                return False
        print(f"My incoming arguments: {e}")
        e =list(map(con, e))
        c=func(*e)
        print(f'Outcoming arguments: {e}')
        return c
    return myf
        
@dec
def func1(*e):
    return sum(e)

a = func1(8,6,6,9,1,-3,0)
print("Sum of agruments: ",a)