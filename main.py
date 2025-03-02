"""
    Esta funcion nos permite calcular las operaciones basicas de dos numeros enteros o flotantes
    primero mostramos las opciones disponibles
    despues, calculamos el resultado
    y por ultimo lo imprimimos en pantalla
"""

def calculadora():
    #mostramos las opciones
    print("Seleccione la operaciC3n:")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")

    #inicializamos la variable (la creamos y guardamos el valor)
    opcion = input("Ingrese el nC:mero de la operaciC3n (1/2/3/4): ")

    #segun la opcion escogido realizamos la operacion
    if opcion in ("1", "2", "3", "4"):

        #ingresamos los numeros
        num1 = float(input("Ingrese el primer nC:mero: "))
        num2 = float(input("Ingrese el segundo nC:mero: "))

        #realizamos la operacion y mostramos en la consola
        if opcion == "1":
            print(f"Resultado: {num1} + {num2} = {num1 + num2}")
        elif opcion == "2":
            print(f"Resultado: {num1} - {num2} = {num1 - num2}")
        elif opcion == "3":
            print(f"Resultado: {num1} * {num2} = {num1 * num2}")
        elif opcion == "4":
            if num2 != 0:
                print(f"Resultado: {num1} / {num2} = {num1 / num2}")
            else:
                print("Error: No se puede dividir entre cero.")
    else:
        print("OpciC3n invC!lida. IntC)ntelo de nuevo.")


# Ejecutar solo si el script se ejecuta directamente
if __name__ == "__main__":
    calculadora()