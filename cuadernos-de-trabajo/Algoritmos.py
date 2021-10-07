import big_o
import matplotlib.pyplot as plt
import math
from random import shuffle
from random import seed
from big_o import complexities as cls

from random import shuffle
from random import seed

#Algoritmos.py, archivo en donde se van a encontrar todos los algoritmos de ordenamiento, asi como funciones y demas operaciones
#*****-------------------------------------Merge--Sort-------------------------------------------------*****#

# Python program for implementation of MergeSort. Hecho por Dravid (Fecha desconocida), recuperado de https://www.geeksforgeeks.org/python-program-for-merge-sort/
def merge(arr, l, m, r): #Funcion principal que realiza el proceso principal del algoritmo de Merge-Sort
    #Establece los limites de cada uno de los sub-arreglos
    n1 = m - l + 1
    n2 = r- m
    #Se crean los sub-arreglos respectivos, identificados como 'L' (LEFT) y 'R' (RIGHT), creando asi una copia del array original, pero dividido en dos
    L = [0] * (n1)
    R = [0] * (n2)
    for i in range(0 , n1):
        L[i] = arr[l + i]
    for j in range(0 , n2):
        R[j] = arr[m + 1 + j]
    i = 0     # Indice inicial del primer sub-arreglo
    j = 0     # Indice inicial del segundo sub-arreglo
    k = l     # Indice inicial del sub-arreglo merged u ordenado
    #A partir de diferentes condiciones comienza a colocar los elementos ordenados
    while i < n1 and j < n2 :
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1
def mergesort(arr,l,r): #Funcion auxiliar que recibe tres parametros: Un arreglo 'arr', posicion inicial 'l' , Posicion final del 'arr' (tamano de 'arr' - 1) 'r'
    if l < r:
        m = (l+(r-1))//2 #m es la mitad del arreglo, se hace de esta forma para evitar un  posible overflow
        #De manera recursiva se comienza a ordenar el arreglo, primero desde el principio ('l') del arreglo ('arr') hasta la mitad de este ('m')
        mergesort(arr, l, m)
        #Luego, desde la mitad+1 ('m+1') hasta el final del arreglo ('r')
        mergesort(arr, m+1, r)

        merge(arr, l, m, r)
def mergeSort(arr):
    l=len(arr)
    mergesort(arr,0,l-1)

#*****-------------------------------------------Quick---Sort----------------------------------------------*****#

# Algoritmo Quick-Sort implementado por Mohit Kumra y editado por Ronald Esquivel Lopez, recuperado en https://www.geeksforgeeks.org/python-program-for-quicksort/
# Los elementos menores al pivote seran ordenados a la izquierda del mismo y los mayores a la derecha del pivote
def partition(arr,low,high): #Algoritmo Quick-Sort principal que tiene como parametros: un arreglo 'arr', indice de partida 'low'e indice de llegada 'high'
    i = ( low-1 )         # elemento primero en sub-arreglo o arreglo
    pivot = arr[(int)(high)]     # pivote

    for j in range(low , high):
        # Si el elemento es mas pequeno o igual al pivote se incrementa el indice del elemento pequeno
        if   arr[j] <= pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] #Swap

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )
def quicksort(arr,low,high): #Funcion auxiliar recursiva que realiza la division o particion recursiva del arreglo en sub-arreglos
    if low < high:
        pi = partition(arr,low,high)
        quicksort(arr, low, pi-1) #Se ejecuta el algoritmo a todas las partes  en la poscicion izquierda de todos los arreglos o sub-arreglos o particiones
        quicksort(arr, pi+1, high) #Se ejecuta el algoritmo a todas las partes  en la poscicion derecha de todos los arreglos o sub-arreglos o particiones
def quickSort(arr):
    l=len(arr)
    quicksort(arr,0,l-1)
#*****-------------------------------------------QuickSort-Mitad----------------------------------------------*****#
def quickSortOP(arr): 
    largo = len(arr)
    quicksortOP(0, largo - 1,arr)
def exchange(i,j,arr): 
    temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
def quicksortOP(low,high,arr): 
    i , j = low , high
    pivot = arr[(int)(low + (high-low)/2)]
    while (i <= j): # If the current value from the left list is smaller than the pivot     
        while (arr[i] < pivot):# element then get the next element from the left list
            i+=1 #If the current value from the right list is larger than the pivot
        while (arr[j] > pivot): 
            j-=1;
            # If we have found a value in the left list which is larger than
            # the pivot element and if we have found a value in the right list
            # which is smaller than the pivot element then we exchange the
            # values.
            # As we are done we can increase i and j
        if (i <= j):
            exchange(i, j, arr)
            i+=1
            j-=1
    if (low < j): #recursion
        quicksortOP(low, j,arr)
    if (i < high):
        quicksortOP(i, high,arr)
