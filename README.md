#  ¿Cómo funciona c/u en la implementación (incluyendo todas las funciones y clases utilizadas)?
- Búsqueda en Anchura (BFS):
BFS utiliza una cola para explorar cada nivel de un árbol antes de pasar al siguiente, asegurando que la primera solución encontrada es la más cercana al punto de partida. El algoritmo inicia en el nodo raíz y, si cumple con la condición de objetivo, detiene la búsqueda y retorna el camino hacia la solución. De lo contrario, expande el nodo generando "hijos" (movimientos posibles en el puzzle) y coloca cada hijo en la cola, explorándolos en el orden en que se generaron. Además, evita repetir estados ya visitados.

- Búsqueda en Profundidad (DFS):
DFS explora completamente un camino del árbol antes de retroceder para explorar otras rutas. Funciona con una pila, lo que permite una búsqueda profunda. Se establece un límite de 30 niveles para evitar caminos excesivamente largos o ciclos infinitos. Al alcanzar este límite sin encontrar una solución, el algoritmo abandona esa rama. Cada nodo explorado se registra en una lista, y sus hijos se agregan a la pila solo si no han sido visitados antes.

- Búsqueda Greedy:
Este algoritmo elige los nodos que minimizan la distancia heurística hacia el objetivo, empleando la distancia de Manhattan como una medida de la cercanía al objetivo. Evalúa cada nodo en función de su valor heurístico, priorizando la expansión del nodo con menor distancia estimada. Una vez encontrado el objetivo, proporciona el camino de solución y cuenta los nodos explorados.

- Búsqueda A*:
A* utiliza una combinación de la heurística de la distancia de Manhattan y el costo acumulado hasta el nodo actual. De este modo, se priorizan los nodos con el menor costo total estimado (heurística + costo) en la cola de prioridad, lo que permite una búsqueda eficiente que garantiza encontrar la solución óptima.

# Para determinar si un juego se puede o no resolver, dice en la implementación que el número de inversiones debería ser par, ¿porqué? ¿cómo funciona de manera detallada este mecanismo?
Esta regla existe porque los movimientos en el rompecabezas solo cambian el orden de a dos piezas a la vez (la que mueves y la vacía), lo que no cambia si el número de inversiones es par o impar de manera sencilla. Así, si se comienza con un número par de inversiones, siempre podrás llegar al orden correcto.
Es decir, si las piezas están revueltas en un orden con número par de inversiones, el juego es resoluble. Pero si el número de inversiones es impar, el desorden no te deja llegar al objetivo, no importa cuánto intentes.
En resumen, solo podemos resolver el rompecabezas cuando el desorden es par. Cuando el desorden es impar, simplemente no alcanza con los cambios de a dos para ordenarlo todo.

