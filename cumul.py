#cumulative product
#
#lista = [1,2,3,4]
#suma = 1*2*3*4 + 2*3*4 + 3*4
#

def cumul(lista):
    suma = 0
    while len(lista)>1:
        z = lista[0]
        for i in range(1,len(lista)):
            z *= lista[i]
            #print(i)

        #print('razem: ', z)
        lista = lista[1:]
        #print('lista: ',len(lista))
        suma += z
    return suma
