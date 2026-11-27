# Definir función
# REGRESIÓN LINEAL
def regresion_lineal(x_datos, y_datos):
    """Ajusta una recta y = mx + b mediante el método de mínimos cuadrados.

    [PARÁMETROS]
    ----------
    x_datos : list[float]
        Lista de valores de la variable independiente X.
    y_datos : list[float]
        Lista de valores de la variable dependiente Y.

    [RETORNA]
    -------
    tuple[float, float]
        Tupla (m, b) con la pendiente y la ordenada al origen de la recta ajustada.

    [EXCEPCIONES]
    -----------
    ValueError
        Si hay menos de dos puntos, las longitudes no coinciden o todos los valores de X son iguales.

    [EJEMPLO]
    -------
    >>> regresion_lineal([1, 2, 3], [2, 4, 6])
    (2.0, 0.0)
    """

    if len(x_datos) != len(y_datos) or len(x_datos) < 2:
        raise ValueError("[ERROR] SE NECESITAN AL MENOS DOS PARES DE PUNTOS (x, y) DE LA MISMA LONGITUD")

    n = len(x_datos)

    suma_x = sum(x_datos)
    suma_y = sum(y_datos)
    suma_xy = sum(x * y for x, y in zip(x_datos, y_datos))
    suma_x2 = sum(x ** 2 for x in x_datos)

    denominador_m = n * suma_x2 - (suma_x ** 2)

    if denominador_m == 0:
        raise ValueError("[ERROR] DIVISIÓN ENTRE CERO. NO SE PUEDE CALCULAR LA PENDIENTE (valores de 'x' idénticos)")

    m = (n * (suma_xy) - (suma_x * suma_y)) / denominador_m

    b = (suma_y - (m * suma_x)) / n

    return m, b