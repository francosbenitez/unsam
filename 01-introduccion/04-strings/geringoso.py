"""
Ejercicio 1.18: Geringoso rústico
Usá una iteración sobre el string cadena para agregar la sílaba 'pa', 'pe', 'pi', 'po', o 'pu' según corresponda luego de cada vocal.

>>> cadena = 'Geringoso'
>>> capadepenapa = ''
>>> for c in cadena:
       ?
>>> capadepenapa
Geperipingoposopo
Podés probar tu código cambiando la cadena inicial por otra palabra, como 'apa' o 'boligoma'.

Guardá el código en un archivo geringoso.py.
"""

cadena = "Geringoso"
capadepenapa = ""

for caracter in cadena: 
    if caracter == "a":  
        capadepenapa += "apa"
         
    elif caracter == "e":
        capadepenapa += "epe"
        
    elif caracter == "i":
        capadepenapa += "ipi"
        
    elif caracter == "o":
        capadepenapa += "opo"
        
    elif caracter == "u":
        capadepenapa += "upu"
    else:
        capadepenapa += caracter
        
print(capadepenapa)

        
        