"""
Docstring for understanding_while_loop_centinel

    Un programa que:
        -Cuenta cuantos numeros a ingresado el usuario.
        -realice la suma de estos numeros.
        -Me diga cual es el minimo de los numeros ingresados.
        -Me diga cual es el maximo de los numeros ingresados.
"""
counter = 0
sum_quiantities = 0.0
minimun = None
maximum = None



while True:
    print("Escribe Exit para salir")
    user_input = input("Ingresa una cantidad (MXN):")

    if user_input == "Exit":
            break
    
    try:
          value = float(user_input)
    except ValueError:
          print("caracter invalido. Por favor ingresa un numero")
          continue
    except KeyboardInterrupt:
          print("salida manual")
          break
    counter += 1 #counter = counter + 1
    sum_quiantities += value    #sum_quiantities = sum_quiantities + value(sumador)

    if minimun is None or value <minimun:
          minimun = value
    if  minimun is None or value <maximum:
          maximum = value
          
print("cantidaad de numeros ingresados:")
print("suma de cantidades:", sum_quiantities)
print("minima cantida:", minimun)
print("maxima cantidad:", maximum)
