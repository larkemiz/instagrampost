#13/06 string con signos 

def texto_con_mayus_reemplazadas (texto):
    for letra in texto: 
         if letra.isupper():
            texto = texto.replace (letra,'$')
    return texto 

texto = 'Viva la CocaCola'
print (texto_con_mayus_reemplazadas(texto))