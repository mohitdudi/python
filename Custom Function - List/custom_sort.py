def custom_sort(lt):
    l=len(lt)
    s=""
    for x in range(0,l):
        for y in range(0,l):
                if lt[x]<lt[y]:
                    s=lt[x]
                    lt[x]=lt[y]
                    lt[y]=s
    return lt