#*****-------------------------------------------QuickSort Over - Power----------------------------------------------*****#
'''def quickSortOP(arr):
    l=len(arr)
    Quicksort(arr,0,l-1)
#array = [5,4,3,2,1]
def Quicksort(L, first, last):
    # definimos los índices y calculamos el pivote
    i = first
    j = last
    pivote = (int)((L[i] + L[j]) / 2)

    # iteramos hasta que i no sea menor que j
    while i < j:
        # iteramos mientras que el valor de L[i] sea menor que pivote
        while L[i] < pivote:
            # Incrementamos el índice
            i+=1
        # iteramos mientras que el valor de L[j] sea mayor que pivote
        while L[j] > pivote:
            # decrementamos el índice
            j-=1
        # si i es menor o igual que j significa que los índices se han cruzado
        if i<=j:
            # creamos una variable temporal para guardar el valor de L[j]
            x = L[j]
            # intercambiamos los valores de L[j] y L[i]
            L[j] = L[i]
            L[i] = x
            # incrementamos y decrementamos i y j respectivamente
            i+=1
            j-=1

    # si first es menor que j mantenemos la recursividad
    if first < j:
        Quicksort(L, first, j)
    # si last es mayor que i mantenemos la recursividad
    if last > i:
        Quicksort(L, i, last)'''

#*****-------------------------------------------Burbuja----------------------------------------------*****#
def bubbleSort(A):
    n = len(A)
    for i in range(1, n):
        for j in range(0, n - i):
            if A[j] > A[j + 1]:
                swap(A, j, j + 1)

def swap(A, i, j):
    tmp = A[i]
    A[i] = A[j]
    A[j] = tmp

#*****-------------------------------------------Burbuja-Optimizado----------------------------------------------*****#
def optimized_bubbleSort(A):
    change = True
    n = len(A)
    while (change and n>1): #verifica si hubo cambio
        change = False
        for j in range(0, n-1):
            if A[j] > A[j+1]:
                swap(A, j, j+1) #hace el cambio
                change = True
        n-=1

#*****-------------------------------------------Selection-Sort----------------------------------------------*****#
def selectionSort(A):
    for i in range(len(A)):
        min=i #pivote
        for j in range(i,len(A)):
            if(A[j] < A[min]): #verifica si un numero es menor al pivote
                min=j #crea el nuevo pivote

        aux=A[i] #temporal para colocar el pivote
        A[i]=A[min]
        A[min]=aux

#*****-------------------------------------------Insertion-Sort----------------------------------------------*****#
def insertionSort(A): #codigo tomado de geeksforgeeks, mencionado en la bibliografia

    # recorre la lista
    for i in range(1, len(A)):
        key = A[i]

        # Mueve los elementos de A[0..i-1], que son
        # mas grandes que key, hacia la siguiente posicion
        # de su posicion actual
        j = i-1
        while j >= 0 and key < A[j] :
                A[j + 1] = A[j]
                j -= 1
        A[j + 1] = key

#*****-------------------------------------------Analisis de datos----------------------------------------------*****#

#Funcion que imprime la complejidad de la prueba y devuelve los coeficientes de tiempo obtenidos
def aprox_asintotica(datos):
    ys = datos['times']
    for k, v in datos.items():
        if isinstance(k, cls.ComplexityClass):
            residual = v
            r2 = 1 - residual / (ys.size * ys.var())
            print(k, f' (r={residual}, r^2={r2})')
            return list(k.coeff) # [constante de tiempo de la prueba, el factor que multiplica la operacion]

#Graficar las pruebas obtenidas segun tiradas las pruebas sin necesidad de utilizar un tiempo fijo
''' Parametros
 @ datos: los datos obtenidos de la prueba de cierto algoritmo
 @ operacion: la operacion (criterio de la funcion) necesaria para graficar
'''
def graficar_casos(datos,operacion):
    xs = datos['measures']
    ys = datos['times']
    aproximacion_obtenida = aprox_asintotica(datos)
    constante= aproximacion_obtenida[0]
    coeficiente =aproximacion_obtenida[1]
    aprox_ys = [constante+coeficiente*operacion(n) for n in xs]
    plt.plot(xs, aprox_ys,label='Aproximación')
    plt.plot(xs, ys, label="Valores obtenidos")
    plt.legend(loc = 2)
    plt.ylabel('Tiempo (s)')
    plt.xlabel('n (tamaño del arreglo)')
    plt.show()

