from sympy import *
import matplotlib.pyplot as plt
import numpy as np

# Función para imprimir paso a paso la solución de una integral y graficar la función
def paso_a_paso_integracion():
    # Paso 1: Solicitar la función a integrar y la variable
    funcion = input("Ingrese la función a integrar: ")
    variable = input("Ingrese la variable respecto a la que se integra: ")
    funcion = sympify(funcion)
    variable = Symbol(variable)

    # Paso 2: Obtener la integral de la función
    integral = integrate(funcion, variable)

    # Paso 3: Imprimir la integral
    print("Paso 1: Integración de la función")
    print(f"∫ {funcion} d{variable} = {integral}")

    # Paso 4: Calcular la constante de integración
    c = symbols('c')
    solucion = integral + c

    # Paso 5: Imprimir la constante de integración
    print("Paso 2: Calcular la constante de integración")
    print(f"La solución general es: {solucion}")

    # Paso 6: Graficar la función original y su integral
    x = np.linspace(-10, 10, 1000)
    f = lambdify(variable, funcion, "numpy")
    plt.plot(x, f(x), label="Función original")
    F = lambdify(variable, integral, "numpy")
    plt.plot(x, F(x), label="Integral")
    plt.legend()
    plt.show()

    # Paso 7: Resolver la constante de integración si se especifican los límites
    limites = input("¿Los límites de integración son definidos? (s/n): ")
    if limites == "s":
        limite_inferior = input("Ingrese el límite inferior: ")
        limite_superior = input("Ingrese el límite superior: ")

        # Paso 8: Evaluar la constante de integración en los límites dados
        solucion_definida = solucion.subs(variable, limite_superior) - solucion.subs(variable, limite_inferior)

        # Paso 9: Imprimir la solución definida
        print("Paso 3: Solución de la integral definida")
        print(f"La solución de la integral definida de {funcion} d{variable} entre {limite_inferior} y {limite_superior} es: {solucion_definida}")

    else:
        print("Paso 3: Solución de la integral indefinida")
        print("La solución es una constante arbitraria (c) más la solución general")        

# Ejemplo de uso
paso_a_paso_integracion()
