# Utilizando varias listas

guisos_disponibles = ["salsa verde", "desebrada", "desebarada", "mole"]
guisos_a_ordenar = ["desebrada", "caldo de iguana"]

print("que giso deses ordenar?")
for guiso in guisos_a_ordenar:
    print(f"deseo{guiso}")
    if guiso in guisos_disponibles:
        print(f"si tenemos{guiso}")
    else:
        print("no tenemos de ese guiso")
print("realizando pedido...")
