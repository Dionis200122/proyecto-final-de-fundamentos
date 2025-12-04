def mostrar_menu():
    print("\n==============================")
    print("   BIENVENIDO A LA CALCULADORA")
    print("==============================")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    print("==============================")

def sumar():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    resultado = a + b
    print(f"El resultado de la suma es: {resultado}")

def restar():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    resultado = a - b
    print(f"El resultado de la resta es: {resultado}")

def multiplicacion():
    a = float(input("Ingrese el primer numero: "))
    b = float(input("Ingrese el segundo numero: "))
    resultado = a * b
    print(f"El resultado de la multiplicacion es: {resultado}")

def division():
     a = float(input("Ingrese el primer numero: "))
     b = float(input("Ingrese el segundo numero: "))
     
if b != 0: # type: ignore
        resultado = a / b # type: ignore
        print("El resultado de la division es:", resultado)

else:
        print("Error: no se puede dividir entre cero")

while True:
    mostrar_menu()
    opcion = input("Seleccione una opcion (1-3): ")

    if opcion == "1":
        sumar()
    elif opcion == "2":
        restar()
    elif opcion == "3":
        print("Gracias por usar la calculadora. ¡Hasta luego!")
        break
    else:
        print("Opcion invalida, por favor elija 1, 2 o 3.")
