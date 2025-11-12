"""
    Las listas tambien pudesn almacenar
    numeros y de hecho, son ideales para esto.
    python ofrece una gran cantidad de herramientas
    que ayudan a trabajar eficientemente
    con listas de numeros.

"""

# Metodo built-in range()
"""
    El metodo range() genera una serie de numeros
    en un rango especifico.

    Por ejemplo, range(1, 10) generara los numeros
    del 1 al 9.

"""
print("numeros del 0 al 9")
for value in range(10): # 10 genera numeros del 0 al 9
    print(value)


print("numeros del 1 al 9")
for value in range(1, 10): # 10 genera numeros del 1 al 9
    print(value)
odd_numbers = list(range(1, 10, 2)) 
print(odd_numbers)

print("numeros impares del 1 al 9")
for value in range(1, 10, 2): # 10 genera numeros del 1 al 9 con paso de 2
    print(value)
numeros_impares = list(range(1, 10, 2))
print(numeros_impares)


print("numeros pares del 2 al 10")
for value in range( 0, 10, 2): # 10 genera numeros entre 0 y 10 con paso de 2
    print(value)
numeros_pares = list(range(0, 10, 2))
print(numeros_pares)

print("tabla del 9")
for value in range( 0, 91, 9): # genera numeros entre 0 y 90 con paso de 9
    print(value)
table_of_9 = list(range(0, 91, 9))
print(table_of_9)




# cuadrado de los primeros 10 numeros

squares = []
for number in range(1, 11):
    square = number ** 2
    squares.append(square)
print(squares)

# Mas metodos built-in 
#metodo min()
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits)) # salida: 0

#metodo max()
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(max(digits)) # salida: 9

#metodo sum()
digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(sum(digits)) # salida: 45

