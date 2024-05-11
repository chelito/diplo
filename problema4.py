""" 

Problema 4: Utilizando una tupla, genere un programa que determine con True o False si una letra que se
ingresa es una vocal o no.

 """
def es_vocal(letra):
    # Convertimos la letra a minúscula para manejar ambos casos
    letra = letra.lower()
    
    if letra in 'aeiou':
        return True
    else:
        return False

# Ejemplos de uso
letra = input ("Ingrese una letra para saber si es una vocal: ")
print(es_vocal(letra))  # Debería imprimir True
 
 

