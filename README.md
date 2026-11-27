# PRÁCTICA 4 • Creación de una biblioteca propia
## • Objetivo 
Paquete en Python que implementa métodos numéricos fundamentales para el cálculo de errores, búsqueda de raíces, interpolación polinomial y regresión lineal.

## • Estructura
~~~text
Practica_04/
├── biblioteca_numerica/
│   ├── __init__.py
│   ├── errores.py          # Cálculo de error absoluto y relativo
│   ├── interpolacion.py    # Interpolación polinomial de Lagrange
│   ├── raices.py           # Métodos de Newton-Raphson y de la Secante
│   ├── regresion.py        # Ajuste por mínimos cuadrados (regresión lineal)
│   ├── resultados.py       # Clase ResultadoNumerico para bitácoras de ejecución
│   └── validaciones.py     # Funciones auxiliares de validación de entradas
├── ejemplos/
│   ├── ejemplo_lagrange.py
│   ├── ejemplo_newton.py
│   └── ejemplo_regresion.py
├── pruebas/
│   └── test_biblioteca.py  # Pruebas unitarias con assert
├── main.py
└── README.md
~~~

## • Requisitos
* **Lenguaje:** Python 3.8 o superior
* **Dependencias externas:** Ninguna. El paquete está construido exclusivamente con la biblioteca estándar de Python (`math`), por lo que no requiere instalar `numpy` ni `scipy`.

## • Forma de importación
Para utilizar el paquete, sitúate en la carpeta raíz del proyecto (`Práctica_04`) e importa directamente las funciones o clases desde `biblioteca_numerica`:
~~~python
from biblioteca_numerica import (
    error_abs,
    error_rel,
    NewtonRaphson,
    MetodoSecante,
    lagrange,
    regresion_lineal,
    ResultadoNumerico,
)
~~~

Si ejecutas scripts ubicados dentro de subcarpetas (como `ejemplos/` o `pruebas/`), hazlo desde la raíz usando la bandera `-m` para que Python resuelva las rutas correctamente:
~~~bash
python3 -m ejemplos.ejemplo_newton
python3 -m pruebas.test_biblioteca
~~~

## • Ejemplo mínimo
~~~python
from biblioteca_numerica import NewtonRaphson, lagrange, regresion_lineal

# 1. Búsqueda de raíz para f(x) = x^3 - x - 2
metodo = NewtonRaphson(lambda x: x**3 - x - 2, lambda x: 3*x**2 - 1, tolerancia=1e-8)
resultado = metodo.resolver(1.5)
print(resultado)

# 2. Interpolación de Lagrange en x = 1.5
y_est = lagrange([0.0, 1.0, 2.0], [1.0, 3.0, 2.0], 1.5)
print(f"Valor interpolado: {y_est}")

# 3. Regresión lineal simple
m, b = regresion_lineal([1, 2, 3, 4], [2, 4, 6, 8])
print(f"Recta ajustada: y = {m}x + {b}")
~~~

## • Métodos disponibles
* **Cálculo de errores (`errores.py`)**:
    * `error_abs(valor_real, aproximacion)`: Calcula la diferencia absoluta $|v_{real} - v_{aprox}|$
    * `error_rel(valor_real, aproximacion)`: Calcula el error relativo $\frac{|v_{real} - v_{aprox}|}{|v_{real}|}$

* **Búsqueda de raíces (`raices.py`)**:
    * `NewtonRaphson(funcion, derivada, tolerancia=1e-6, max_iteraciones=100)`: Encuentra raíces mediante tangentes sucesivas usando su método `.resolver(x0)`.
    * `MetodoSecante(funcion, tolerancia=1e-6, max_iteraciones=100)`: Encuentra raíces sin requerir derivada analítica mediante `.resolver(x0, x1)`.

* **Interpolación (`interpolacion.py`)**:
    * `lagrange(x_datos, y_datos, x_eval)`: Evalúa el polinomio interpolador de Lagrange de grado $n-1$ en el punto `x_eval`.

* **Ajuste de curvas (`regresion.py`)**:
    * `regresion_lineal(x_datos, y_datos)`: Calcula la pendiente $m$ y la ordenada al origen $b$ de la recta $y=mx+b$ por mínimos cuadrados.

* **Gestión de resultados (`resultados.py`)**:
    * `ResultadonNumerico(metodo)`: Estructura el historial de iteraciones, estado de convergencia y resumen formateado de los métodos iterativos.

## • Límitaciones conocidas
* **Derivada manual en Newton-Raphson**: El usuario debe proporcionar explícitamente la función derivada $f'(x)$; el paquete no realiza diferenciación simbólica ni numérica automática.
* **Sensibilidad a valores iniciales**: Tanto `NewtonRaphson` como `MetodoSecante` pueden divergir o detenerse con error si se eligen puntos iniciales lejanos a la raíz o si la derivada/pendiente se vuelve cero durante las iteraciones.
* **Oscilación en interpolación de alto grado**: Al usar polinomios globales de Lagrange con muchos puntos equidistantes, pueden presentarse oscilaciones pronunciadas en los extremos (fenómeno de Runge).
* **Ajuste únicamente lineal**: El módulo de regresión solo ajusta modelos lineales de primer grado ($y = mx + b$); no soporta regresión polinomial ni multivariable.
* **Estructuras de datos nativas**: Las funciones operan sobre listas estándar de Python (`list`) y valores escalares (`float`/`int`), por lo que no están optimizadas para procesamiento vectorizado de grandes volúmenes de datos.
