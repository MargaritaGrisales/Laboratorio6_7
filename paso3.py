#Parte 1
estudiantes = ["Camilo", "Santiago", "Sebastian", "Laura", "Nathalia"]

print("Lista de estudiantes:")
for estudiante in estudiantes:
    print(estudiante)

#Parte 2
contacto = {
    "Nombre": "Camilo",
    "Correo": "camilo@example.com"
}

print("\nInformación de contacto:")
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")
    
#Parte 3

while True:
    nuevo_estudiante = input("\nIngresa un nombre para agregar a la lista (o escribe 'salir' para terminar): ")
    if nuevo_estudiante.lower() == "salir":
        break
    estudiantes.append(nuevo_estudiante)
    print(f"{nuevo_estudiante} ha sido agregado a la lista.")

# Actualizar el diccionario
nuevo_correo = input("\nIngresa un nuevo correo para Camilo: ")
contacto["Correo"] = nuevo_correo
print("\nDiccionario actualizado:")
for clave, valor in contacto.items():
    print(f"{clave}: {valor}")

