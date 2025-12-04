"""

   Alumno: Iker Misael Zapata Ortega
   Matricula: 2530077
"""

# Los tipos int y float representan números enteros y números con decimales,
# respectivamente, y permiten realizar operaciones matemáticas según la precisión
# necesaria. Los booleanos (True/False) indican si una condición es verdadera y
# se obtienen principalmente a partir de comparaciones como ==, >, < o >=. Validar
# rangos numéricos es esencial para evitar errores lógicos y cálculos inválidos,
# incluyendo la división entre cero, que produce fallos en la ejecución. Este
# documento incluye la descripción de cada problema, el diseño de entradas y
# salidas, las validaciones utilizadas y el uso adecuado de enteros, flotantes
# y valores booleanos para controlar el flujo del programa y tomar decisiones seguras.


"""
# 7.1 Problem 1: Temperature converter and range flag
# ==================================================
# Description:
# Converts Celsius temperature to Fahrenheit and Kelvin, and determines
# a high temperature flag when temp_c >= 30.0.
# Inputs: temp_c (float)
# Outputs: Fahrenheit, Kelvin, High temperature flag
# Validations: temp_c must be float and Kelvin >= 0.0
"""

try:
    temp_c = float(input("Enter temperature in Celsius: "))
    temp_k = temp_c + 273.15
    if temp_k < 0.0:
        print("Error: invalid input")
    else:
        temp_f = temp_c * 9/5 + 32
        is_high_temperature = (temp_c >= 30.0)
        print("Fahrenheit:", temp_f)
        print("Kelvin:", temp_k)
        print("High temperature:", is_high_temperature)
except:
    print("Error: invalid input")

"""
    1) Normal Case (temperatura válida)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Enter temperature in Celsius: 25
Fahrenheit: 77.0
Kelvin: 298.15
High temperature: False

2) Border Case (cerca del límite, alta temperatura)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Enter temperature in Celsius: 30
Fahrenheit: 86.0
Kelvin: 303.15
High temperature: True

3) Error Case (entrada inválida)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Enter temperature in Celsius: hola
Error: invalid input

"""

"""
# ==================================================
# 7.2 Problem 2: Work hours and overtime payment
# ==================================================
# Description:
# Calculates weekly payment including overtime.
# Inputs: hours_worked (float), hourly_rate (float)
# Outputs: Regular pay, Overtime pay, Total pay, Overtime flag
# Validations: hours_worked >= 0, hourly_rate > 0
# Test cases:
#  Normal: hours_worked=38, rate=100 -> no overtime
#  Border: hours_worked=40 -> exact limit
#  Error: hours_worked=-5 -> Error
"""

try:
    hours_worked = float(input("Hours worked: "))
    hourly_rate = float(input("Hourly rate: "))

    if hours_worked < 0 or hourly_rate <= 0:
        print("Error: invalid input")
    else:
        overtime_hours = max(0.0, hours_worked - 40.0)
        regular_hours = min(hours_worked, 40.0)
        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
        has_overtime = (hours_worked > 40.0)

        print("Regular pay:", regular_pay)
        print("Overtime pay:", overtime_pay)
        print("Total pay:", total_pay)
        print("Has overtime:", has_overtime)
except:
    print("Error: invalid input")

"""
    1) Normal Case (empleado con horas extra)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Hours worked: 45
Hourly rate: 100
Regular pay: 4000.0
Overtime pay: 750.0
Total pay: 4750.0
Has overtime: True

2) Border Case (justo 40 horas, sin horas extra)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Hours worked: 40
Hourly rate: 80
Regular pay: 3200.0
Overtime pay: 0.0
Total pay: 3200.0
Has overtime: False

3) Error Case (entrada inválida: horas negativas)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Hours worked: -5
Hourly rate: 100
Error: invalid input

"""
"""
# ==================================================
# 7.3 Problem 3: Discount eligibility
# ==================================================
# Description:
# Determines if the customer gets discount based on student/senior flag
# or purchase total.
# Inputs: purchase_total (float), texts YES/NO
# Outputs: Discount flag, final total
# Test cases:
#  Normal: total=1200, NO, NO -> discount
#  Border: total=1000, NO, NO -> discount
#  Error: text="MAYBE" -> Error
"""

try:
    purchase_total = float(input("Purchase total: "))
    is_student_text = input("Student (YES/NO): ").strip().upper()
    is_senior_text = input("Senior (YES/NO): ").strip().upper()

    if purchase_total < 0.0:
        print("Error: invalid input")
    elif is_student_text not in ("YES", "NO") or is_senior_text not in ("YES", "NO"):
        print("Error: invalid input")
    else:
        is_student = (is_student_text == "YES")
        is_senior = (is_senior_text == "YES")

        discount_eligible = is_student or is_senior or (purchase_total >= 1000.0)
        final_total = purchase_total * 0.9 if discount_eligible else purchase_total

        print("Discount eligible:", discount_eligible)
        print("Final total:", final_total)
except:
    print("Error: invalid input")

