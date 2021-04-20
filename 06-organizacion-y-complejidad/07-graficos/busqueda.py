"""
Ejercicio 6.20: Búsqueda binaria vs. búsqueda secuencial
En este Ejercicio vamos a rehacer los gráficos del ejemplo anterior, pero primero cambiando el algoritmo de búsqueda y luego comparando ambos algoritmos.

Usando experimento_secuencial_promedio(lista, m, k) como base, escribí una función experimento_binario_promedio(lista, m, k) que cuente la cantidad de comparaciones que realiza en promedio (entre k experimentos elementales) la búsqueda binaria sobre la lista pasada como parámetro.
Graficá los resultados de estos experimentos para listas de largo entre 1 y 256.
Graficá ambas curvas en una misma figura, nombrando adecuadamente las curvas, los ejes y la figura completa. Jugá con xlim e ylim para visualizar bien las dos curvas, aunque tengas que restringir el rango.
¿Qué observas en estos gráficos? ¿Qué podés decir sobre la complejidad de cada algoritmo? ¿Son similares?
El código de este ejercicio guardalo en plot_bbin_vs_bsec.py.
"""

import random
import matplotlib.pyplot as plt
import numpy as np

def generar_lista(n, m):
    l = random.sample(range(m), k = n)
    l.sort()
    return l

def generar_elemento(m):
    return random.randint(0, m-1)


def busqueda_secuencial(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1.
    '''
    pos = -1
    for i,z in enumerate(lista):
        if z == x:
            pos = i
            break
    return pos

def busqueda_secuencial_(lista, x):
    '''Si x está en la lista devuelve el índice de su primera aparición, 
    de lo contrario devuelve -1. Además devuelve la cantidad de comparaciones
    que hace la función.
    '''
    comps = 0 
    pos = -1
    for i,z in enumerate(lista):
        comps += 1 
        if z == x:
            pos = i
            break
    return pos, comps

def experimento_secuencial_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_secuencial_(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom

def busqueda_binaria(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 
    izq = 0
    der = len(lista) - 1
    while izq <= der:
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio    
        if lista[medio] > x:
            der = medio - 1 
        else:               
            izq = medio + 1 
    return pos

def busqueda_binaria_(lista, x, verbose = False):
    '''Búsqueda binaria
    Precondición: la lista está ordenada
    Devuelve -1 si x no está en lista;
    Devuelve p tal que lista[p] == x, si x está en lista
    '''
    if verbose:
        print(f'[DEBUG] izq |der |medio')
    pos = -1 
    izq = 0
    der = len(lista) - 1
    comps_tot = 0
    while izq <= der:
        comps_tot += 1
        medio = (izq + der) // 2
        if verbose:
            print(f'[DEBUG] {izq:3d} |{der:>3d} |{medio:3d}')
        if lista[medio] == x:
            pos = medio     
        if lista[medio] > x:
            der = medio - 1 
        else:               
            izq = medio + 1 
    return pos, comps_tot

def experimento_binario_promedio(lista, m, k):
    comps_tot = 0
    for i in range(k):
        x = generar_elemento(m)
        comps_tot += busqueda_binaria_(lista,x)[1]
    comps_prom = comps_tot / k
    return comps_prom

m = 10000
n = 100
k = 1000
lista = generar_lista(n, m)

m = 10000
k = 1000

largos = np.arange(256) + 1 
comps_promedio_sec = np.zeros(256) 
comps_promedio_bin = np.zeros(256)

for i, n in enumerate(largos):
    lista = generar_lista(n, m) 
    comps_promedio_sec[i] = experimento_secuencial_promedio(lista, m, k)
    comps_promedio_bin[i] = experimento_binario_promedio(lista, m, k)

plt.plot(largos,comps_promedio_sec,label = 'Búsqueda Secuencial')
plt.plot(largos,comps_promedio_bin,label = 'Búsqueda Binaria')
plt.xlabel("Largo de la lista")
plt.ylabel("Cantidad de comparaciones")
plt.title("Complejidad de la Búsqueda")
plt.legend()
plt.xscale("log")
plt.yscale("log")
plt.show()
