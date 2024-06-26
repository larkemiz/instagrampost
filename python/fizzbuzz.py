numero = 1

while numero <= 100:  # Se puede cambiar 100 
    if numero % 3 == 0 and numero % 5 == 0: #verifica si el numero es multiplo de 5 y de 3
        print("FizzBuzz") # imprime el numero si es multiplo de 5 y 3
    elif numero % 3 == 0:
        print("Fizz")
    elif numero % 5 == 0:
        print("Buzz")
    else:
        print(numero)
    
    numero += 1
    