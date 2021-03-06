"""
Ejercicio 3.17: Tablas de multiplicar
Escribí un programa tablamult.py que imprima de forma prolija las tablas de multiplicar del 1 al 9 usando f-strings. Si podés, evitá usar la multiplicación, usando sólo sumas alcanza.

       0   1   2   3   4   5   6   7   8   9
---------------------------------------------
 0:    0   0   0   0   0   0   0   0   0   0
 1:    0   1   2   3   4   5   6   7   8   9
 2:    0   2   4   6   8  10  12  14  16  18
 3:    0   3   6   9  12  15  18  21  24  27
 4:    0   4   8  12  16  20  24  28  32  36
 5:    0   5  10  15  20  25  30  35  40  45
 6:    0   6  12  18  24  30  36  42  48  54
 7:    0   7  14  21  28  35  42  49  56  63
 8:    0   8  16  24  32  40  48  56  64  72
 9:    0   9  18  27  36  45  54  63  72  81
"""

print("    0   1   2   3   4   5   6   7   8   9", end = "\t")
print('\n------------------------------------------')
for i in range(0, 10):
    print(i, end=':  ')
    for j in range(0, 10):
        print(i * j, end="\t")
    print("")