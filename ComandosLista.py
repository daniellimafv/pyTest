lista = [1,2,['a','b','c'],'daniel']
print(len(lista))
print(lista)
print(lista[-1])
print(lista[2][1])

lista[3] = 'daniel lima'
print(lista)

lista = [1,2,3,4,5,5,65,6,6,7,7,7,3,4563456,345,63,456,345,63,45,63,45]
i = 0
while i < len(lista):
    print(lista[i], end=' ')
    i += 1

lista = [1,2,['a','b','c'],'daniel']
print(lista[-3])
print(lista[0:3])
