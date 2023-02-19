def custom_count(lt,args):
    c=0
    for x in lt:
        if x==args:
            c+=1
        else:
            continue
    print(c)