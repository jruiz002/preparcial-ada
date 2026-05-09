# Soluciones: Ejercicios 5 y 6

## Ejercicio 5 — Selección de Estructura de Datos

**1. Estructuras de datos y justificación:**
Usaría una combinación de un **Hash Map** y un **Árbol Binario de Búsqueda Balanceado**, o en su defecto, un **Skip List**.
- **Mapa Hash:** Almacena el `ID_del_jugador` como clave y un puntero al nodo correspondiente en la estructura ordenada como valor. Esto otorga acceso estructurado e instantáneo al registro del jugador.
- **Árbol Balanceado / Skip List:** Almacena los pares `(Puntaje, ID_del_jugador)` ordenados de mayor a menor. Esto mantiene los puntajes siempre ordenados, lo que permite extraer el Top 10 rápidamente en cualquier momento.

**2. Complejidad temporal:**
- **Actualización de puntaje:** $O(\log N)$, donde $N$ es la cantidad total de jugadores. Buscar el jugador en el Hash Map toma $O(1)$. Luego, eliminar su puntaje viejo del árbol o skip list toma $O(\log N)$ e insertar su nuevo puntaje toma $O(\log N)$.
- **Consulta del Top-10:** $O(1)$ (o estrictamente $O(K)$ donde $K=10$). Solamente requiere leer los primeros 10 nodos ordenados de la estructura. Al ser un límite fijo independiente de $N$, se considera en tiempo constante.

**3. Tradeoff introducido y cómo manejarlo:**
- **Tradeoff (Compromiso):** Mantener un árbol perfectamente balanceado para cientos de miles de usuarios actualizando su puntaje varias veces por segundo puede causar contención alta de bloqueos en memoria y alto consumo de CPU.
- **Mitigación:** Usaría batching de actualizaciones. En lugar de procesar cada pequeño cambio individual a la estructura principal en tiempo real, acumularía el puntaje modificado de cada jugador en memoria caché y actualizaría el árbol central periódicamente (ej. cada 1 segundo). Para un videojuego, una consistencia eventual con medio segundo de retraso en el Top 10 general es imperceptible para el humano, y alivia enormemente la carga del servidor.

## Ejercicio 6 — Selección de Algoritmo (App de Navegación)

**1. Algoritmo y justificación:**
Usaría el algoritmo A*.
- **Por qué encaja:** A* es ideal para el "Pathfinding" o búsqueda de rutas en grafos geográficos. A diferencia de otros algoritmos que buscan en todas direcciones ciegas, A* utiliza una aproximación heurística (generalmente la distancia en línea recta entre la posición actual y el destino final) para dirigir la búsqueda focalizada hacia el objetivo, resolviéndolo rapidísimo para el tamaño dado de 50,000 nodos y 120,000 aristas.

**2. Manejo de pesos cambiantes (tráfico/incidentes):**
- Los "pesos" del grafo se mantendrían en memoria y serían actualizados asíncronamente en segundo plano a medida que varíen los datos de tráfico. 
- Para que A* encuentre siempre el camino más rápido, la heurística elegida debe seguir siendo "admisible" (es decir, no debe sobrestimar el costo real). Por ejemplo, asumiendo siempre la velocidad máxima de la vía sin ningún obstáculo como heurística a futuro. Así, cada nueva ruta o recalculo constante utilizará instantáneamente los nuevos pesos actualizados sin tener que recalcular interacciones completas desde cero.

**3. Alternativa considerada y descartada:**
- **Alternativa:** El clásico algoritmo de **Dijkstra** (o esquemas precalculados todos-contra-todos como Floyd-Warshall).
- **Por qué se descartó:** Floyd-Warshall toma $O(V^3)$ lo cual es intratable y excesivo para mapas grandes dinámicos. En el caso de Dijkstra, se descartó porque Dijkstra no utiliza heurísticas; explora en un anillo radial expansivo y evaluaría carreteras en dirección contraria al objetivo. Cuando miles de conductores piden rutas en paralelo, la ineficiencia de Dijkstra frente a rutas dirigidas colapsaría el sistema en comparación.