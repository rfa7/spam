'''
fatctorial
n! = n*(n-1) * ... * 1
'''
def factIter(n):
    result = 1
    while n > 0:
        result *= n
        n -= 1

def factRec(n):
    if n ==1:
        return n
    else:
        return n*factRec(n-1)
