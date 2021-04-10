def propagar_v1(lis):
    for i, f in enumerate(lis):
        if i - 1 >= 0:
            # si esta nuevo y tiene un fosforo prendido al lado
            if f==0 and lis[i-1]==1: 
                # prendo fuego el fosforo actual
                lis[i] = 1
    return lis

def propagar_v2(lis):
    for i, f in enumerate(lis):
        # corre de izquierda a derecha 
        if i - 1 >= 0:
            if f==0 and lis[i-1]==1:
                lis[i] = 1
        # corre de derecha a izquierda
        if i + 1 < len(lis): 
            if f==0 and lis[i+1]==1:
                lis[i] = 1
    return lis

def propagar_v3(lis):
    hice_cambio = True
    while hice_cambio:
        hice_cambio = False
        for i, f in enumerate(lis):
            if i - 1 >= 0:
                if f==0 and lis[i-1]==1:
                    lis[i] = 1
                    hice_cambio = True
            if i + 1 < len(lis):
                if f==0 and lis[i+1]==1:
                    lis[i] = 1
                    hice_cambio = True
    return lis

def propagar_v4(lis):
    # recorro de un lado a otro, el fuego se arrastra hacia un lado
    for i in range(len(lis)):
        if i - 1 >= 0:
            if lis[i]==0 and lis[i-1]==1:
                lis[i] = 1
    # viceversa
    # recorrer desde la longitud de la lista-1, 
    # hasta la posicion de la lista
    # y yendo para atras
    for i in range(len(lis)-1,-1,-1):
        if i + 1 < len(lis):
            if lis[i]==0 and lis[i+1]==1:
                lis[i] = 1
    return lis

# varios ejemplos para testear los algoritmos
lista_1 = [ 0, 0, 0,-1, 1, 0, 0, 0,-1, 0, 1, 0, 0]
lista_2 = [ 0, 0, 0, 1, 0, 0]
lista_3 = [ 1, 0, 0, 0, 0, -1]
lista_4 = [ 0, 0, 0, 0, 0, -1]
lista_5 = [ 0, 0, 0, 0, 0, 1]
lista_6 = []

#%%

def propagar(lista):
    # comienzo con una cadena vacía
    c=''
    # traduzco de lista a cadena, con un diccionario
    d={-1:'-',0:'o',1:'x'}
    for e in l:
        c+=d[e]
    # separo en fragmentos
    fragmentos = c.split('-')  
    # quemo
    propagados = []
    for fragmento in fragmentos:
        if 'x' in fragmento:
            # lo cambio por todos quemados
            propagados.append('x'*len(fragmento))
        else:
            # los dejo como estan
            propagados.append(fragmento)
    # junto todo
    cadena_propagada = '-'.join(propagados)
    # invierto la traduccion: de cadena a lista
    i={'-':-1,'o':0,'x':1}
    lista_propagada = []
    for e in cadena_propagada:
        lista_propagada.append(i[e])
    # devuelvo
    return lista_propagada

l=[0,0,0,-1,0,0,0,1,0,0,0,0]
print(l)
print(propagar(l))

#%%

def propagar(lista):
	quemado = -1
	prendido = False
	for pos, fosfo in enumerate(lista):
		if fosfo == 1:
			prendido = True
		if fosfo == -1:
			if prendido:
				lista[quemado+1:pos] = [1] * (pos - quemado - 1)
				prendido = False
			quemado = pos
    # no hay fosforos quemados
	if prendido and quemado == -1: 
		lista = [1] * len(lista)
    # final de la lista
	if prendido and quemado != -1: 
		lista[quemado+1:len(lista)] = [1] * (len(lista) - 1  - quemado)
	return lista