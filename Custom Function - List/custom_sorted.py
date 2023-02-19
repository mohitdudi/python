def custom_sorted(lt):
    import copy
    t=copy.deepcopy(lt)
    l=len(t)
    s=""
    for x in range(0,l):
        for y in range(0,l):
                if t[x]<t[y]:
                    s=t[x]
                    t[x]=t[y]
                    t[y]=s
    return t