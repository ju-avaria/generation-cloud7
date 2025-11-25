def mensaje_bienvenida():
    print("¡Bienvenido a nuestro programa!")


def saludo(nombre, edad):
    total_dias = cuenta_dias_con_edad(edad)
    print(f"Hola, {nombre}! que bueno tenerte de regreso , tienes {total_dias} días de vida.")


def cuenta_dias_con_edad(edad):
    dias_totales = edad * 365
    return dias_totales
mensaje_bienvenida()
saludo("Carlos" , 32)




