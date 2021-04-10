"""
Ejercicio 1.29: Traductor (rústico) al lenguaje inclusivo
Queremos hacer un traductor que cambie las palabras masculinas de una frase por su versión neutra. Como primera aproximación, completá el siguiente código para reemplazar todas las letras 'o' que figuren en el último o anteúltimo caracter de cada palabra por una 'e'. Por ejemplo 'todos somos programadores' pasaría a ser 'todes somes programadores'. Guardá tu código en el archivo inclusive.py

>>> frase = 'todos somos programadores'
>>> palabras = frase.split()
>>> for palabra in palabras:
       if ?
       ...
   frase_t = ?
   print(frase_t)
'todes somes programadores'
>>>
Probá tu código con 'Los hermanos sean unidos porque ésa es la ley primera', '¿cómo transmitir a los otros el infinito Aleph?' y 'Todos, tu también'. ¿Qué falla en esta última? (¡no hace falta que lo resuelvas!)
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
    
    
        
    