frutas = ["manzana", "banana", "cereza"]

print("Frutas disponibles:")
for fruta in frutas:
    print(fruta)

print(frutas[0])
print(frutas[1])
print(frutas[2])

alumnos = []

alumno1 = input("Ingresa el nombre del primer alumno: ")
alumno2 = input("Ingresa el nombre del segundo alumno: ")
alumno3 = input("Ingresa el nombre del tercer alumno: ")
almuno4 = input("Ingresa el nombre del cuarto alumno: ")
alumno5 = input("Ingresa el nombre del quinto alumno: ")

alumnos.append(alumno1)
alumnos.append(alumno2) 
alumnos.append(alumno3)
alumnos.append(almuno4)
alumnos.append(alumno5)

print("Lista de alumnos:")
print(alumnos)

# ACTUALIZAMOS CON UN NUEVO ALUMNO PARA LA POSICION 2
alumnos.insert(1, input("Ingrese el nombre del nuevo alumno para la posicion 2: "))
print(alumnos)

alumnos.pop(1) # ELIMINAMOS EL ALUMNO QUE ESTABA EN LA POSICION 2a


print("Lista actualizada de alumnos:")
print(alumnos)