# try:
#     numero = int(input("Ingrese un número: "))
#     print(f"El número ingresado es: {numero}")
# except:
#     print("Error: Debe ingresar un número entero válido.")


# try:
#     numero = int(input("Ingrese un número: "))
#     print(f"El número ingresado es: {numero}")
#     resultado = numero / 5
#     print(f"El resultado de dividir el número entre 5 es: {resultado}")
# except:
#     print("Error: Ocurrió un problema al procesar el número.")

# def validar_edad(edad):
#     if edad < 0:
#         raise ValueError("La edad no puede ser negativa.")
#     return edad

# validar_edad(int(input("Ingrese su edad: ")) )

def validar_email(email):
    if "@" not in email or "." not in email:
        raise ValueError("El correo electrónico no es válido.")
    else:
        print("Correo electrónico válido.", email )
        return email

validar_email(input("Ingrese su correo electrónico: "))