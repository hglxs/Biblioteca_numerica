# Clase "ResultadoNumerico" (Práctica 3 • Actividad 2)
class ResultadoNumerico:
    """Almacena y formatea la bitácora de ejecución de un método numérico.

    [PARÁMETROS]
    ----------
    metodo : str
        Nombre del método numérico ejecutado.
    """

    def __init__(self, metodo):
        self.metodo = metodo
        self.iteraciones = []
        self.convergio = False
        self.mensaje = ""

    def agregar_iteraciones(self, numero, aproximacion, error):
        empaquetar = {'Número': numero, 'Aproximación': aproximacion, 'Error': error}
        self.iteraciones.append(empaquetar)

    def ultima_aproximacion(self):
        if len(self.iteraciones) == 0:
            return None
        else:
            return self.iteraciones[-1]['Aproximación']

    def __str__(self):
        if len(self.iteraciones) == 0:
            return f"{self.metodo}: NO SE HA REALIZADO NINGUNA ITERACIÓN"
        else:
            return f"Método: {self.metodo}\nTotal Iteraciones: {len(self.iteraciones)}\nConvergió: {self.convergio}\nMensaje: {self.mensaje}"

