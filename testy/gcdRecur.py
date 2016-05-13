def gcdRecur(a, b):
    if b==0:
        return a
    print('a= ' + str(a))
    return gcdRecur(b,a%b)
