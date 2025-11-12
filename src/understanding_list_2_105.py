"""
    Slicing a list
"""
players = ["charles", "martina", "michael", "florence", "eli"]
print("listaoriginal:", players)

print("silice de lista oriinal", players[0:3])
print("silice de lista oriinal", players[1:4])
print("silice de lista oriinal", players[:4])
print("silice de lista oriinal", players[2:])
print("silice de lista oriinal", players[-3:])
print("silice de lista oriinal", players[5:2])
print("silice de lista oriinal", players[-3:-1])


"""
    slicing en un for
"""

players = ["charles","martina","michael","florence", "eli" ]
print("aqui se precentan los primeros 3 jugadores del equipo")
for player in players[0:3]:
    print(player.title())

"""
    Copiando una lista

"""
my_food = ["pizza", "tacos", 'flautas', 'gorditas']

#my_foods_copy = my_foods #Error: esta no es la manera correcta de copiar una lista
my_food = ["pizza",]
my_food = my_food
my_food_1 = my_food [:]
my_foods_2 = my_food.copy()
my_foods_3 = list(my_food)

 