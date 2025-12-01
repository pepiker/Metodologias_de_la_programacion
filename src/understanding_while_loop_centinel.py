"""
Docstring for understanding_while_loop_centinel

    Un programa que:
        -Cuenta cuantos numeros a ingresado el usuario.
        -realice la suma de estos numeros.
        -Me diga cual es el minimo de los numeros ingresados.
        -Me diga cual es el maximo de los numeros ingresados.
"""
a=0
b=1

while True:
    n=input("escribe el rango que deceas:")
    if n <1 or n > 50:
        print("ingresa un numero valido")
    else:
        for i in range(0,n):
            print(a)
            a,b=b , b+a
            
            print(fibonacci_serie)
            break
print("Error numero no valido")
