# Importar clases
from .resultados import ResultadoNumerico
from .validaciones import validar_tolerancia, validar_iteraciones

# Clase "NewtonRaphson" (Práctica 3 • Actividad 3)
class NewtonRaphson:
    """Implementación del método numérico de Newton-Raphson para encontrar raíces.

    [PARÁMETROS]
    ----------
    funcion : callable
        Función matemática f(x) a la que se le busca la raíz.
    derivada : callable
        Primera derivada f'(x) de la función.
    tolerancia : float, opcional
        Criterio de parada basado en el error entre iteraciones (por defecto 1e-6).
    max_iteraciones : int, opcional
        Número máximo de iteraciones permitidas (por defecto 100).

    [EXCEPCIONES]
    -----------
    ValueError
        Si `tolerancia <= 0` o `max_iteraciones <= 0`.
    """

    def __init__(self, funcion, derivada, tolerancia=1e-6, max_iteraciones=100):
        validar_tolerancia(tolerancia)
        validar_iteraciones(max_iteraciones)

        self.funcion = funcion
        self.derivada = derivada
        self.tolerancia = tolerancia
        self.max_iteraciones = max_iteraciones
        
    def resolver(self, x0):
        """Ejecuta el algoritmo a partir de una estimación inicial.

        [PARÁMETROS]
        ----------
        x0 : float
            Valor inicial para comenzar las iteraciones.

        [RETORNA]
        -------
        ResultadoNumerico
            Objeto con el historial de iteraciones, estado de convergencia y mensaje final.
        """

        resultado = ResultadoNumerico("Newton-Raphson")
        x_actual = x0

        for i in range (self.max_iteraciones):
            valor_derivado = self.derivada(x_actual)

            if abs(valor_derivado) < 1e-12:
                resultado.mensaje = "ERROR: DERIVADA CERCANA A CERO"
                break

            x_nuevo = x_actual - (self.funcion(x_actual) / valor_derivado)
            error = abs(x_nuevo - x_actual)

            resultado.agregar_iteraciones(i, x_actual, error)

            x_actual = x_nuevo

            if error < self.tolerancia:
                resultado.convergio = True
                resultado.mensaje = "RAÍZ ENCONTRADA EXITOSAMENTE"
                break

        if not resultado.convergio and not resultado.mensaje:
            resultado.mensaje = "SE ALCANZÓ EL MÁXIMO DE ITERACIONES SIN CONVERGER"

        return resultado

class MetodoSecante:
    """Implementación del método de la Secante para encontrar raíces sin requerir derivada.

    [PARÁMETROS]
    ----------
    funcion : callable
        Función matemática f(x) a la que se le busca la raíz.
    tolerancia : float, opcional
        Criterio de parada basado en el error entre iteraciones (por defecto 1e-6).
    max_iteraciones : int, opcional
        Número máximo de iteraciones permitidas (por defecto 100).

    [EXCEPCIONES]
    -----------
    ValueError
        Si `tolerancia <= 0` o `max_iteraciones <= 0`.
    """
    
    def __init__(self, funcion, tolerancia = 1e-1, max_iteraciones = 100):
        validar_tolerancia(tolerancia)
        validar_iteraciones(max_iteraciones)

        self.funcion = funcion
        self.tolerancia = tolerancia
        self.max_iteraciones = max_iteraciones

    def resolver(self, x0, x1):
        """Ejecuta el algoritmo a partir de dos estimaciones iniciales.

        [PARÁMETROS]
        ----------
        x0 : float
            Primer punto inicial.
        x1 : float
            Segundo punto inicial.

        [RETORNA]
        -------
        ResultadoNumerico
            Objeto con el historial de iteraciones, estado de convergencia y mensaje final.
        """

        resultado = ResultadoNumerico("Método de la Secante")
        x_anterior = x0
        x_actual = x1

        for i in range(self.max_iteraciones):
            f_actual = self.funcion(x_actual)
            f_anterior = self.funcion(x_anterior)

            if abs(f_actual - f_anterior) < 1e-12:
                resultado.mensaje = "[ERROR]: División por cero (f(x1) - f(x0) es casi cero)"
                break

            x_nuevo = x_actual - (f_actual * (x_actual - x_anterior) / (f_actual - f_anterior))
            error = abs(x_nuevo - x_actual)

            resultado.agregar_iteraciones(i, x_actual, error)

            x_anterior = x_actual
            x_actual = x_nuevo

            if error < self.tolerancia:
                resultado.convergio = True
                resultado.mensaje = "RAÍZ ENCONTRADA EXITOSAMENTE"
                break

        if not resultado.convergio and not resultado.mensaje:
            resultado.mensaje = "SE ALCANZÓ EL MÁXIMO DE ITERACIONES SIN CONVERGER"

        return resultado