alien_0 = {"color": "yellow"}
print(alien_0["color"])

# Modyfying values in a dictionary
alien_0["color"] = "bleue"
print(alien_0["color"])

# Adding new elements to a dictionary
alien_0["x_position"] = 0
alien_0["y_position"] = 25
alien_0["name"] = "paul"
print (alien_0)

# Lopping through items in a dictionary
print("\nLopping through keys:")
for key, value in alien_0.items():
    print(f"Key: {key} has value : {value}")
    print("\nLopping through keys:")

# Looping through keys
for key in alien_0.keys():
    print(f"Key: {key}")

# Looping through values
print("\nLopping through values:")
for value in alien_0.values():
    print(f"Value: {value}")

# diccionarios en diccionarios

convenant_grunt = {
    "color": "orange",
    "weapon": "plasma-gun",
    "armament": "plasma-granade",
    "health": 2,

}

convenant_elite = {
    "color": "green",
    "weapon": "plasma-gun",
    "armament": "plasma-granade",
    "health": 75,

}


convenant_jackal = {
    "color": "gray",
    "weapon": "plasma-gun",
    "armament": "plasma-granade",
    "health": 5,

}

convenants = [
    convenant_grunt,
    convenant_elite,
    convenant_jackal
    ]

for convenant in convenants:
    print("\n", convenant)
    for key, value in convenant.items():
        print(f"{key}: {value}")

#listas de diccionarios
students = {
    "santiago": ["reprobado", "prepa 1", "rebelde"],
    "jorge-crack": ["aprobado", "cbtis-271", "goleador"],
    "gabriel": ["aprobado", "119muerte", "crack-fortnite"]

}

#diccionarios en diccionarios 

sensors = {
    "temperature": {
        "id": "temp_1",
        "location": "aula 105",
        "value": 25,
        "unit": "celsius",
    },
    "humidity": {
        "id": "hum_1",
        "location": "aula 103",
        "value": 60,
        "unit": "porcentaje",
    }

}

print("Temperatura")
print(sensors["humidity"]["value"])
print("ubicacion")
print(sensors["humidity"]["location"])

#Estudiar el metodo get() de los diccionarios
