def suma(x,y): #suma donde se introducen los numeros en el codigo 
   resultado = x + y 
   return resultado

print(suma (2,4))


numero1 = int(input('introduce un numero')) #tipo de suma para introducir numeros en la consola 
numero2 = int(input('introduce un numero'))

resultado = numero1 + numero2 

print(resultado)


def saludar(x): #funcion para saludar 
   print ( f'Hola {x}, mucho gusto')

saludar ('Carlos')


def fizzbuzz(x):  # fizzbuzz funcion 
   if resultado := x % 3 == 0 and x % 5 == 0:  
      print('fizzbuzz') 
   elif resultado := x % 3 == 0: #fizz 
      print('fizz')
   elif resultado := x % 5 == 0: #buzz 
      print('buzz')
   else: 
      print(x)
   
fizzbuzz(5)

def NumeroPrimo(numero): # defino la variable 
   if numero == 1 or numero == 0: #si es 1 o 0 es falso que sea n primo 
      return False 
   for x in range (2, numero): #x es el num por el que se divide la variable numero definida en la fila 34 (no contempla "numero" [2, numero[ )
      if numero % x == 0: # si numero es divisible en el rango de x el modulo sera 0 y eso me dara falso, ya que sera divisible por otro numero aparte de si mismo 
         return False 
      return True 
print (NumeroPrimo(5))
print (NumeroPrimo(27))
print (NumeroPrimo(345))
print (NumeroPrimo(7))
print (NumeroPrimo(12))


