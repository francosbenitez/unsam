def regresiva(n):
    while n > 0:
        yield n
        n -= 1

for x in regresiva(10):
    print(x, end=" ")
    
list(regresiva(10))

#%%

def filematch(filename, substr):
    with open(filename, 'r') as f:
        for line in f:
            if substr in line:
                yield line

for line in open('Data/camion.csv'):
    print(line, end="")
        
for line in filematch('Data/camion.csv', 'Naranja'):
    print(line, end="")
 