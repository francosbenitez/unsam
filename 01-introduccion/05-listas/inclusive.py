"""
Ejercicio 1.29: Traductor (r�stico) al lenguaje inclusivo
Queremos hacer un traductor que cambie las palabras masculinas de una frase por su versi�n neutra. Como primera aproximaci�n, complet� el siguiente c�digo para reemplazar todas las letras 'o' que figuren en el �ltimo o ante�ltimo caracter de cada palabra por una 'e'. Por ejemplo 'todos somos programadores' pasar�a a ser 'todes somes programadores'. Guard� tu c�digo en el archivo inclusive.py

>>> frase = 'todos somos programadores'
>>> palabras = frase.split()
>>> for palabra in palabras:
       if ?
       ...
   frase_t = ?
   print(frase_t)
'todes somes programadores'
>>>
Prob� tu c�digo con 'Los hermanos sean unidos porque �sa es la ley primera', '�c�mo transmitir a los otros el infinito Aleph?' y 'Todos, tu tambi�n'. �Qu� falla en esta �ltima? (�no hace falta que lo resuelvas!)
"""

frase = "todos somos programadores"
palabras = frase.split()
i = 0 

for palabra in palabras:
    if palabra[-1] == "o":        
        palabras[i] = palabra[:-1] + "e"
    elif (len(palabra) >= 2) and (palabra[-2] == "o"):
        palabras[i] = palabra[:-2] + "e" + palabra[-1:]
        i = i + 1 
     
frase_t = ' '.join(palabras) 
print(frase_t)
    
    
        
    