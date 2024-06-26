#desafio while 
numero=1

while numero <= 10: #numero hasta el 10
    print (numero) #imprime el numero 
    numero +=1 #le suma 1 

#----------------------------------------------------------
#desafio suma con while 
suma = 0
cuenta = 1
while cuenta <= 10:
    suma += cuenta 
    print(f'Al sumar{suma - cuenta} + {cuenta}, da como resultado {suma}')
    cuenta += 1
print (f'La suma de los primeros 10 numeros naturales es: {suma}')


#-------------------------------------------------------
#desafio random 
import random 
NumeroAleatorio = random.randint (1,10)     #No se para que sirve randint :c 
intento = 0                                 #Inicializamos la variable de intento fuera del bucle

while intento != NumeroAleatorio:
    intento = int(input('Escoge un numero: ')) #intento = int(input('Escoge un número: ')
    if intento == NumeroAleatorio:
        print ('Es el numero correcto')
        break 
    else: 
        print ('Intenta de nuevo')

#---------------------------------------------------------

#Menú Interactivo

opcion = 0

print("Menú:Tienes 1 numero que quieres saber")
while opcion <= 4:
    opcion = int(input('Escoge una opcion: '))
    if opcion == 1:
        print("1. Cual es su potencia de 2")
    elif opcion == 2: 
        print("2. Si es divisible por 2")
    elif opcion == 3:
        print("3. Cuanto es si se suma 2 veces")
    else:
        print("4. Salir")


