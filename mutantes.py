letrasObligatorias = ["A", "T", "C", "G"]
secuenciaADN = []

# ------------------------------------------------------ #

# VALIDAR QUE EL USUARIO INGRESE LAS PALABRAS CORRECTAMENTE
def validarPalabra(dimMatriz, i):
    palabra = input().upper()
    validarSecuencia = False

    while validarSecuencia == False:

        cantCaracteres = True
        letrasCorrectas = True

        if len(palabra) != dimMatriz:
            print("solo deben ser",dimMatriz,"letras")
            cantCaracteres = False

        for letra in palabra:
            if letra not in letrasObligatorias:
                print(f"caracter '{letra}' no es válido.")
                letrasCorrectas = False

        if cantCaracteres == False or letrasCorrectas == False:
            print()
            print("Intente de nuevo. Palabra",i+1,":", end=" ")
            palabra = input().upper()
        else:
            validarSecuencia = True

    print("Correcto, secuencia ingresada: ", palabra)
    print()
    return palabra

# ------------------------------------------------------ #

# MOSTRAR ARRAY (SECUENCIA ADN CREADA POR EL USUARIO)
def mostrarArray(secuenciaADN):
    for x in range(len(secuenciaADN)):
        print(secuenciaADN[x], end=" ")
    print()
    print()

# MOSTRAR MATRIZ CREADA
def mostrarMatriz(matriz):
    for row in matriz:
        print(row)
    print()

# ------------------------------------------------------ #

# MATRIZ TRANSPUESTA
def matrizTranspuesta(matrizOriginal, rows, columns) :
    matrizTrans = []
    for r in range(rows):
        matrizTrans.append([])
        for c in range(columns):
            matrizTrans[r].append(matrizOriginal[c][r])
    
    return matrizTrans

# ------------------------------------------------------ #

# OBTENER DIAGONALES
def obtenerDiagonales(matriz):
    diagonales = []
    aux = ""
    dimMatriz = len(matriz)

    # Recorrido de la matriz por sus diagonales:
    # Inicio en esquina inferior izquierda, retrocediendo hasta la
    # esquina superior izquierda y asciendiendo hasta 
    # finalizar en la esquina superior derecha.

    # Bucle para obtener las diagonales inferiores a la central inclusive
    for i in range(dimMatriz-1, 0-1, -1):
        row = i
        col = 0
        
        while(row<dimMatriz and col<dimMatriz):
            aux += matriz[row][col]
            row = row + 1
            col = col + 1
        
        # Agregar diagonal al array
        diagonales.append(aux)
        # Reinicio de variable aux
        aux = ""


    # Bucle para obtener las diagonales superiores a la central sin incluir
    for i in range(dimMatriz):
        row = 0
        col = i+1

        while (row<dimMatriz and col<dimMatriz):
            aux += matriz[row][col]
            row = row + 1
            col = col + 1
        
        # Agregar diagonal
        diagonales.append(aux)
        # Reinicio de variable aux
        aux = ""

    return diagonales


# ------------------------------------------------------ #

# OBTENER MATRIZ ESPEJO (INVERTIR COLUMNAS)
def matrizEspejo(matriz, rows, columns):
    matrizEspejo = []
    for i in range(rows):
        matrizEspejo.append([])
        for j in range(columns-1, 0-1, -1):
            matrizEspejo[i].append(matriz[i][j])

    return matrizEspejo

# ------------------------------------------------------ #

# DETERMINAR SECUENCIAS DE LETRAS REPETIDAS
def consecutivos(arrayFila):
    valor = ' '
    cantidad = 1

    for c in arrayFila:
        if cantidad == 4:
            break
        elif c == valor:
            cantidad = cantidad + 1
        else:
            valor = c
            cantidad = 1
    
    return cantidad == 4

# ------------------------------------------------------ #

# DETERMINAR SI LA SECUENCIA CORRESPONDE A UN MUTANTE O NO.
def isMutant(secuenciaADN):
    # Resultado a retornar
    result = False

    ##Creando Matriz n*n
    matriz = []
    rows = len(secuenciaADN)
    columns = len(secuenciaADN)

    for i in range(rows):
        matriz.append([])
        for j in range(columns):
            # Se extrae cada letra de cada palabra de la secuencia
            matriz[i].append(secuenciaADN[i][j:j+1]) 

    # Mostrar matriz creada
    print("Matriz creada: ")
    mostrarMatriz(matriz)


    # Crear matriz transpuesta
    # La matriz transpuesta nos permite valorar la existencia de una 
    # secuencia vertical repetida de cuatro letras en la matriz original
    matrizTrans = matrizTranspuesta(matriz, rows, columns)


    # Obtener las diagonales de izq. a der. y guardarlas en un array
    diagonalesIzqDer = obtenerDiagonales(matriz)

    # La matriz espejo (columnas invertidas) permite obtener las diagonales
    # secundarias, es decir, aquellas de derecha a izquierda.
    matrizInvertida = matrizEspejo(matriz, rows, columns)
    diagonalesDerIzq = obtenerDiagonales(matrizInvertida)


    # Recorrido de las matrices: Por cada fila se invoca a consecutivos
    # que determina si existe una secuencia de cuatro letras repetidas.
    cantSecuenciasRepetidas = 0

    for i in range(rows):
        if consecutivos(matriz[i]):
            cantSecuenciasRepetidas = cantSecuenciasRepetidas + 1
            print("Coincidencia en fila con índice",i,".")
        
        if consecutivos(matrizTrans[i]):
            cantSecuenciasRepetidas = cantSecuenciasRepetidas + 1
            print("Coincidencia en columna con índice",i,".")
    

    # Recorrido de los arrays diagonales, primero se valida que la diagonal
    # cuente con 4 letras como mínimo
    for i in range(len(diagonalesIzqDer)):

        if len(diagonalesIzqDer[i]) >= 4:
            if consecutivos(diagonalesIzqDer[i]):
                cantSecuenciasRepetidas = cantSecuenciasRepetidas + 1
                print("Coincidencia en diagonal con índice",i,"de izq. a der.")
            
            if consecutivos(diagonalesDerIzq[i]):
                cantSecuenciasRepetidas = cantSecuenciasRepetidas + 1
                print("Coincidencia en diagonal con índice",i,"de der. a izq.")

    # Resultado final
    if cantSecuenciasRepetidas > 1:
        result = True
    elif cantSecuenciasRepetidas == 1:
        print("Solo hay una secuencia repetida.")
    else:
        print("No hay ninguna secuencia repetida.")

    print()   
    return result


## ----------------------------------------------------------

# PROGRAMA PRINCIPAL
print()
print("--- SISTEMA DE RECONOCIMIENTO DE MUTANTES ---")
print()

# Determinar cantidad de filas
dimMatriz = int(input("Ingrese la cantidad de filas: "))
print()
print(" ----------------------------------------- ")
print()

# Ingreso de secuencia
print("Ingrese",dimMatriz,"palabras de seis letras, solo deben ser A,T,C,G")
for i in range(dimMatriz):
    print("Palabra",i+1,": ", end="")
    palabra = validarPalabra(dimMatriz, i)
    secuenciaADN.append(palabra)

print()
print(" ----------------------------------------- ")
print()

# Mostrar secuencia creada
print("Secuencia creada: ")
mostrarArray(secuenciaADN)

# Resultado final
if isMutant(secuenciaADN):
    print("LA PERSONA ES MUTANTE")
else:
    print("LA PERSONA NO ES MUTANTE")

print()
print("Hasta luego !")
print()