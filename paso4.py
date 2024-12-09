# Calculadora básica
print("Bienvenido a la calculadora básica.")

num1 = float(input("Ingresa el primer número: "))
num2 = float(input("Ingresa el segundo número: "))
operacion = input("Elige una operación (+, -, *, /): ")


#Operación
if operacion == "+":
    print(f"Resultado: {num1} + {num2} = {num1 + num2}")
elif operacion == "-":
    print(f"Resultado: {num1} - {num2} = {num1 - num2}")
elif operacion == "*":
    print(f"Resultado: {num1} * {num2} = {num1 * num2}")
elif operacion == "/":
    if num2 != 0:
        print(f"Resultado: {num1} / {num2} = {num1 / num2}")
    else:
        print("Error: No se puede dividir entre cero.")
else:
    print("Operación no válida.")

#Juego de adivinanza
import random

numero_secreto = random.randint(1, 100)

print("¡Bienvenido al juego de adivinanza!")
print("Adivina un número entre 1 y 100.")

while True:
    
    adivinanza = int(input("Ingresa tu número: "))

    if adivinanza == numero_secreto:
        print("¡Felicidades! Adivinaste el número.")
        break 
    elif adivinanza < numero_secreto:
        print("El número es mayor. Intenta de nuevo.")
    else:
        print("El número es menor. Intenta de nuevo.")

