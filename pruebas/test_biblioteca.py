# Importar librerías
from biblioteca_numerica import (
    error_abs,
    error_rel,
    lagrange,
    regresion_lineal,
    NewtonRaphson
)

# >>> Prueba 1. Cálculo exacto de errores (caso normal). 
def test_errores():
    assert error_abs(10, 9.5) == 0.5, "EL ERROR ABSOLUTO DEBERÍA DE SER IGUAL A '0.5'"
    assert error_rel(10, 9.5) == 0.05, "EL ERROR RELATIVO DEBERÍA SER IGUAL A '0.05'"

# >>> Prueba 2. Propiedad fundamental de Lagrange en un nodo (caso normal). 
def test_lagrange_en_nodo():
    x_datos = [0.0, 1.0, 2.0, 3.0, 4.0]
    y_datos = [1.0, 1.58, 3.56, 6.23, 10.56]
    x_evaluar = 2.0

    resultado = lagrange(x_datos, y_datos, x_evaluar)
    assert abs(resultado - 3.56) < 1e-9, f"[ERROR] LAGRANGE EN EL NODO 'x = 2.0' DEBIÓ DAR 3.56, PERO DIO {resultado}"

# >>> Prueba 3. Ajuste exacto en regresión lineal (caso normal). 
def test_regresion_lineal():
    x_datos = [1, 2, 3, 4]
    y_datos = [5, 8, 11, 14]
    pendiente, ordenada = regresion_lineal(x_datos, y_datos)

    assert abs(pendiente - 3.0) < 1e-9, f"[ERROR] LA PENDIENTE DEBIÓ SER 3.0, PERO SE OBTUBO {pendiente}"
    assert abs(ordenada - 2.0) < 1e-9, f"[ERROR] LA ORDENADA AL ORIGEN DEBIÓ SER 2.0, PERO SE OBTUVO {ordenada}"

# >>> Prueba 4. Convergencia de raíces (caso normal). 
def test_convergencia_newton():
    f = lambda x: x**2 - 4
    df = lambda x: 2 * x

    newton = NewtonRaphson(f, df, 1e-8)
    resultado = newton.resolver(3.0)

    assert resultado.convergio is True, f"[NO CONVERGIÓ]"
    assert abs(resultado.ultima_aproximacion() - 2.0) < 1e-6, f"[ERROR] LA RAÍZ DEBIÓ SER ~2.0, PERO SE OBTUVO {resultado.ultima_aproximacion()}"

# >>> Prueba 5. Manejo de excepciones ante entradas y salidas (casos de error). 
def test_casos_errores():
    try:
        prueba_errores = error_rel(0, 5)
        assert False, "Debió lanzar ValueError"
    except ValueError:
        pass

# >>> Main del programa
if __name__ == "__main__":
    test_errores()
    test_lagrange_en_nodo()
    test_regresion_lineal()
    test_convergencia_newton()
    test_casos_errores()

    print("[TODAS LAS PRUEBAS PASARON EXITOSAMENTE]")