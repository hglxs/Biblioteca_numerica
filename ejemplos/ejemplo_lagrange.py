# Importar librería
from biblioteca_numerica import lagrange

x_datos = [0.0, 1.0, 2.0, 3.0]
y_datos = [1.0, 2.7183, 7.3891, 20.0855]
x_evaluar = 1.5

ejemplo_lagrange = lagrange(x_datos, y_datos, x_evaluar)
print("\n=== LAGRANGE ===")
print(ejemplo_lagrange)