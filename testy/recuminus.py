def recmin(razem):
    if razem == 1:
        return razem
    razem -= 1
#    print("po odjeciu 1 : " + str(razem))
    return 1 + recmin(razem)
