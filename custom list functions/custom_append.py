# 1st Method
def cuappend(lt,args):
    elt=[]
    for x in lt:
        elt=elt+[x]
    lt=elt+[args]
    print(lt)

# 2nd Method
def custom_append(lt,args):
    lt=lt+[args]
    print(lt)