"""

1) Normal Case (estudiante con descuento)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Purchase total: 500
Student (YES/NO): YES
Senior (YES/NO): NO
Discount eligible: True
Final total: 450.0

2) Border Case (no es estudiante ni senior, pero compra >= 1000)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Purchase total: 1000
Student (YES/NO): NO
Senior (YES/NO): NO
Discount eligible: True
Final total: 900.0

3) Error Case (entrada inválida en YES/NO)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Purchase total: 300
Student (YES/NO): maybe
Senior (YES/NO): NO
Error: invalid input
"""
"""
# ==================================================
# 7.4 Problem 4: Basic statistics of three integers
# ==================================================
# Description:
# Reads 3 integers and outputs sum, average, max, min, and even flag.
# Test cases:
#  Normal: 2,4,6 -> all even
#  Border: 1,2,3 -> not all even
#  Error: "a",2,3 -> Error
"""

try:
    n1 = int(input("Enter integer 1: "))
    n2 = int(input("Enter integer 2: "))
    n3 = int(input("Enter integer 3: "))

    sum_value = n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1, n2, n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print("Sum:", sum_value)
    print("Average:", average_value)
    print("Max:", max_value)
    print("Min:", min_value)
    print("All even:", all_even)
except:
    print("Error: invalid input")
"""
1) Normal Case (tres enteros válidos)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Enter integer 1: 4
Enter integer 2: 7
Enter integer 3: 2
Sum: 13
Average: 4.333333333333333
Max: 7
Min: 2
All even: False

2) Border Case (todos pares)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Enter integer 1: 2
Enter integer 2: 4
Enter integer 3: 6
Sum: 12
Average: 4.0
Max: 6
Min: 2
All even: True

3) Error Case (entrada no numérica)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Enter integer 1: hola
Error: invalid input


"""
"""
# ==================================================
# 7.5 Problem 5: Loan eligibility
# ==================================================
# Description:
# Determines loan eligibility based on income, debt ratio, and credit score.
# Test cases:
#  Normal: income 10000, debt 2000, score 700 -> eligible
#  Border: income 8000, debt 3200, score 650 -> eligible
#  Error: income 0 -> Error
"""

try:
    monthly_income = float(input("Monthly income: "))
    monthly_debt = float(input("Monthly debt: "))
    credit_score = int(input("Credit score: "))

    if monthly_income <= 0 or monthly_debt < 0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)

        print("Debt ratio:", debt_ratio)
        print("Eligible:", eligible)
except:
    print("Error: invalid input")

"""
1) Normal Case (datos válidos para ser elegible)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Monthly income: 9000
Monthly debt: 3000
Credit score: 700
Debt ratio: 0.3333333333333333
Eligible: True


2) Border Case (caso límite: justo NO elegible)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Monthly income: 8000
Monthly debt: 3300
Credit score: 650
Debt ratio: 0.4125
Eligible: False


3) Error Case (entrada inválida)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Monthly income: hola
Error: invalid input

"""
"""
# ==================================================
# 7.6 Problem 6: BMI and category flag
# ==================================================
# Description:
# Calculates BMI and determines category flags.
# Test cases:
#  Normal: 70kg, 1.75m -> normal
#  Border: BMI=18.5 -> normal
#  Error: height=0 -> Error
"""

try:
    weight_kg = float(input("Weight (kg): "))
    height_m = float(input("Height (m): "))

    if weight_kg <= 0 or height_m <= 0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_r = round(bmi, 2)

        is_underweight = (bmi < 18.5)
        is_normal = (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0)

        print("BMI:", bmi_r)
        print("Underweight:", is_underweight)
        print("Normal:", is_normal)
        print("Overweight:", is_overweight)
except:
    print("Error: invalid input")
"""
1) Normal Case (BMI dentro del rango normal)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Weight (kg): 70
Height (m): 1.75
BMI: 22.86
Underweight: False
Normal: True
Overweight: False


2) Border Case (caso límite → sobrepeso mínimo)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Weight (kg): 80
Height (m): 1.75
BMI: 26.12
Underweight: False
Normal: False
Overweight: True


3) Error Case (entrada inválida)
PS C:\Users\iker misael\pyton_proyects\Metodologias_de_la_programacion> python .\src\Manejo_de_números_y_booleanos_en_Python.py
Weight (kg): hola
Error: invalid input


"""
# --------------------------------------------------
# 8. CONCLUSIONES
# --------------------------------------------------
# En estos ejercicios se observa cómo los enteros y flotantes trabajan juntos
# para resolver problemas reales, desde cálculos simples hasta operaciones
# financieras. Las comparaciones permiten generar valores booleanos, los
# cuales son esenciales para tomar decisiones con estructuras if. También se
# refuerza la importancia de validar rangos y evitar errores como divisiones
# entre cero o datos inválidos. Además, el uso de condiciones combinadas con
# and, or y not permite crear reglas más precisas y realistas. Finalmente,
# se reconoce que estos patrones de validación y decisión se repiten en
# problemas comunes como nóminas, descuentos, préstamos o evaluaciones.


# --------------------------------------------------
# References
# --------------------------------------------------
# - Python Official Docs: https://docs.python.org/3/
# - Class Notes