#Graficar dos pruebas obtenidas segun tiradas las pruebas sin necesidad de utilizar un tiempo fijo
''' Parametros
 @ datos: los datos obtenidos de la prueba de cierto algoritmo
 @ datos2: los datos obtenidos de la prueba de un segundo algoritmo
 @ operacion: la operacion (criterio de la funcion) necesaria para graficar
 @ nombre1: nombre del primer algoritmo
 @ nombre2: nombre del segundo algoritmo
'''
def graficar_2_casos(datos,datos2,operacion,operacion2,nombre1,nombre2):
    xs = datos['measures']
    ys = datos['times']
    ys2 = datos2['times']
    print('\n'+ nombre1 + " = ")
    aproximacion_obtenida = aprox_asintotica(datos)
    print('\n'+ nombre2 + " = ")
    aproximacion_obtenida2 = aprox_asintotica(datos2)
    constante,constante2 = aproximacion_obtenida[0],aproximacion_obtenida2[0]
    coeficiente,coeficiente2=aproximacion_obtenida[1],aproximacion_obtenida2[1]
    aprox_ys = [constante+coeficiente*operacion(n) for n in xs]
    aprox_ys2 = [constante2+coeficiente2*operacion2(n) for n in xs]
    plt.plot(xs, aprox_ys,label='Aproximación '+nombre1)
    plt.plot(xs, aprox_ys2,label='Aproximación '+nombre2)
    plt.plot(xs, ys, label=nombre1)
    plt.plot(xs, ys2, label=nombre2)
    plt.legend(loc = 2)
    plt.ylabel('Tiempo (s)')
    plt.xlabel('n (tamaño del arreglo)')
    plt.show()

#Graficar cuatro pruebas obtenidas segun tiradas las pruebas sin necesidad de utilizar un tiempo fijo
''' Parametros
 @ datos: los datos obtenidos de la prueba de cierto algoritmo
 @ datos2: los datos obtenidos de la prueba de un segundo algoritmo
 @ datos3: los datos obtenidos de la pueba de un tercer algoritmo
 @ datos4: los datos obtenidos de la prueba de un cuarto algoritmo
'''
def graficar_4_casos(datos, datos2, datos3, datos4):
    xs = datos['measures']
    ys = datos['times']
    ys2 = datos2['times']
    ys3 = datos3['times']
    ys4 = datos4['times']
    print('\n' "burbuja = ")
    aproximacion_obtenida = aprox_asintotica(datos)
    print('\n' "burbuja_optimizado = ")
    aproximacion_obtenida2 = aprox_asintotica(datos2)
    print('\n' "insertion = ")
    aproximacion_obtenida3 = aprox_asintotica(datos3)
    print('\n' "selection = ")
    aproximacion_obtenida4 = aprox_asintotica(datos4)
    constante,constante2,constante3,constante4  = aproximacion_obtenida[0],aproximacion_obtenida2[0], aproximacion_obtenida3[0], aproximacion_obtenida4[0]
    coeficiente,coeficiente2,coeficiente3,coeficiente4=aproximacion_obtenida[1],aproximacion_obtenida2[1],aproximacion_obtenida3[1],aproximacion_obtenida4[1]
    aprox_ys = [constante+coeficiente*cuadrado(n) for n in xs]
    aprox_ys2 = [constante2+coeficiente2*cuadrado(n) for n in xs]
    aprox_ys3 = [constante3+coeficiente3*cuadrado(n) for n in xs]
    aprox_ys4 = [constante4+coeficiente4*cuadrado(n) for n in xs]
    plt.plot(xs, aprox_ys,label='Aproximación burbuja')
    plt.plot(xs, aprox_ys2,label='Aproximación Optimizado')
    plt.plot(xs, aprox_ys3,label='Aproximación insertion')
    plt.plot(xs, aprox_ys4,label='Aproximación selection')
    plt.plot(xs, ys, label="burbuja")
    plt.plot(xs, ys2, label="burbuja_optimizado")
    plt.plot(xs, ys3, label="insertion")
    plt.plot(xs, ys4, label="selection")
    plt.legend(loc = 2)
    plt.ylabel('Tiempo (s)')
    plt.xlabel('n (tamaño del arreglo)')
    plt.show()

