# Definir función
# LAGRANGE
def lagrange(x_datos, y_datos, x_eval):
    """Evalúa el polinomio interpolador de Lagrange en un punto dado.

    [PARÁMETROS]
    ----------
    x_datos : list[float]
        Lista de coordenadas en X de los puntos conocidos (sin valores repetidos).
    y_datos : list[float]
        Lista de coordenadas en Y correspondientes a cada punto.
    x_eval : float
        Punto en el cual se desea estimar el valor interpolado.

    [RETORNA]
    -------
    float
        Valor estimado P(x_eval).

    [EXCEPCIONES]
    -----------
    ValueError
        Si las listas están vacías, tienen distinta longitud o existen valores de X repetidos.

    [EJEMPLO]
    -------
    >>> lagrange([0, 1, 2], [1, 3, 2], 1.5)
    2.875
    """
    
    if len(x_datos) != len(y_datos) or len(x_datos) == 0:
        raise ValueError("[ERROR] LAS LISTAS DE DATOS DEBEN TENER LA MISMA LONGITUD Y NO ESTAR VACÍAS")

    n = len(x_datos)
    resultado = 0.0

    for i in range(n):
        termino = 1.0
        for j in range(n):
            if i != j:
                if x_datos[i] == x_datos[j]:
                    raise ValueError("[ERROR] LOS VALORES DE 'x' NO PUEDEN REPETIRSE")

                termino *= (x_eval - x_datos[j]) / (x_datos[i] - x_datos[j])
        
        resultado += y_datos[i] * termino

    return resultado