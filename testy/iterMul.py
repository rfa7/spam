def iterMul(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result
def iterPower(base,exp):
    if exp == 0:
        return 1
    elif exp == 1:
        return base
    else:
        res = base
        for i in range(exp-1):
            res *= base
        return res    

