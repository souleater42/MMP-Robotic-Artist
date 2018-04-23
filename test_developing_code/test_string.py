stra = 'PA 500 500;'
print(stra)
# remove ;
lista = list(stra)
print(lista)
print(len(lista))
print(lista[len(lista) - 1])
lista[len(lista) - 1] = ' '
strb = ''.join(lista)
print(strb)
listb = strb.split(' ')
print(listb)
if listb[0] == 'PA':
    print(listb[0])

str(KeyError('bad'))
