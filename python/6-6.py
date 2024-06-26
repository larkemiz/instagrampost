
SumaPrimos = 0 

for Numero in range (2,354): 
   EsPrimo = True 
   
   for x in range (2, int(Numero**0.5)):
    Numero += 1 
    if Numero % x == 0:   
      EsPrimo = False 
      print (f'{Numero}     No es un numero primo\n')
      break 
    if EsPrimo:
      print (f'{Numero}     Si es un numero primo')
      SumaPrimos += Numero
      print (f'     La suma es: {SumaPrimos}\n')

print(f'Este es el resultado de todos los numeros primos del 1 al 354: {SumaPrimos}')