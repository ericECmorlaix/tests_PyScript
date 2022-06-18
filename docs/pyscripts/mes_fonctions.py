

def indice_min(nombres : list) -> int :
        indice = 0
        minimum = nombres[0]
        for i in range(len(nombres)) :
            if minimum > nombres[i] :
                minimum = nombres[i]
                indice = i
        return indice