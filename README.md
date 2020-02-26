Distribucion de bombillos.
==========================

El script bombillos.py lee un archivo matriz.txt. En el repositorio hay una
carpeta ejemplo con un archivo de entrada de prueba de una matriz.

Si se desea cambiar la matriz a leer, se puede modificar la línea 21 en el
script bombillos.py.

Teniendo esa matriz de entrada, se procede a buscar todas las soluciones
óptimas para el problema de la distribución de bombillos. Por ejemplo, si la
solución más óptima a la matriz es usar 4 bombillos, entonces el algoritmo
mostrará todas las posibles combinaciones donde se usen 4 bombillos.

La razón por la cual se utilizó listas para alumbrar y matrix de numpy para
contar es porque al revisar los tiempos con cProfile, me di cuenta que era más
rápido de esta forma, cuando intenté hacerlo todo con numpy no me dió buenos
resultados.

Está hecho con Python 3.6.9. para ejecutarlo se usa:

*$ python3 bombillos.py*

- **B**: Las habitaciones que tienen bombillo.
- **L**: Las habitaciones que tienen luz por algun bombillo.
- **1**: Las habitaciones con paredes.
