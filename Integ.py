import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

f_str = input("Ingrese la función: ").replace(" ", "")

f = sp.sympify(f_str)

integral_definida = input("La integral es definida? (S/N): ").lower() == 's'

if integral_definida:
    a = float(input("Ingrese el límite inferior de integración: "))
    b = float(input("Ingrese el límite superior de integración: "))

x = sp.symbols('x')
if integral_definida:
    integral = sp.integrate(f, (x, a, b))
else:
    integral = sp.integrate(f, x)

with open("procedimiento.txt", "w") as archivo:
    archivo.write(str(integral))

f_lambdify = sp.lambdify(x, f, "numpy")
xs = np.linspace(-10, 10, 500)
ys = f_lambdify(xs)

plt.plot(xs, ys, label="Función original")

if integral_definida:
    ys_fill = f_lambdify(np.linspace(a, b, 500))
    plt.fill_between(np.linspace(a, b, 500), ys_fill, alpha=0.3, label="Región bajo la curva")

if integral_definida:
    valor_integral = sp.integrate(f, (x, a, b)).evalf()
else:
    valor_integral = sp.integrate(f, x).evalf()

plt.legend(title=f"Valor de la {'integral definida' if integral_definida else 'integral indefinida'}: {valor_integral}")

plt.savefig("grafica.png")

with open("procedimiento.txt", "r") as archivo:
    procedimiento = archivo.read()

imagen = Image.open("grafica.png")
imagen.show()
print(f"Procedimiento:\n{procedimiento}")
