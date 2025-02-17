def myfunc(n):
    print(abs(n - 50))
    return abs(n - 50)
thislist = [100,20,10,90,50,50,70]
thislist.sort(key = myfunc)
print(thislist)