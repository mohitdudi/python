def custom_insert(lt,i,args):
    elt=[]
    for x in lt:
        if lt[i]==x:
            elt=elt+[args]
        else:
            elt=elt+[x]
            continue
    print(elt)