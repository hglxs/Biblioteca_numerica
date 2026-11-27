# Definir funciones
# ERROR ABSOLUTO
def error_abs(valor_real, aproximacion):
    """Calcula el error absoluto entre un valor real y su aproximación

    [PARÁMETROS]
    --------------------------
    valor_real : float
        Valor exacto o de referencia
    aproximacion : float
        Valor estimado por el método numérico

    [RETORNA]
    --------------------------
    float
        Diferencia positiva |valor_real - aproximacion|

    [EJEMPLO]
    --------------------------
    >>> error_absoluto(10, 9.5)
    0.5
    """
    
    return abs(valor_real - aproximacion)

# ERROR RELATIVO
def error_rel(valor_real, aproximacion):
    """Calcula el error relativo entre un valor real y su aproximación, dividido entre el valor real

    [PARÁMETROS]
    --------------------------
    valor_real : float
        Valor exacto o de referencia (debe ser distinto de cero)
    aproximacion : float
        Valor estimado por el método numérico
    
    [RETORNA]
    --------------------------
    float
        Error relativo |valor_real - aproximacion| / |valor_real|

    [EXCEPCIONES]
    --------------------------
    ValueError
        Si 'valor_real' es igual a cero

    [EJMEPLO]
    --------------------------
    >>> error_relativo(10. 95)
    0.05
    """
    if valor_real == 0:
        raise ValueError("[ERROR] EL VALOR REAL NO PUEDE SER CERO PARA CALCULAR EL ERROR RELATIVO")
    else:
        return error_abs(valor_real, aproximacion) / abs(valor_real)