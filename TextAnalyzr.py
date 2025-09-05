texto = input("Ingresa un texto cualquiera: ")
letras = []
texto = texto.lower()

print("Acontinuacion ingrese 3 letras de su eleccion: ")

letras.append(input("Ingrese la primera letra: ").lower())
letras.append(input("Ingrese la segunda letra: ").lower())
letras.append(input("Ingrese la tercera letra: ").lower())

print("\n")
print("La cantidad de letras son: ")

cantidad_de_letras1 = texto.count(letras[0])
cantidad_de_letras2 = texto.count(letras[1])
cantidad_de_letras3 = texto.count(letras[2])

print(f"Se encontraron '{letras[0]}' repetida {cantidad_de_letras1} veces")
print(f"Se encontraron '{letras[1]}' repetida {cantidad_de_letras2} veces")
print(f"Se encontraron '{letras[2]}' repetida {cantidad_de_letras3} veces")

print("\n")
print("Cantidad de palabras: ")

palabras = texto.split()
print(f"Se encontraron un total de {len(palabras)} palabras en el texto que ingreso")

print("\n")
print("Primer letra y ultima letra: ")

letra_inicio = texto[0]
letra_final = texto[-1]

print(f"La letra inicial es '{letra_inicio}' y la letra final es '{letra_final}'")

print("\n")
print("Texto invertido")

palabras.reverse()
texto_invertido = ' '.join(palabras)
print(f"Tu texto invertido dira: '{texto_invertido}' ")

print("\n")
print("Python esta aqui?")

buscar_python = 'python' in texto
dic = {True:"si",False:"no"}

print(f"La palabra 'Python' {dic[buscar_python]} se encuentra en el texto")
