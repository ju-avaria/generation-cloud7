frutas = ["manzana", "banana", "cereza"]

for fruta in frutas:
    print(fruta)


verduras = [
    {"nombre": "zanahoria", "precio": 1.5, "cantidad": 10},
    {"nombre": "lechuga", "precio": 1.0, "cantidad": 5},
    {"nombre": "espinaca", "precio": .5, "cantidad": 8}
]


total_ventas = 0.0
for verdura in verduras:
    total_ventas += verdura["precio"] * verdura["cantidad"]
    print(verdura["nombre"])


print("Calculando el total de ventas...")
print("Total de ventas: $", total_ventas)


# while (True):
#     entrada = input("Escribe 'salir' para terminar el bucle: ")
#     if entrada.lower() == "salir":
#         print("Saliendo del bucle...")
#         break
#     else:
#         print("Has escrito:", entrada)

frutas = []
while True:
    nombre = input("Ingresa el nombre de la fruta que deseas buscar (o 'salir' para terminar): ").capitalize()

    if nombre.lower().strip() == "salir":
        print("Saliendo del programa...")
        break

    precio = float(input("Ingresa el precio de la fruta: "))
    print("Has ingresado:", nombre)
    print("Precio:", precio)


    fruta = {"nombre": nombre, "precio": precio}
    frutas.append(fruta)   

print("**** Ticket de compra ****")
for fruta in frutas:
    print("Producto:", fruta["nombre"], "- Precio:", fruta["precio"]) 




