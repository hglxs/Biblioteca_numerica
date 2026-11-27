# Definir funciones
# VALIDACIÓN DE TOLERANCIA
def validar_tolerancia(tol):
    if tol < 0:
        raise ValueError("[ERROR] LA TOLERANCIA NO PUEDE SER NEGATIVA")

# VALIDACIÓN DE ITERACIONES
def validar_iteraciones(max_iteraciones):
    if max_iteraciones <= 0:
        raise ValueError("[ERROR] EL MÁXIMO DE ITERACIONES DEBE SER MAYOR QUE CERO")