# Challenge Software Engineer Backend

Para el Challenge Software Engineer Backend, se utilizo los siguientes paquetes de pip for Python 3.8.10:

    * Requests -> 2.27.1
    * Pytest -> 7.1.1

Las funciones para cada pregunta se encuentran en el script `functions.py`.

    * Pregunta 1 -> names_with_at_and_double_a
    * Pregunta 2 -> breed_pokemons
    * Pregunta 3 -> get_max_and_min_weight

**Nota:**

Para la pregunta 1, se tomo en cuneta lo siguiente:
    
    * Se considero los nombre que contengan 2 at ya que no especifica cuantas veces debe aparecer, y este el limitado por el numero de 2 a.
    ejemplo:

        * "raticate" --> contiene 2 'at' en su nombre y 2 'a', por lo tanto se considera.
        * "patrat" --> contiene 2 'at' en su nombre y 2 'a', por lo tanto se considera.

    ya que el enunciado de la pregunta no especifica que debe ser un unico 'at'.

## Resultados

1. Para ver los resultados debe clonar el repositorio
2. intalar las dependencias que se encuentran en `requirements.txt`, usando el comando 
```
pip install -r requirements.txt
```

## Comandos
1. para ver los 3 resultados (primera segunda y tercera pregunta), correr el comando:
```
python3 functions.py
```
2. para ver el resultado de cada pregunra por separado, correr el comando:

pregunta 1:
```
python3 exercise.py 1
```
pregunta 2:
```
python3 exercise.py 2
```
pregunta 3:
```
python3 exercise.py 3
```

3. Para correr los tests, correr el comando:
```
pytest
```