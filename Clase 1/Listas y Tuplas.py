#Lista y Tumplas y sus diferencias


lista=[4,45.6,"Python",True,3,True]
print(lista[0])
print(lista[-1])
print(lista[-4])
tupla=(4,45.6,"Python",True,3,True)
print(type(lista))
print(type(tupla))
print(tupla[0])
print(tupla[3])
print(tupla[-2])

lista[5]=False
del lista[5]
print (lista)
print(len(lista))

tupla[5]=23
del tupla[5]



