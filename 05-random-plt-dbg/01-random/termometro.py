"""
Ejercicio 5.5: Gaussiana
Con random.random() generamos valores aleatorios entre 0 y 1 con una distribución uniforme. En esa distribución, todos los valores posibles tienen la misma probabilidad de ser seleccionados. También es posible generar valores aleatorios con otras distribuciones. Una de las distribuciones más importantes es la distribución normal o Gaussiana.

La distribución normal tiene dos parámetros, denominados media y desvío estándar y denotados usualmente con las letras griegas mu y sigma, respectivamente.

Distribución normal

La función random.normalvariate(mu,sigma) genera números aleatorios según esta distribución de probabilidades. Por ejemplo, usando mu = 0 y sigma = 1 podemos generar 6 valores aleatorios así:

>>> for i in range(6):
        print(f'{random.normalvariate(0,1):.2f}', end=', ')
-0.60, 0.06, -1.33, -0.62, -0.81, 0.63, 
La distribución normal tiene muchos usos. Uno de ellos es modelar errores experimentales, es decir la diferencia entre el valor medido de una magnitud física y el valor real de dicha magnitud.

Hagamos algún ejercicio sencillo antes de terminar. Supongamos que una persona se compra un termómetro que mide la temperatura con un error aleatorio normal con media 0 y desvío estándar de 0.2 grados (error gaussiano). Si la temperatura real de la persona es de 37.5 grados, simulá usando normalvariate() (con mu y sigma adecuados) n = 99 valores medidos por el termómetro.

Imprimí los valores obtenidos en las mediciones de temperatura simuladas y luego, como resumen, cuatro líneas indicando el valor máximo, el mínimo, el promedio y la mediana de estas n mediciones. Guardá tu programa en el archivo termometro.py.

Para encontrar el máximo y mínimo podés usar y agrandar tu código de busqueda_en_listas.py o usar las primitivas max() y min() de Python. El promedio es la suma de los valores dividido su cantidad; podés programarla desde cero o usar la primitiva sum() y un cociente por n. Finalmente, la mediana de una cantidad impar de valores es el valor en la posición central cuando los datos están ordenados. Acá podés usar el método sort() de listas. Y ya que estamos, ¿se te ocurre cómo encontrar los cuartiles?
"""

import random
from statistics import median
import numpy as np
import matplotlib.pyplot as plt
N = 999

def campana(maxi, mini, veces, total, l_mediana):
    mediciones = []
    for i in range(6):
        medicion = float(random.normalvariate(0,0.2))
        veces += 1
        mediciones.append(round(medicion, 3))
        np.save('Data/Temperaturas.npy', mediciones)
    total += sum(mediciones)
    n_maxi = max(mediciones)
    n_mini = min(mediciones)
    l_mediana.append(median(sorted(mediciones)))
    if n_maxi > maxi:
        maxi = n_maxi
    if n_mini < mini:
        mini = n_mini
    print(f'{mediciones}')
    return maxi, mini, veces, total, l_mediana

def graficar ():
    mediciones = np.load('Data/Temperaturas.npy')
    plt.hist(mediciones, bins=25)
    
if __name__ == '__main__':
    ciclo = True
    while ciclo == True:
        try:
            opc = int(input("""\nElija una opción:
            1) Realizar mediciones.
            2) Graficar mediciones
            3) Salir
            """))
            if opc == 1:
                maxi, mini, veces, total = 0, 0, 0, 0
                l_mediana = []
                for i in range(N):
                    maxi, mini, veces, total, l_mediana = campana(maxi, mini, veces, total, l_mediana)
                print(f'''En {N} veces ejecutadas la Campana con 6 valores resultantes, obtuve:
                Máximo: {maxi}.
                Mínimo: {mini}.
                Promedio: {total/N:.3f}.
                Mediana: {median(sorted(l_mediana)):.3f}.
                ''')
            if opc == 2:
                graficar()
            ciclo = False if (opc == 3) else True
            if (not(opc in [1, 2, 3])):
                print('La opción seleccionada no es válida.')
        except ValueError:
            print('La opción seleccionada no es válida.')
