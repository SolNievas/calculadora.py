from os import system
from datetime import date
import platform
autor = ("Sol")
hoy = date.today()
so = platform.system()

if so == ("Linux"):
    s = ("clear")
else:
    s = ("cls")
    system (s)

print ("Autor: " f"{autor}".center(50,"*"))
print ("Fecha: " f"{hoy}".center(50,"*"))
print ("Calculadora".center(50,"*").upper())

num1 = int(input(" Ingrese 1° número: "))
num2 = int(input("Ingrese 2° número: "))

resultado = int(num1) + int(num2)
print(f"la suma es: ", {resultado})

resultado = int(num1) - int(num2)
print(f"la resta es: ", {resultado})

resultado = int(num1) * int(num2)
print(f"la multiplicacion es: ", {resultado})

resultado = int(num1) / int(num2)
print(f"el producto es: ", {resultado})

resultado = int(num1) // int(num2)
print(f"el cociente entero es: ", {resultado})

resultado = int(num1) ** int(num2)
print(f"el exponencial es: ", {resultado})

resultado = int(num1) % int(num2)
print(f"el resto de la division es: ", {resultado})



