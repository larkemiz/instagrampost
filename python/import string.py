import string

# Texto original
texto = 'La vida es un viaje lleno de sorpresas, desafíos y momentos inolvidables? Cada día nos ofrece la oportunidad de crecer... aprender y descubrir nuevas experiencias! A veces, el camino puede ser difícil... y lleno de obstáculos!!! Pero es importante recordar que cada desafío nos ayuda a fortalecernos??? y a alcanzar nuestras metas! No importa cuán difícil parezca el camino... Siempre hay una luz al final del túnel??? Aprovechemos cada momento. Vivamos con pasión y enfrentemos cada desafío con valentía y determinación! Así es como creamos recuerdos que perdurarán para siempre en nuestro corazón...'

# Eliminar espacios en blanco al inicio y al final
texto_sin_espacios_extra = texto.strip()

# Convertir todo el texto a minúsculas
texto_minuscula = texto_sin_espacios_extra.lower()

# Reemplazar todos los signos de puntuación por espacios
texto_sin_signos = texto_minuscula.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))

# Dividir el texto en palabras
palabras = texto_sin_signos.split()

# Contar la frecuencia de cada palabra
frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

# Contar la frecuencia de cada palabra
frecuencia_palabras = {}
for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

# Ordenar el diccionario por frecuencia (de mayor a menor)
frecuencia_palabras_ordenadas = {k: v for k, v in sorted(frecuencia_palabras.items(), key=lambda item: item[1], reverse=True)}

# Texto final corregido
texto_final = ' '.join(palabras)

# Mostrar el texto final corregido
print("Texto final corregido:")
print(texto_final)

# Mostrar las palabras con sus frecuencias en orden descendente
print("\nFrecuencia de cada palabra (de mayor a menor):")
for palabra, frecuencia in frecuencia_palabras_ordenadas.items():
    print(f"{palabra}: {frecuencia}")