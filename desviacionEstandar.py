import math


# Excepción personalizada
class NoSePuedeCalcular(Exception):
    pass


# Función para calcular el promedio
def calcular_promedio(elementos):
    if len(elementos) == 0:
        raise NoSePuedeCalcular("No se puede calcular el promedio de una lista vacía")

    # Verificar si todos los elementos son numéricos
    for elemento in elementos:
        if not isinstance(elemento, (int, float)):
            raise TypeError("Todos los elementos deben ser numéricos")

    # Calcular promedio
    return sum(elementos) / len(elementos)


# Función para calcular la desviación estándar
def calcular_desviacion_estandar(elementos):
    if len(elementos) == 0:
        raise NoSePuedeCalcular("No se puede calcular la desviación estándar de una lista vacía")

    # Verificar si todos los elementos son numéricos
    for elemento in elementos:
        if not isinstance(elemento, (int, float)):
            raise TypeError("Todos los elementos deben ser numéricos")

    if len(elementos) == 1:
        return 0  # La desviación estándar de un solo elemento es 0

    # Calcular la media
    media = calcular_promedio(elementos)

    # Calcular la suma de las diferencias al cuadrado
    suma_diferencias_cuadradas = sum((x - media) ** 2 for x in elementos)

    # Calcular la desviación estándar
    return math.sqrt(suma_diferencias_cuadradas / len(elementos))

