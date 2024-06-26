numero = 1
fizzbuzz= numero

while numero <= 100:  # hasta que numero llega el bucle 
    if numero == 24 or numero == 55: #identifica si es 24 o 55 
        print (numero) #imprime 24 y/o 55 
    elif numero % 3 == 0 and numero % 5 == 0: #verifica si el numero es multiplo de 5 y de 3
        print("FizzBuzz") # imprime el numero si es multiplo de 5 y 3
    elif numero % 3 == 0: #verifica si es multiplo de 3 
        print("Fizz")
    elif numero % 5 == 0: #verifica si es multiplo de 5
        print("Buzz")
    else:
        print(numero) #imprime numeros que no sean fizz o buzz 
    
    numero += 1 # suma uno para seguir el bucle 
    