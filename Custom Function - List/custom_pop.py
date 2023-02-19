def custom_pop(lt,i):
    elt=[]
    for x in lt:
        if lt[i]==x:
            continue
        else:
            elt=elt+[x]
    print(elt)