#Generar los datos de complejidad temporal dado un algoritmo que se desea probar
''' Parametros
 @ complejidades_esperadas: las complejidades que se tiene como hipotesis a medir
 @ generador_caso: la funcion que retorna una lista segun un caso particular al algoritmo
 @ algoritmo: el algoritmo que se desea probar la complejidad temporal
 @ valores_n: parametros necesarios de la funcion big_o
 ejemplo valores = {"min_n":3,"max_n":250,"n_medidas":100,"repeticiones":3}
'''
def generar_datos(complejidades_esperadas, generador_caso,algoritmo,valores_n):
    clase, datos = big_o.big_o(algoritmo,
                     generador_caso,
                     valores_n["min_n"], valores_n["max_n"],
                     valores_n["n_medidas"],valores_n["repeticiones"],
                     verbose=False, return_raw_data=True,
                     classes=complejidades_esperadas)
    return datos

#Graficar los datos obtenidos al ejecutar un caso particular a 2 algoritmos (A y B)
''' Parametros
 @ datos_a y datos_b: los datos obtenidos de la prueba para cada algoritmo
 @ nombre_a y nombre_b: nombres de los algoritmos seleccionados
'''
def comparar_algoritmos(datos_A,datos_B,nombre_A,nombre_B):
    xs = datos_A['measures']
    tiempos_a = datos_A['times']
    tiempos_b = datos_B['times']
    plt.plot(xs, tiempos_a, label=nombre_A)
    plt.plot(xs, tiempos_b, label=nombre_B)
    plt.legend(loc = 2)
    plt.ylabel('Tiempo (s)')
    plt.xlabel('n (tamaño del arreglo)')
    plt.show()

#Creador de cuadros comparativos

def crear_cuadros_comparativos(datos_A,datos_B,nombre_A,nombre_B):
    print('{:^15}{:^25}{:^25}{:^25}{:^25}'.format('n_elementos',nombre_A+': Tiempo',nombre_B+': n_elementos','Diferencia','Ganador'))
    n_medidas=len(datos_A['measures'])
    for y in range(0,n_medidas):
        diferencia = datos_A['times'][y] - datos_B['times'][y]
        ganador = nombre_B
        if(diferencia<0):
            ganador = nombre_A
        print('{:^15}{:^25}{:^25}{:^25}{:^25}'.format(datos_A['measures'][y], datos_A['times'][y],datos_B['times']  [y],diferencia,ganador))
        print('________________________________________________________________________________________________')

#Crear un cuadro con los tiempos para los casos dados de un algoritmo
def crear_cuadros_casos(datos_peor,datos_promedio,datos_mejor):
    print('{:^15}{:^25}{:^25}{:^25}'.format("N medidas","C.Peor","C.Prom",'C.Mejor'))
    n_medidas= len(datos_promedio['measures'])
#Iterar por las medidas y  tiempos de 50 a 50
    for y in range(0,n_medidas,5):
        n_actual = datos_promedio['measures'][y]
        t_peor = str(float("%0.7f" % (datos_peor['times'][y])))+'s'
        t_mejor = str(float("%0.7f" % (datos_mejor['times'][y])))+'s'
        t_promedio = str(float("%0.7f" % (datos_promedio['times'][y])))+'s'
        print('{:^15}{:^25}{:^25}{:^25}'.format(n_actual,t_peor,t_promedio,t_mejor))
        print('________________________________________________________________________________________________')

#crea un cuadro comparativo para los algoritmos por intercambio de adyacentes
def crear_cuadros_adyacentes(datos_Bub, datos_Op, datos_ins, datos_sel):
    print('{:^15}{:^20}{:^20}{:^20}{:^20}{:^20}'.format("n_elementos", "BubbleSort", "Optimizado", "Insertion","Selection","Menor tiempo"))
    for y in range (0, len(datos_Bub['measures']), 5):
        n = datos_Bub['measures'][y]
        bub = str(float("%0.7f" % (datos_Bub['times'][y])))+'s'
        opt = str(float("%0.7f" % (datos_Op['times'][y])))+'s'
        ins = str(float("%0.7f" % (datos_ins['times'][y])))+'s'
        sel = str(float("%0.7f" % (datos_sel['times'][y])))+'s'
        dict_tiempos = {bub:"BubbleSort", opt:"Optimizado", ins:"Insertion", sel:"Selection"}
        mejor_tiempo = min(bub, opt, ins, sel)
        print('{:^15}{:^20}{:^20}{:^20}{:^20}{:^20}'.format(n, bub, opt, ins, sel, dict_tiempos[mejor_tiempo]))
        print('_________________________________________________________________________________________________________________')

#*****-------------------------------------------Operaciones matematicas----------------------------------------------*****#
# Estas operaciones ayudan a realizar las operaciones necesarias en el aprox de la grafica
def cuadrado(n):
    return pow(n,2)

