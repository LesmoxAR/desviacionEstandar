# Promedio y Desviación Estándar - Test Driven Development (TDD)

Este proyecto consiste en una aplicación en Python que calcula el promedio y la desviación estándar de una lista de números enteros. El desarrollo se ha realizado siguiendo la metodología de **Test Driven Development (TDD)** y utilizando pruebas unitarias para garantizar la corrección del código.

## Requisitos

1. La aplicación contiene una lista llamada `elementos`, que almacena números.
2. Calcula el promedio y la desviación estándar de los elementos de la lista.
3. Se han implementado pruebas unitarias para validar los siguientes casos:
    - Lista vacía.
    - Un solo elemento.
    - Dos elementos.
    - Elementos positivos y negativos.
    - Todos los elementos son ceros.
    - Elementos no numéricos (lanza una excepción).

## Estructura del proyecto

El proyecto está dividido en dos archivos principales:

- **`desviacionEstandar.py`**: Contiene la lógica de cálculo del promedio y la desviación estándar, junto con las excepciones necesarias.
- **`test_desviacionEstandar.py`**: Contiene las pruebas unitarias para validar el correcto funcionamiento de la aplicación.
