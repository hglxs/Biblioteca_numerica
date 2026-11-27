# Importar librería
from biblioteca_numerica import NewtonRaphson

def f(x):
    return x**3 - x - 2

def df(x):
    return 3*x**2 - 1

ejemplo_newton = NewtonRaphson(f, df, 1e-8, 50)
ejemplo_resultado = ejemplo_newton.resolver(1.5)
print("\n=== NEWTON - RAPHSON ===")
print(ejemplo_resultado)