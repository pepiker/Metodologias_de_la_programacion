
# Fibonacci code


n = input("escribe el limite que deses:")
if not n.isdigit():
    print("Error numero nomvalido.")
    if n < 1 or n > 50:
        print("numero novalido")    
        exit()
    else:
        fuibonacci_serie = []
        a, b = 0, 1
        contador = 0
        contador < n
        fuibonacci_serie.append(a)
        a, b = b, a + b
        contador += 1
        print("Number of terms:", n)
        print("Fibonacci series:", " ".join(str[p] for p in fuibonacci_serie))
