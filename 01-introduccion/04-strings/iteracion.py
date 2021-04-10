"""
Ejercicio 1.17: Iteración sobre cadenas
Usá el comando for para iterar sobre los caracteres de una cadena.

>>> cadena = "Ejemplo con for"
>>> for c in cadena:
       print('caracter:', c)
Mirá el output.
Modificá el código anterior de manera que dentro del ciclo el programa cuente cuántas letras "o" hay en la cadena.

Sugerencia: usá un contador como con los meses de la hipoteca.
"""

cadena = "Ejemplo con for"
contador = 0

for caracter in cadena:
    if caracter == "o":         
        contador += 1           
        print(contador)