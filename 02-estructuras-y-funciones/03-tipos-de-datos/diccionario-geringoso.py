"""
Ejercicio 2.14: Diccionario geringoso.
Construí una función que, a partir de una lista de palabras, devuelva un diccionario geringoso. Las claves del diccionario deben ser las palabras de la lista y los valores deben ser sus traducciones al geringoso (como en el Ejercicio 1.18). Probá tu función para la lista ['banana', 'manzana', 'mandarina']. Guardá este ejercicio en un archivo diccionario_geringoso.py para entregar al final de la clase.
"""

def geringoso(fruta):
    geringoso = ""
    for c in fruta:
        if c in "aeiou":   
            geringoso += c + "p" + c
        else:
            geringoso += c
    return geringoso

def lista_a_diccionario(lista):
    diccionario = {}
    for fruta in lista:
        diccionario[fruta] = geringoso(fruta)
    return diccionario

lista = ['banana', 'manzana', 'mandarina']

diccionario_geringoso = lista_a_diccionario(lista)
print(diccionario_geringoso)

