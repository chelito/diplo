"""
Problema 2: Escriba un programa donde se ingrese el radio y el largo de un cilindro e imprima la superficie y el
 volumen del mismo con dos cifras decimales.
 Areacilindro=2πr(r+l)
 Volumencilindro=π(r**2)*l
 
 """
pi = 3.1416
radio = float(input("Ingrese el radio: "))
largo = float(input("Ingrese el radio: "))
area_cilindro = 2*pi*radio*(radio+largo)
volumencilindro = pi*(radio**2)*largo
print(f"El area del cilindro es: {area_cilindro} y el volumen es {volumencilindro}") 