cars = ['audi','bmw', 'chevrolet','corvette','tesla']
for car in cars:
        if car == 'bmw' or car == 'tesla' or car == 'audi':
            print(car.upper())
        else:
            print(car)

# Condicionales : El condicional es el corazon de un if
# Condicional true 

car = 'bmw'
print (car == 'bmw') # True


car_2 = 'Audi'
print (car_2.lower() == 'audi') # True

# Condicional false

car_2 = 'Audi'
print (car_2 == 'audi') # False

#condicional != para determinar desiguldad

requested_topping = 'mushrooms' #-> string
if requested_topping != 'anchovies': # -> True
    print("Hold the anchovies!")


# Condicionales numericos

age = 18 #-> int
print(age == 18) # True

answer = 17
if answer != 42: # -> True
    print("That is not the correct answer. Please try again!")
age = 19 
print(age < 21) # True
print(age <= 21) # True
print(age > 21) # False
print(age >= 21) # False

# Multiples condicionales

