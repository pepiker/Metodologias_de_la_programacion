# Fibonacci Series with Python ;)

"""
  
Antes del código, agrega algo como (en comentarios):

Problem: Fibonacci series generator  
Description: Program that reads an integer n and prints the first n terms of the Fibonacci series starting at 0 and 1.  

Inputs:  
- n (int; number of terms to generate)  

Outputs:  
- "Fibonacci series:" followed by the n terms separated by spaces or commas  

Validations:  
- n must be an integer  
- n must be >= 1  
- (Optional) n must be <= 50  

Test cases:  
1) Normal: n = ... → expected series: ...  
2) Border: n = ... → expected series: ...  
3) Error: n = ... → expected message: "Error: invalid input"

"""
# La serie de Fibonacci es una secuencia donde cada número
#  es la suma de los dos anteriores (0, 1, 1, 2, 3, 5...).
# “Calcular la serie hasta n términos” significa generar 
# exactamente n valores empezando desde 0 y 1.

# Este programa leerá el valor de n, verificará que sea un 
# entero válido y dentro del rango permitido.
# Si la validación se cumple, generará la serie de Fibonacci
#  usando un ciclo y mostrará los n términos en pantalla.

# Programa: Serie de Fibonacci con validaciones

user_input = input("Enter number of terms: ")

# Validación 1: ¿Se puede convertir a entero?
try:
    n = int(user_input)
except ValueError:
    print("Error: invalid input")
    exit()

# Validación 2: ¿n >= 1?
if n < 1:
    print("Error: invalid input")
    exit()

# Validación 3 (opcional): limitar a 50 términos
if n > 50:
    print("Error: invalid input")
    exit()

# Si pasa las validaciones, generamos la serie
fib = []

if n >= 1:
    fib.append(0)
if n >= 2:
    fib.append(1)

# Generar términos a partir del 3ro
for i in range(2, n):
    siguiente = fib[-1] + fib[-2]
    fib.append(siguiente)

# Imprimir salida
print("Fibonacci series:", " ".join(str(num) for num in fib))


#CONCLUSION

# El uso de un bucle facilitó generar la serie porque permitió construir
# cada término a partir de los anteriores.

# Manejar correctamente los casos n = 1 y n = 2 es importante para evitar
# errores y asegurar que la serie inicie correctamente.

# Esta lógica puede reutilizarse en otros programas que necesiten cálculos
# secuenciales, acumulativos o basados en valores previos.

# Además, sirve como base para funciones matemáticas, algoritmos de 
# optimización o simulaciones que dependan de iteraciones controladas.

# References:
# 1) Python Documentation – "for" and "while" Statements: https://docs.python.org/3/tutorial/controlflow.html
# 2) Python Fibonacci Tutorials – Real Python / W3Schools: explicación de listas y generación de secuencias.
# 3) Apuntes de clase de Programación (Unidad: Estructuras de control y ciclos).

"""
  Casos de prueba 
  
1) (.vnv) PS C:\Users\iker misael\tarea charly> py '.\Fibonacci_Series_with_Python .py'
Number of terms: 0
Error: invalid input
2)
(.vnv) PS C:\Users\iker misael\tarea charly> py '.\Fibonacci_Series_with_Python .py'
Number of terms: 6
Fibonacci series: 0 1 1 2 3 5
 3) 
(.vnv) PS C:\Users\iker misael\tarea charly> py '.\Fibonacci_Series_with_Python .py'
Number of terms: 1
Fibonacci series: 0

"""