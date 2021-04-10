"""
En los siguientes ejercicios te proponemos que uses las técnicas que mencionamos arriba para resolver los problemas que aparecen a continuación. Determiná los errores de los siguientes códigos y corregilos en un archivo solucion_de_errores.py comentando brevemente los errores. ¿Qué tipo de errores tiene cada uno?

En el archivo solucion_de_errores.py separá las correcciones de los distintos códigos con una línea que contenga solamente los símbolos #%% seguido de una o varias líneas comentadas indicando el ejercicio y el problema que tenía. Al terminar, debería verse así tu archivo:

    #solucion_de_errores.py
#Ejercicios de errores en el código
#%%
#Ejercicio 3.1. Función tiene_a()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
#    Lo corregí cambiando esto por aquello.
#    A continuación va el código corregido
...
...

#%%
#Ejercicio 3.2. Función tiene_a(), nuevamente
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
...
...

#%%
#Ejercicio 3.3. Función tiene_uno()
#Comentario: El error era de TAL tipo y estaba ubicado en TAL lugar.
...
...
...
"""
#%%
"""
Ejercicio 3.1: Semántica
¿Anda bien en todos los casos de prueba?

def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if expresion[i] == 'a':
            return True
        else:
            return False
        i += 1

tiene_a('UNSAM 2020')
tiene_a('abracadabra')
tiene_a('La novela 1984 de George Orwell')
"""

# El error es que devuelve False cuando las strings sí poseen a.
# Y devuelve False porque agarra sólo las primeras iniciales. 
# Lo corregí cambiando 
# if expresion[i] == 'a':
#            return True
# por:
# if "a" in expresion:
#            return True
#        elif "A" in expresion:
#            return True
# Y agregué un print.
# A continuación, va el código corregido: 
    
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if "a" in expresion:
            print("Detecto 'a'")
            return True
        elif "A" in expresion:
            print("Detecto 'A'")
            return True
        else:
            print("No")
            return False
        i += 1

test_1 = tiene_a('UNSAM 2020')
test_2 = tiene_a('abracadabra')
test_3 = tiene_a('La novela 1984 de George Orwell')
print(test_1, test_2, test_3)

#%%
"""
Ejercicio 3.2: Sintaxis
¿Anda bien en todos los casos de prueba?

def tiene_a(expresion)
    n = len(expresion)
    i = 0
    while i<n
        if expresion[i] = 'a'
            return True
        i += 1
    return Falso

tiene_a('UNSAM 2020')
tiene_a('La novela 1984 de George Orwell')
"""

# El error es que hay código mal tipeado.
# Lo corregí tipeándolo mejor, y agregándole lo que realicé
# en el ejercicio anterior.
# A continuación, va el código corregido: 
    
def tiene_a(expresion):
    n = len(expresion)
    i = 0
    while i < n:
        if "a" in expresion:
            return True
        elif "A" in expresion:
            return True
        else:
            return False
        i += 1

test_1 = tiene_a('UNSAM 2020')
test_2 = tiene_a('La novela 1984 de George Orwell')
print(test_1, test_2)

#%%
"""
Ejercicio 3.3: Tipos
¿Anda bien en todos los casos de prueba?

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

tiene_uno('UNSAM 2020')
tiene_uno('La novela 1984 de George Orwell')
tiene_uno(1984)
"""

# El error es que la función sólo funciona para cadenas.
# Lo corregí agregando las comillas.
# A continuación, va el código corregido: 

def tiene_uno(expresion):
    n = len(expresion)
    i = 0
    tiene = False
    while (i<n) and not tiene:
        if expresion[i] == '1':
            tiene = True
        i += 1
    return tiene

test_1 = tiene_uno('UNSAM 2020')
test_2 = tiene_uno('La novela 1984 de George Orwell')
test_3 = tiene_uno("1984")
print(test_1, test_2, test_3)

#%%
"""
Ejercicio 3.4: Alcances
La siguiente suma no da lo que debería:
    
def suma(a,b):
    c = a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
"""

# El error es que el "c" no hace nada. 
# Lo corregí quitando el "c" y agregando el return.
# A continuación, va el código corregido: 
    
def suma(a,b):
    return a + b

a = 2
b = 3
c = suma(a,b)
print(f"La suma da {a} + {b} = {c}")
    
#%%
"""
Ejercicio 3.5: Pisando memoria
El siguiente ejemplo usa el dataset de la clase anterior, pero no lo imprime como corresponde, ¿podés determinar por qué y explicarlo brevemente en la versión corregida?

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro[encabezado[0]] = fila[0]
            registro[encabezado[1]] = int(fila[1])
            registro[encabezado[2]] = float(fila[2])
            camion.append(registro)
    return camion

camion = leer_camion('../Data/camion.csv')
pprint(camion)

Ayuda: Primero tratá de pensarlo, pero si este último se te hace muy difícil, podés mirar un poco de la teoría relacionada con esto un par de secciones más adelante (Sección 4.4).
"""

# El error es que se imprimen solamente las naranjas por la manera
# en que se empareja los encabezados y los valores de la fila.
# Lo corregí usando la función dict(zip(encabezado, fila)), 
# que sirve, precisamente, para hacer estos procedimientos de 
# emparejamiento.
# A continuación, va el código corregido: 

import csv
from pprint import pprint

def leer_camion(nombre_archivo):
    camion=[]
    registro={}
    with open(nombre_archivo,"rt") as f:
        filas = csv.reader(f)
        encabezado = next(filas)
        for fila in filas:
            registro = dict(zip(encabezado, fila))
            camion.append(registro)
    return camion

camion = leer_camion('Data/camion.csv')
pprint(camion)