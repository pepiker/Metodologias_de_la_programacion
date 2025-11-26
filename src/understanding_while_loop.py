# Wile

"""
    El while es un circulo controlado/comando
    por condicion.

    La estructura basica de un wile es:

    wilw conditional:
        action


"""

# While infinito
"""
    Programa si el usuario ingresa un numero 
    entre el 25 y 50, entonces esta dentro del rango
    y salirme del while,
    de otro modo pedirle que ingrese otro numero.
"""
while True:
    try:
        number = int(input("ingresa el numero:"))

        if number > 10 and number <= 20:
            print("Estas en el rango, lo hiciste bien")
            break
        else:
            print("Esta fuera de el rango, ingresa otro numero.")

    except ValueError:
        print("se ha introducido una variable no valida")
    except KeyboardInterrupt:
        print("\nprograma terminado por el usuario.")
        break

print("saliste del while jupi")
