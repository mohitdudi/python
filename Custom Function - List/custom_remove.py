def custom_remove(lt,args):
    elt=[]
    for x in lt:
        if x==args:
            continue
        else:
            elt=elt+[x]
    print(elt)