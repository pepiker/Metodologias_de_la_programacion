# trabajo con lista 

"""
rrecorrer una lista sin importar la cantidad de elemntos que tenga

"""
magicians = ["rom", "hermion", "harry"]

print(magicians[0], magicians[1], magicians[2])

for magician in magicians:
    print(magician)
    print(magician.upper())
    print(f"{magician.title()} ese es un gran hechizo.")
    print(f"{magician.title()} no podemos esperar para ver tu siguiente hechizo.")


print("Gracias a todos, fue un gran espectaculo!")

"""
 identacion en python

 python utiliza la identacion para determinar
 cuando una lista de codigo esta conectada a 
 la linea de codigo anterior.

 basicamente, se utilizan espacios en blanco para
 obligarnos a escribir un codigo ordenado y estructurado.

"""

# No olvides la identacion en python

magicians = ["alicia", "david", "carolina"]
for magician in magicians:
    print(magician)
    print(f"I cant wait to see your next trick, {magician.title()}.") 


# Identacion innecesaria
message = "Hello Python world!"
print(message)

