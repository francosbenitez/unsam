agregar_uno = lambda x: x + 1 
agregar_uno(1)

#%%

agregar_uno = lambda x: str(x)
agregar_uno(169797978)


#%%

numeros = [2, 5, 10, 23, 50, 33]
list(map(lambda x: str(x), numeros))

#%%

def agregar_1(numero):
    return numero + 10

print(agregar_1(1))

#%%

numeros = [2, 5, 10, 23, 50, 33]
lista = []

def convertir_str(valores):
    for n in valores:
        lote = str(n)
        lista.append(lote)
    return lista

test = convertir_str(numeros)

#%%

numeros = [2, 5, 10, 23, 50, 33]
test = [ str(n) for n in numeros ] 

#%%
import pandas as pd

columna = pd.DataFrame({'A': [1, 2], 'B': [10, 20]})

def agregar_1(columna):
    return columna.map(lambda x:x+1)

columna.apply(agregar_1)












