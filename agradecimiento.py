def frase(nombre, apellido):
    return f"Hola {nombre} {apellido}, gracias por ver este repositorio."

nombre = input("Ingrese su nombre: ")
apellido = input("Ingrese su apellido: ")

frase_resultante = frase(nombre, apellido)

print(frase_resultante)