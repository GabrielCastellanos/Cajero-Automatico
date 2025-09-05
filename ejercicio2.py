# Se definen los usuarios y contraseñas válidas
user_one = "Gabriel Castellanos"
password_one = "uzumaki naruto123"
user_two = "Claudia Sheinbaum"
password_two = "cuarta transformacion"

# Se establece el número máximo de intentos
intentos = 3

# Mensaje de bienvenida
print("\n--- Inicio de Sesión ---")

# El bucle se ejecuta mientras queden intentos
while intentos > 0:
    print(f"\nTe quedan {intentos} intentos.")
    
    # 1. Se piden los datos DENTRO del bucle para permitir reintentos
    user = input("Introduzca el nombre de usuario: ")
    password = input("Introduzca la contraseña: ")

    # 2. Se comprueba si alguno de los campos está vacío (error de autentificación)
    if user == "" or password == "":
        print("Error de autentificación: Ambos campos son obligatorios.")
        intentos -= 1 # Se resta un intento por el error
        continue # Vuelve al inicio del bucle para el siguiente intento

    # 3. Se comprueban las combinaciones correctas de usuario y contraseña
    if (user == user_one and password == password_one) or \
       (user == user_two and password == password_two):
        print("\n✅ ¡Enhorabuena! Has iniciado sesión correctamente.")
        break # Si es correcto, se rompe el bucle y termina el programa

    # 4. Si la combinación no fue correcta, se verifica si el usuario existe para dar un error específico
    elif user != user_one and user != user_two:
        print("Error: El usuario no existe. Intenta de nuevo.")
        intentos -= 1 # Se resta un intento
    
    # 5. Si el usuario existe pero la contraseña no coincidió, se da otro error
    else:
        print("Error: Contraseña incorrecta. Intenta de nuevo.")
        intentos -= 1 # Se resta un intento

# 6. Si el bucle termina porque se acabaron los intentos, se muestra este mensaje
if intentos == 0:
    print("\nHas superado el número máximo de intentos. Acceso bloqueado.")