#Menú Interactivo

opcion = 0

print(' Te ayudaremos a calcular un numero') 
numero = int(input('Escoge un numero: '))

print ('¿Qué quieres saber de este numero?\n'
'Estas son las opciones: \n'
'1. Cual es su potencia de 2\n'
'2. Si es divisible por 2\n'
'3. Cuanto es si se suma 2 veces\n'
'4. No quiero saber nada\n')


while opcion <= 4:
    opcion = int(input('Escoge una opcion: '))
    
    if opcion == 1:
        print("1. Cual es su potencia de 2")
        potencia = numero ** 2
        print(potencia)
    
    elif opcion == 2: 
        print("2. Si es divisible por 2") 
        if resultado := numero % 2 == 0: 
            print('Es divisible por 2')
        else:
            print('No es divisible por 2')       
    
    elif opcion == 3:
        print("3. Cuanto es si se suma 2 veces")
        def suma(numero): 
            resultado = numero*2
            return resultado
        print(suma(numero)) 

    else:
        print("4. No quiero saber nada") 
        break 

#ejemplo de chatgpt con el except como funcion 
opcion = 0

print('Te ayudaremos a calcular un número') 
numero = int(input('Escoge un número: '))

print('¿Qué quieres saber de este número?\n'
      'Estas son las opciones: \n'
      '1. Cuál es su potencia de 2\n'
      '2. Si es divisible por 2\n'
      '3. Cuánto es si se suma 2 veces\n'
      '4. No quiero saber nada\n')

while True:
    try:
        opcion = int(input('Escoge una opción: '))
        
        if opcion == 1:
            print("1. Cuál es su potencia de 2")
            potencia = numero ** 2
            print(potencia)
        
        elif opcion == 2: 
            print("2. Si es divisible por 2") 
            if numero % 2 == 0: 
                print('Es divisible por 2')
            else:
                print('No es divisible por 2')       
        
        elif opcion == 3:
            print("3. Cuánto es si se suma 2 veces")
            def suma(numero): 
                resultado = numero * 2
                return resultado
            print(suma(numero)) 

        elif opcion == 4:
            print("4. No quiero saber nada") 
            break

        else:
            print("Por favor, escoge una opción válida (del 1 al 4).")

    except ValueError:
        print("Entrada no válida. Por favor, ingresa un número del 1 al 4.")




