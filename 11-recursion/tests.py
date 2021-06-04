#%% recursive function (example 1)

def potencia(b,n):
    """Precondición: n >= 0
       Devuelve: b^n"""
    if n <= 0:
        # caso base
        return 1
    if n % 2 == 0:
        # caso n par
        p = potencia(b, n // 2)
        return p * p
    else:
        # caso n impar
        p = potencia(b, (n - 1) // 2)
        return p * p * b
    
print(potencia(2,3))

#%% iterative function (example 1)

def potencia(b, n):
    """Precondición: n >= 0
       Devuelve: b^n"""
    pila = []
    while n > 0:
        if n % 2 == 0:
            pila.append(True)
            n //= 2
        else:
            pila.append(False)
            n = (n - 1) // 2
    p = 1
    while pila:
        es_par = pila.pop()
        if es_par:
            p *= p
        else:
            p *= p * b

    return p

print(potencia(2,3))

#%% recursive function (example 2)

def sumar(lista):
    """Precondición: len(lista) >= 1
       Devuelve: la suma de los elementos en la lista"""
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + sumar(lista[1:])

print(sumar([1,2,3]))

#%% two functions: promediar isn't recursive (it's a wrapper function); 
# but promediar_aux is. 

def promediar(lista):
    """Devuelve: el promedio de los elementos de una lista de números"""
    def promediar_aux(lista):
        suma = lista[0]
        cantidad = 1    
        if len(lista) > 1:
            suma_resto, cantidad_resto = promediar_aux(lista[1:])
            suma += suma_resto
            cantidad += cantidad_resto
        return suma, cantidad
    suma, cantidad = promediar_aux(lista)
    return suma / cantidad

print(promediar([10,5,5,5]))

#%%

def sumar(a, b):
    """Precondición: b >= 0"""
    print(f"Llamé a sumar con {a} {b}")
    if b == 0: # el final de nuestro resultado (caso base)
        res = a
    else:
        res = sumar(a+1, b-1)
    print(f"El resultado de sumar {a} con {b} es {res}")
    return res

print(sumar(1,2))

""" 
funcion recursiva: 3 etapas
1) un lugar donde termina el resultado (caso base)
2) un lugar donde nos llamamos a nosotros mismos, y la forma en que llamamos
    nos va acercando al lugar donde se termina la función
3) combinacion 
"""

#%%

def factorial(n):
    if n==1:
        res = 1
    else: 
        res = n * factorial(n-1)
    return res

print(factorial(4))
print(4*3*2*1)
    
#%%

def es_impar(n, str_tab=""):
    if n==0:
        print(f"{str_tab} Llegué al cero")
        res = False
    else:
        print(f"{str_tab} Para saber si {n} es impar, niego la paridad de uno menos")
        temp = es_impar(n-1, str_tab + "\t") # se va acercando al caso base
        res = not temp
        print(f"{str_tab} Para saber si {n} era impar obtuve es_impar({n-1})={temp} y lo negué para obtener {res}")
    return res

print(es_impar(3))
# print(es_impar(1000)) # python no se banca 1000 llamados recursivos
    
#%%

def maximo(lista, str_tab=""):
    """Precondición: la lista no es vacía
       Devuelve: el máximo de la lista"""
    print(f"{str_tab} Acabo de entrar con {lista}")
    if len(lista)==1:
        res = lista[0]
        print(f"{str_tab} En el caso base")
    else:
        primero = lista[0]
        max_del_resto = maximo(lista[1:], str_tab + "\t")
        res = max(primero, max_del_resto)
        print(f"{str_tab} Asigno res=max({primero}, maximo({lista[1:]}))=max({primero},{max_del_resto})={res}")
    print(f"{str_tab} Devuelvo: {res}")
    return res
    
print(maximo([2,0,6,4]))    

#%% the most complex exercise  

def permutaciones(lista, str_tab=""):
    """Precondición: TRUE
    Devuelve: una lista con la lista de permutaciones"""
    print(f"{str_tab} Acabo de entrar con {lista}")
    if len(lista)==0:
        res = []
    elif len(lista)==1:
        res = [lista]
    else:
        res = []
        for i, e in enumerate(lista):
            permutaciones_del_resto = permutaciones(lista[:i] + lista[i+1:], str_tab + "\t")
            print(f"{str_tab} Permutaciones parciales: {permutaciones_del_resto}")
            res += [ [e] + p for p in permutaciones_del_resto ]
            print(f"{str_tab} Fin iteración {i} (con {e} de primero): {res}")
    print(f"{str_tab} Devuelvo: {res}")
    return res

print(permutaciones([1,2,3]))