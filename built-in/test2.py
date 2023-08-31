lst1 = [x*x for x in range(5)]
print(lst1)
def fun(lst):
    del lst[lst[2]]
    return lst
print(fun(lst1))
