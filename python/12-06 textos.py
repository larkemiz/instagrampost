#Reemplazar subcadenas todos los HOLA/hola por Hola 
print ('\n')

saludo = "HOLA MUNDO, hola universo"
saludo_minusculas = saludo.lower() #pone todo en minuscula 
nuevo_saludo = saludo_minusculas.replace("hola", "Hola")

print(nuevo_saludo)
print ('--------------------------------------------------------------\n')

#Dividir cadenas 

frutas = 'Manzana pera plátano uva'
frutas_separadas = frutas.split()
print(f'La lista es: {frutas_separadas}')  # Me entrega una lista dividida
print ('--------------------------------------------------------------\n')

#Eliminar los espacios 

saludo = '  Hola mundo  '
saludo_sin_espacios = saludo.strip()
print(saludo_sin_espacios)
print ('--------------------------------------------------------------\n')

#Ejercicio combinado 
texto = 'La vida es un viaje lleno de sorpresas, desafíos y momentos inolvidables? Cada día nos ofrece la oportunidad de crecer... aprender y descubrir nuevas experiencias! A veces, el camino puede ser difícil... y lleno de obstáculos!!! Pero es importante recordar que cada desafío nos ayuda a fortalecernos??? y a alcanzar nuestras metas! No importa cuán difícil parezca el camino... Siempre hay una luz al final del túnel??? Aprovechemos cada momento. Vivamos con pasión y enfrentemos cada desafío con valentía y determinación! Así es como creamos recuerdos que perdurarán para siempre en nuestro corazón...'
texto_sin_espacios_extra = texto.strip() #Eliminar espacios en blanco al inicio y al final 
texto_minuscula = texto_sin_espacios_extra.lower() #Pone todo en minuscula 
texto_mayuscula_inicio = texto_minuscula.capitalize ()
texto_sin_signos = texto_mayuscula_inicio.replace ('.'','';'':''!''?', ' ')
texto_dividido = texto_sin_signos.split()
