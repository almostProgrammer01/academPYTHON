
def con(str):
    try:
        a=str[0]
        return True
    except:
        return False
    

def find(substring,string):
    if not con(substring):
        return True
    if not con(string):
        return "Wrong string"
    if substring[0]==string[0]:
        if not con(substring[1:]):
            return True
        if con(string[1:]):
            return find(substring[1:],string[1:])
        else:
            return False
    else:
        if con(string[1:]):
            return find(substring,string[1:])
        else:
            return False
        
mySubstr=input('Enter your substring: ')
myStr=input('Enter your string: ')

print (find(mySubstr,myStr))