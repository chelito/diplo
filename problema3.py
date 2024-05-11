""" 

Problema 3: Defina una lista que contenga números de tipo float y determine: el largo de la lista, el valor
 mínimo, el valor máximo y la suma de los elementos de la misma. 
 
 """
mi_lista = [ 2,5.25,10,522,50]
largo = len(mi_lista)
minimo = min(mi_lista)
maximo = max(mi_lista)
suma = sum(mi_lista)
print( f"De la lista { mi_lista} \nEl largo de la lista es: {largo}. \nEl valor mínimo es {minimo}.")
print(f"El valor máximo es {maximo}.\nEl valor suma total es {suma}." )

"""
Luego ingrese un valor y determine si el
 mismo pertenece o no a la lista. 
 
"""
valor = float (input ("Ingrese el valor para consular si existe en la lista: " ))
if  valor in mi_lista:
    print( f" {valor} existe en lista{mi_lista} y esta en la posición { mi_lista.index(valor)}" )
else:
    print( f" {valor} no existe en lista{mi_lista}." )
 

