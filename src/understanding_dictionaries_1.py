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

    