def logaritmo(n):
    return math.log2(n)

def lineal(n):
    return n

def linearitmica(n):
    return n*math.log2(n)
#*****-------------------------------------------Generar Casos----------------------------------------------*****#
def generar_descendente(n):
    A = list(range(0, n))

    return A[::-1] #invierte la lista

def generar_aleatorio(n):
    seed(0)
    A = list(range(0,n))
    shuffle(A)

    return A

def generar_ascendente(n):
    A = list(range(0, n))

    return A
#*****-------------------------------------------Generar Casos especiales----------------------------------------------*****#


def Quick_Peor(n): #Funcion que recibe como parametro 'n' al tamano maximo del arreglo
    arr = list(range(1,n+1))
    return arr

def Quick_Mejor(n): #Funcion que recibe como parametro 'n' al tamano maximo del arreglo, si es par, convierte el valor en impar
    if(n%2==0):
        n+=1
    arr = list(range(1, n+1))
    shuffle(arr)
    return arr

def Quick_Promedio(n): #Funcion que recibe como parametro 'n' al tamano maximo del arreglo
    arr1 = list(range(0, (int)(n/2)))
    arr2 = list(range((int)(n/2)+1, n+1))
    shuffle(arr2)
    arr = arr1 + arr2
    return arr

def Merge_Peor(n): #Funcion que recibe como parametro 'n' al tamano maximo del arreglo
    arr = n * [0]
    limite = (int)((n/2)-1)
    for i in range(0,n-2):
        arr[i]=i+1
    shuffle(arr)
    arr[limite] = n
    arr[n-1] = n-1
    return(arr)
def Merge_Mejor(n): #Funcion que recibe como parametro 'n' al tamano maximo del arreglo
    rest = n - (int)(n/2)
    arr1 = (int)(n/2) * [0]
    for i in range(0,((int)(n/2))):
        arr1[i] = i+1
    arr2 = rest * [0]
    for j in range((int)(n/2), n):
        arr2[j-(int)(n/2)] = j+1
    shuffle(arr1)
    shuffle(arr2)
    arr = arr1 + arr2
    return arr


def Merge_Promedio(n): #Funcion que recibe como parametro 'n' al tamano maximo del arreglo
    arr1 = list(range(0, (int)(n/2)))
    arr2 = list(range((int)(n/2)+1, n+1))
    shuffle(arr2)
    arr = arr1 + arr2
    return arr

def generar_rango(datos_A,datos_B,nombre_A,nombre_B):
	diferencias = []
	tol = (int)((len(datos_A['measures']))*0.3)
	tolerancia = 0
	for x in range(len(datos_A['measures'])):
		diferencia = datos_A['times'][x] - datos_B['times'][x]
		if diferencia<0:
			diferencias.append(datos_A['measures'][x])
			tolerancia = 0
		else:
			if tolerancia <= tol:
				break
			else:
				tolerancia+=1
	LEN = len(diferencias)
	print("Dependiendo de las experimentaciones y del kernel en donde este documento es ejecutado, hay ocasiones en las cua -les " + nombre_A + " es más eficiente que  " + nombre_B + ". En este caso:" )
	if LEN==0:
		print("\n" + nombre_B + " es más eficiente en todo el rango")
	elif LEN==1:
		a = diferencias[0]
		print("\n" + nombre_A + " es más eficiente con tamaños de arreglos que van desde el 0 hasta " + str(a) + " aproximadamente.")
	else:
		a = diferencias[0]
		b = diferencias[LEN-1]
		print("\n" + nombre_A + " es más eficiente con tamaños de arreglos que van desde el " + str(a) + " hasta " + str(b) + " aproximadamente.")

def generar_rango_2(datos_A,datos_B,nombre_A,nombre_B):
	diferencias = []
	tol = (int)((len(datos_A['measures']))*0.3)
	tolerancia = 0
	for x in range(len(datos_A['measures'])):
		diferencia = datos_A['times'][x] - datos_B['times'][x]
		if diferencia>0:
			diferencias.append(datos_A['measures'][x])
			tolerancia = 0
		else:
			if tolerancia <= tol:
				break
			else:
				tolerancia+=1
	LEN = len(diferencias)
	if LEN==0:
		print("\n" + nombre_A + " es más eficiente en todo el rango")
	else:
		a = diferencias[0]
		b = diferencias[LEN-1]
		print("\n" + nombre_B + " es más eficiente con tamaños de arreglos que van desde el " + str(a) + " hasta " + str(b))
