"""
Ejercicio 1.18: Geringoso r�stico
Us� una iteraci�n sobre el string cadena para agregar la s�laba 'pa', 'pe', 'pi', 'po', o 'pu' seg�n corresponda luego de cada vocal.

>>> cadena = 'Geringoso'
>>> capadepenapa = ''
>>> for c in cadena:
       ?
>>> capadepenapa
Geperipingoposopo
Pod�s probar tu c�digo cambiando la cadena inicial por otra palabra, como 'apa' o 'boligoma'.

Guard� el c�digo en un archivo geringoso.py.
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

        
        