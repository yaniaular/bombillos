Distribucion de bombillos.
==========================

El script bombillos.py lee un archivo matriz.txt. En el repositorio hay una
carpeta ejemplo con un archivo de entrada de prueba de una matriz.

El archivo con la matriz de entrada es pasado por argumento. (Ver como se ejecuta más abajo)

Teniendo esa matriz de entrada, se procede a buscar todas las soluciones
posibles para el problema de la distribución de bombillos y se escoje la más óptima. 
Por ejemplo, si la solución más óptima a la matriz es usar 4 bombillos, entonces 
el algoritmo mostrará todas las posibles combinaciones donde se usen 4 bombillos.

La razón por la cual se utilizó listas para alumbrar y matrix de numpy para
contar es porque al revisar los tiempos con cProfile, me di cuenta que era más
rápido de esta forma, cuando intenté hacerlo todo con numpy no me dió buenos
resultados.

Se utilizó programación dinámica y se almacenó los caminos que ya se
recorrieron, se almacenan en set() ya que son muchísimos más rápidos
que las listas cuando se utliza el operador IN.

Está hecho con Python 3.6.9. para ejecutarlo se usa:

*$ python3 bombillos.py matrix.txt*

- **B**: Las habitaciones que tienen bombillo.
- **L**: Las habitaciones que tienen luz por algun bombillo.
- **1**: Las habitaciones con paredes.
