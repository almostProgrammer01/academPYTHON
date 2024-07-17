voc = {
    1:5,
    'b':6,
    'c':'d'
    }
    
def incl(el,dictin):
    con=False
    try:
        temp=dictin[el]
        con=True
    except:
        for i in dictin:
            dictin[i]=str(dictin[i])
            if dictin[i]==el:
                con=True
                return con              
        # if key is int:
        try:
            el=int(el)
            tmp2=dictin[el]
            con=True
        except:
            pass
    return con    

elem = input("Enter your element or key please: ")
print(incl(elem,voc))


