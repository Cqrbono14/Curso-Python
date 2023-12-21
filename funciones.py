# Funciones arriba

def suma(number1, number2):
    resultado = number1 + number2
    print("El resultado de la suma es:", resultado)

def sumaConRetorno(number1, number2):
    resultado = number1 + number2
    return resultado

# Llamada abajo

print("Suma funcion sin retorno")
suma(2, 3)

print("Suma funcion con retorno")
resultado = sumaConRetorno(2, 5)
print("El resultado de la suma es:", resultado)
