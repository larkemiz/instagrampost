#Calculadora 
opcion = '' #Define las opciones como strings 
while True: 
    print('Calcula 2 numeros\n')  
    print(
                  's. Suma\n'
                  'r. Resta\n'
                  'm. Multiplica\n'
                  'd. Divide\n'
                  'p. Potencia\n'
                  'rc. Raiz Cuadrada\n' 
                  'f. Termina la operación\n')

    try:
        opcion = input ('Escoge una opción: ').lower() #para que al escribir x, de multiplicación, tome mayúsculas también
        if opcion in ['s', 'r', 'm', 'd', 'p', 'rc', 'f']: #para que verifique si el valor ingresado (el input) está dentro de las opciones de la lista    
            
            #si es la opcion fin, se termina la operacion 
            if opcion == 'f':
                print ('Termina la operación')
                break 
        
            #si es raiz se opera con 1 numero 
            elif opcion == 'rc':
                numero_1 = float (input('La raiz cuadrada de: '))
                raiz = numero_1 ** 0.5
                raiz = round (raiz, 3) 
                print(f'La raiz cuadrada de {numero_1} es:  {raiz}\n')
                break 

        #todo lo demás: se opera con 2 numeros 
            else: 
                while True: 
                    try: 
                        numero_1 = float(input('Primer Número: ')) #Para ingresar el primer numero 
                        break 
                    except ValueError:
                        print ('Ingresa un número válido')    

                while True: 
                    try:
                        numero_2 = float(input('Segundo Número: ')) #Para ingresar el segundo numero 
                        break 
                    except ValueError:
                        print ('Ingresa un número válido')     

                #para suma 
                if opcion == 's':
                    suma = numero_1 + numero_2
                    print(f'suma {numero_1} + {numero_2} = {suma}\n')
        
                #para resta
                elif opcion == 'r': 
                    resta = numero_1 - numero_2
                    print(f'resta {numero_1} - {numero_2} = {resta}\n')     
        
                #para multiplicación
                elif opcion == 'm':
                    multiplica = numero_1 * numero_2
                    print(f'multiplica {numero_1} * {numero_2} = {multiplica}\n') 

                #para division
                elif opcion == 'd' :
                    if numero_2 != 0: #para saber si el valor es distinto de 0 
                        division = numero_1 / numero_2
                        division = round (division, 3) #para redondear el resultado en el tercer decimal 
                        print (f'divide {numero_1} / {numero_2} = {division}\n') 
                    else:
                        print ('No se puede dividir por 0')
        
                #para potencia
                elif opcion == 'p':    
                    potencia = numero_1 ** numero_2
                    print (f' {numero_1} a la potencia de {numero_2} =  {potencia}\n')
        
        #para todas las opciones no validas
        else: 
            print('Por favor, escoge una opción válida (s, r, m, d, p, rc, f)')

    except ValueError:
        print('Ingresa una opción válida')







        