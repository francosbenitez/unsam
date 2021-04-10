import csv

def leer_arboles(nombre_archivo):
    arboles = list()
    f = open(nombre_archivo, encoding="utf8")
    rows = csv.reader(f)
    headers = next(rows)
    for row in rows:
        lote = dict(zip(headers, row))
        arboles.append(lote)
    return arboles

arboleda = leer_arboles("Data/arbolado.csv")

def medidas_de_especies(espcies, arboleda):
    diccionario = {}
    for especie in especies:
        diccionario[especie] = [(float(arbol["altura_tot"]), 
                             float(arbol["diametro"])) for arbol in arboleda if arbol["nombre_com"] == especie]
    return diccionario

especies = ['Eucalipto', 'Palo borracho rosado', 'Jacarandá']
medidas = medidas_de_especies(especies, arboleda)

def medidas_de_especies_extra(especies, arboleda):
    diccionario_extra = {especie: [(float(arbol["altura_tot"]), 
                             float(arbol["diametro"])) for arbol in arboleda if arbol["nombre_com"] == especie] for especie in especies}
    return diccionario_extra

medidas_extra = medidas_de_especies_extra(especies, arboleda)    
