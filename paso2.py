# Parte 1: Determinar si un número es par o impar
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print(f"El número {numero} es par.")
else:
    print(f"El número {numero} es impar.")

# Parte 2: Iterar sobre una lista e imprimir los cuadrados
numeros = [1, 2, 3, 4, 5]
print("\nCuadrados de los números en la lista:")
for num in numeros:
    print(f"El cuadrado de {num} es {num ** 2}")

# Parte 3: Usar un bucle while hasta que se cumpla una condición
print("\nIntroduce un número mayor a 10 para salir!")

while True:
    numero = int(input("Ingresa un número: "))
    if numero > 10:
        print("¡Número válido! Se termina el bucle!")
        break
    else:
        print("El número no es mayor a 10. Inténtalo de nuevo.")