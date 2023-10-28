def getMEX(a):
    found = False
    n = len(a)
    for i in range(1, n + 2):
        print(" print i " , i)
        found = False
        for j in range(n):
            print(" print j " , j)
            print(" print aj " ,  a[j])
            if a[j] == i:
                found = True
                break
        if found == False:
            return i

a = [2, 3, -7, 6, 8, 1, -10, 15]
pp = getMEX(a)
print(pp)