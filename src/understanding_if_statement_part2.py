age = 0

try:
    age = int(input("escribe tu edad:"))
except:
    age = -1
    print("Error, ingresaste un valor no valido")

# bloque if-elif-else
if age > 100:
    print("Tienes mas de un siglo")
elif age >= 18 and age <= 100:
    print("Eres mayor de edad")
elif age >= 0 and age < 18:
    print("Eres menor de edad")
else:
    print("Tuviste un error")
   
print("hola charly")


"""
    Hacer un programa que pregunte la edad de una persona 
    y responda lo siguiente
    -si la edad es menor a 4, entonces la entrada es gratuita
    -si la entrada es menor a 18, pero mayor a 4
    entnces la entrada cuest $200
    -si la edad es mayor o igual que 18, entonces la entrada 
    cuesta $400

"""
try:
    age = 0
    age = int(input("escribe tu edad:"))
except:
    age = -1 
    print("Error, ingresaste un valor no valido")
if age >= 0 and age <= 4:
        print("Tu entrada es gratuita")
elif age > 4 and age < 18:
    print("tu entrada cuesta $200")
elif age >= 18:
    print("tu entrada cuesta $400")
else:
    print("Tuviste un error")


   
print("hola charly")

