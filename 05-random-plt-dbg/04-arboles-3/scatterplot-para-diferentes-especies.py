"""
Ejercicio 5.26: Scatterplot para diferentes especies
Ahora vamos a usar la función medidas_de_especies() definida en el Ejercicio 4.21.

Comenzando con éste código, hacé tres gráficos como en el ejercicio anterior, uno por cada especie.

import os
import matplotlib.pyplot as plt

os.path.join('..', 'Data', 'arbolado-en-espacios-verdes.csv')
arboleda = leer_arboles(nombre_archivo)
especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)
¿Se mantienen las relaciones que viste en el ejercicio anterior para las tres especies? ¿Hay diferencias entre las especies? Para un mismo alto, ¿cuál tiene mayor diámetro (tipicamente)?

Para poder comparar diferentes especies resulta conveniente fijar los límites en los ejes x e y en las diferentes figuras usando las funciones xlim() e ylim(). A continuación un ejemplo:

plt.xlim(0,30) 
plt.ylim(0,100) 
Acordate siempre de ponerle título a las figuras y nombres y unidades a los ejes. Guardá los últimos tres ejercicios dentro de tres funciones diferentes en tu archivo arboles.py. Te pediremos que lo entregues en la próxima página.

Extra: ¿podés hacer un solo gráfico que muestre dos de estas tres especies en diferentes colores y resulte claro? ¿Y las tres especies?
"""

import csv
import matplotlib.pyplot as plt
import numpy as np

def leer_arboles(nombre_archivo):
    arboles = list()
    f = open(nombre_archivo, encoding="utf8")
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        lote = dict(zip(headers, row))
        arboles.append(lote)
    return arboles

arboleda = leer_arboles("Data/arbolado.csv")

def medidas_de_especies(especies, arboleda):
    diccionario = {}
    for especie in especies:
        diccionario[especie] = [(float(arbol["altura_tot"]), 
                             float(arbol["diametro"])) for arbol in arboleda if arbol["nombre_com"] == especie]
    return diccionario

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)

def medidas_euc():
    alt_diam_euc = medidas["Eucalipto"]
    altura_euc = np.array(alt_diam_euc)[:,0] 
    diametro_euc = np.array(alt_diam_euc)[:,1]
    plt.scatter(diametro_euc, altura_euc, alpha = 0.3)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Eucalipto")
    plt.figure()
    plt.xlim(0,230) 
    plt.ylim(0,60) 

def medidas_palo():
    alt_diam_palo = medidas["Palo borracho rosado"]
    altura_palo = np.array(alt_diam_palo)[:,0] 
    diametro_palo = np.array(alt_diam_palo)[:,1]
    plt.scatter(diametro_palo, altura_palo, alpha = 0.3)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Palo borracho rosado")
    plt.figure()
    plt.xlim(0,230) 
    plt.ylim(0,60) 

def medidas_jac():
    alt_diam_jac = medidas["Jacarandá"]
    altura_jac = np.array(alt_diam_jac)[:,0] 
    diametro_jac = np.array(alt_diam_jac)[:,1]
    plt.scatter(diametro_jac, altura_jac, alpha = 0.3)
    plt.xlabel("diametro (cm)")
    plt.ylabel("alto (m)")
    plt.title("Relación diámetro-alto para Jacarandá")
    plt.xlim(0,230) 
    plt.ylim(0,60) 
    
plot_palo = medidas_palo()
plot_euc = medidas_euc()
plot_jac = medidas_jac()