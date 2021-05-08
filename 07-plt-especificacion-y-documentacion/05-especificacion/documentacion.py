"""
Ejercicio 7.8: Funciones y documentación
Para cada una de las siguientes funciones:

Pensá cuál es el contrato de la función.
Agregale la documentación adecuada.
Comentá el código si te parece que aporta.
Detectá si hay invariantes de ciclo y comentalo al final de la función
Guardá estos códigos con tus modificaciones en el archivo documentacion.py.

def valor_absoluto(n):
    if n >= 0:
        return n
    else:
        return -n
def suma_pares(l):
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0

    return res
def veces(a, b):
    res = 0
    nb = b
    while nb != 0:
        #print(nb * a + res)
        res += a
        nb -= 1
    return res
def collatz(n):
    res = 1

    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1

    return res
"""

def valor_absoluto(n):
    '''
    Devuelve valor absoluto de n => f(n) = |n|
    Precondicion: valor n real
    Poscondicion: valor n positivo
    '''
    if n >= 0:
        return n
    else:
        return -n

def suma_pares(l):
    '''
    Devuelve la suma de numeros pares de una lista
    Precondicion: valores reales en la lista
    Poscondicion: si el elemento es par, hago la suma res += e
                si el elemento es impar, sumo 0
    '''
    res = 0
    for e in l:
        if e % 2 ==0:
            res += e
        else:
            res += 0
    return res
    # La invariante es que res debe comenzar en 0 para sumar

def veces(a, b):
    '''
    Realizo la multiplicacion entre a y b
    ------------
    Precondicion: valor a real, valor b entero
    Poscondicion: producto entre a y b
    '''
    res = 0
    nb = b
    while nb != 0:
        res += a
        nb -= 1
    return res
    # La invariante es que res debe comenzar en 0 para sumar

def collatz(n):
    '''
    Funcion de conjetura de Collatz
    Precondicion: valor n entero positivo
    Poscondicion: si el n es par, se divide entre 2
                si el n es impar, devuelve 3*n+1
    '''
    res = 1
    while n!=1:
        if n % 2 == 0:
            n = n//2
        else:
            n = 3 * n + 1
        res += 1
    return res
    # La invariante es que res debe empezar en 1 
    # si el usuario coloca un n = 1

