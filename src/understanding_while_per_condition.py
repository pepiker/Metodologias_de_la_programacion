"""
    vamos a realizar un programa que defina un pin 
    para acceso de usuario.

    El usuario tendra un maxiomo de intenos, para
    colocar bien el pin.

    Si el usuario sobrepasa el maximo de intentos 
    se le va a bloquear la cuenta y el acceso
"""

CORRECT_PIN = "1234"
MAX_ATTEMPTS =  3
attempt = 0

while attempt < MAX_ATTEMPTS:

    user_input = input("ingresa tu pin:")

    if user_input == CORRECT_PIN:
        print("Acceso concedido")
        break
    else:
        attempt+=1
        reaming_attemps = MAX_ATTEMPTS - attempt
        if reaming_attemps > 0:
            print("ingresaste un pin no valido")
            print(f"te quedam {reaming_attemps} intentos")
        else:
            print("cuenta bloqueada")