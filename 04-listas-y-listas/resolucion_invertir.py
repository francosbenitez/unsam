def invertir_lista_v1(lista):
    invertida = []
    for e in lista: # recorro la lista
        invertida = [e] + invertida
    return invertida

def invertir_lista_v2(lista):
    invertida = []
    for i in range(len(lista)-1, -1, -1): # recorro la lista
        invertida.append(lista[i])
    return invertida

def invertir_lista_v3(lista):
    invertida = lista[::-1]
    return invertida

def invertir_lista_v4(lista):
    invertida = []
    i = len(lista) -1
    while (i >= 0):
        invertida.append(lista[i])
        i -= 1
    return invertida

lis_1 = [1, 2, 3, 4, 5]
lis_2 = ['Bogotá', 'Rosario', 'Santiago', 'San Fernando', 'San Miguel']
lis_3 = []
lis_4 = [10-x for x in range(10)]