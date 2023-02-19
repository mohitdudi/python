# method 1
def custom_reverse(lt):
    lt=lt[::-1]
    return lt

# method 2
def custom_reverse(lt):
    elt = []
    l = len(lt) - 1
    i = l
    while(l<=i):
        elt = elt + [lt[i]]
        i -= 1
        print(lt[i])
    print(elt)
