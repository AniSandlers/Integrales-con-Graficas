#En la primera línea, importamos las librerías necesarias
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from sympy.parsing.sympy_parser import (parse_expr, standard_transformations, implicit_multiplication_application)

# Pedimos la función al usuario
func_str = input("Ingrese la función: ")

# Convertimos la cadena a una expresión de SymPy
transformations = (standard_transformations + (implicit_multiplication_application,))
f = parse_expr(func_str, transformations=transformations)

# Preguntamos si la integral es definida o indefinida
es_definida = input("La integral es definida? (si/no): ")

if es_definida == "si":
    # Pedimos los límites de integración al usuario
    a = float(input("Ingrese el límite inferior: "))
    b = float(input("Ingrese el límite superior: "))
    # Calculamos la integral definida de la función
    integral = sp.integrate(f, (sp.Symbol('x'), a, b))
    # Mostramos la solución con procedimiento y resultado en una imagen
    sp.preview(sp.Eq(sp.Integral(f, (sp.Symbol('x'), a, b)), integral), viewer='file', filename='solucion.png', euler=False)
    # Imprimimos el resultado de la integral definida
    print(f"La integral definida de {f} en el intervalo [{a}, {b}] es {integral.evalf()}")
else:
    # Calculamos la integral indefinida de la función
    integral = sp.integrate(f, sp.Symbol('x'))
    # Mostramos la solución con procedimiento y resultado en una imagen
    sp.preview(sp.Eq(sp.Integral(f, sp.Symbol('x')), integral), viewer='file', filename='solucion.png', euler=False)
    # Imprimimos el resultado de la integral indefinida
    print(f"La integral indefinida de {f} es {integral}")

# Graficamos la función y su integral
x = sp.symbols('x')
f_lambdify = sp.lambdify(x, f, "numpy")
integral_lambdify = sp.lambdify(x, integral, "numpy")
xs = np.linspace(-10, 10, 500)
ys_f = f_lambdify(xs)
ys_integral = integral_lambdify(xs)

#Esto nos ayuda a graficar.
plt.plot(xs, ys_f, label="Función original")
plt.plot(xs, ys_integral, label="Integral")
plt.legend()
plt.show()
