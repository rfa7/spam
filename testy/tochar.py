def toChar(s):
    s = s.lower()
    ans =''
    for c in s:
        if c in 'abcdefghijklmnopqrstuvwxyz':
            ans = ans+c
    return ans

