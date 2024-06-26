# Calculadora 
opcion = '' # Define las opciones de las letras 

print('Calcula 2 numeros')  
print(
      's. Suma\n'
      'r. Resta\n'
      'm. Multiplica\n'
      'd. Divide\n'
      'p. Potencia \n'
      'rc. Raiz Cuadrada \n' 
      'f. Termina la operación')


while True: 
    try:
        opcion = input('Escoge una opción: ').lower() # Para que al escribir x, de multiplicación, tome mayúsculas también
        if opcion in ['s', 'r', 'm', 'd', 'p', 'rc', 'f']: # Para que verifique si el valor ingresado (el input) está dentro de las opciones de la lista    
            
            # Si es la opción 'f', se termina la operación 
            if opcion == 'f':
                print('Termina la operación')
                break 
        
            # Si es la opción 'rc', se opera con 1 número para la raíz cuadrada 
            elif opcion == 'rc':
                numero_1 = float(input('La raiz cuadrada de: '))
                raiz = numero_1 ** 0.5 
                print(f'La raiz cuadrada de {numero_1} es:  {raiz}')

            # Si no es 'f' ni 'rc', se opera con 2 números 
            else: 
                numero_1 = float(input('Primer Número: ')) # Para ingresar el primer número
                numero_2 = float(input('Segundo Número: ')) # Para ingresar el segundo número 

                # Para suma 
                if opcion == 's':
                    suma = numero_1 + numero_2
                    print(f'Suma {numero_1} + {numero_2} = {suma}')

                # Para resta
                elif opcion == 'r': 
                    resta = numero_1 - numero_2
                    print(f'Resta {numero_1} - {numero_2} = {resta}') 

                # Para multiplicación
                elif opcion == 'm':
                    multiplicacion = numero_1 * numero_2
                    print(f'Multiplica {numero_1} * {numero_2} = {multiplicacion}') 

                # Para división
                elif opcion == 'd':
                    if numero_2 != 0: # Para saber si el valor es distinto de 0 
                        division = numero_1 / numero_2
                        division = round(division, 3) # Para redondear el resultado en el tercer decimal 
                        print(f'Divide {numero_1} / {numero_2} = {division}') 
                    else:
                        print('No se puede dividir por 0')

                # Para potencia
                elif opcion == 'p': 
                    potencia = numero_1 ** numero_2
                    print(f'{numero_1}^{numero_2} = {potencia}')

        # Para todas las opciones no válidas
        else: 
            print('Por favor, escoge una opción válida (s, r, m, d, p, rc, f)')

    except ValueError:
        print('Ingresa una opción válida')