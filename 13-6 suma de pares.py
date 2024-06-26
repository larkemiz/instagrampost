def suma_pares(lista):
    suma = 0 
    numeros_pares = []  #lista que almacenará los números pares resultantes de la función for 


    for numero in lista: #para los numeros en la lista, 
        if numero % 2 == 0:
            suma += numero 
            numeros_pares.append(numero)
    
    print (f'numeros pares{numeros_pares}')
    return suma 

numeros =[1,2,3,4,5,6,7,8,9,10] 
print (suma_pares (numeros))

