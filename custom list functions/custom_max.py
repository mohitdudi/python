def custom_max(lt):
    out=0
    t=""
    for x in range(len(lt)):
        for y in range(len(lt)):
            if lt[x]>lt[y] or lt[x]==lt[y]:
                out=1
            else:
                out=0;break
        if out==1:
            print(lt[x]);break
        else:
            continue
