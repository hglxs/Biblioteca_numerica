# Importar biblioteca
from biblioteca_numerica import regresion_lineal

x_datos = [1, 2, 3, 4, 5]
y_datos = [2.1, 3.9, 6.2, 7.8, 10.1]

ejemplo_regresion = regresion_lineal(x_datos, y_datos)
print("\n=== REGRESIÓN LINEAL ===")
print(ejemplo_regresion)