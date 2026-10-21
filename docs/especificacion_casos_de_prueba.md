# Laboratorio 04 — Especificación de casos de prueba

## Código bajo prueba (pseudocódigo original, numeración de nodos)

```
1   i = tamanho(vet)
2   while i >= 2
3       j = 1
4       while j <= i - 1
5           if vet[j] > vet[j+1]
6               aux = vet[j]; vet[j] = vet[j+1]; vet[j+1] = aux
7           j++
8       i--
9   fin
```

## 1. Grafo de flujo de control

| Nodo | Descripción |
|------|-------------|
| 1 | Inicio: `i = tamanho(vet)` |
| 2 | Decisión bucle externo: `i >= 2` |
| 3 | `j = 1` |
| 4 | Decisión bucle interno: `j <= i-1` |
| 5 | Decisión: `vet[j] > vet[j+1]` |
| 6 | Intercambio con `aux` |
| 7 | `j++` |
| 8 | `i--` |
| 9 | Fin |

Aristas (E = 11):

```
1→2   2→3 (V)   2→9 (F)   3→4   4→5 (V)   4→8 (F)
5→6 (V)   5→7 (F)   6→7   7→4   8→2
```

```
        [1]
         |
         v
   +--->[2]--F-------------------+
   |     | V                     |
   |     v                       |
   |    [3]                      |
   |     |                       |
   |     v                       |
   |  +>[4]--F-->[8]-------------+  (8→2)
   |  |  | V                     |
   |  |  v                       |
   |  | [5]--F--+                |
   |  |  | V    |                |
   |  |  v      |                |
   |  | [6]     |                |
   |  |  |      |                |
   |  |  v      |                |
   |  +-[7]<----+                |
   |                             v
   +--(8→2)                     [9]
```

## 2. Complejidad ciclomática

| Fórmula | Cálculo | Resultado |
|---------|---------|-----------|
| V(G) = E − N + 2P | 11 − 9 + 2(1) | **4** |
| V(G) = P + 1 (nodos de decisión: 2, 4, 5) | 3 + 1 | **4** |
| V(G) = regiones | 3 encerradas + 1 exterior | **4** |

## 3. Caminos independientes (decisión + condición simple)

| Camino | Secuencia de nodos |
|--------|--------------------|
| C1 | 1-2-9 |
| C2 | 1-2-3-4-5-7-4-8-2-9 |
| C3 | 1-2-3-4-5-6-7-4-8-2-9 |
| C4 | 1-2-3-4-5-6-7-4-5-6-7-4-8-2-3-4-5-7-4-8-2-9 |

Cada condición es simple (sin `&&`/`||`), por lo que cobertura de decisiones y de condición coinciden.
Con indexación 1-based, `i >= 2` garantiza que el bucle interno se ejecuta al menos una vez, así que la arista 4→8 sin pasar por 5 es infactible.

## 4. Casos de prueba

| ID CP | Camino en el Grafo | Valores de Prueba | Resultado Esperado |
|-------|--------------------|-------------------|--------------------|
| CP1 | 1-2-9 | `[]`, `[7]` | `[]`, `[7]` |
| CP2 | 1-2-3-4-5-7-4-8-2-9 | `[1, 2]` | `[1, 2]` |
| CP3 | 1-2-3-4-5-6-7-4-8-2-9 | `[2, 1]` | `[1, 2]` |
| CP4 | 1-2-3-4-5-6-7-4-5-6-7-4-8-2-3-4-5-7-4-8-2-9 | `[3, 1, 2]` | `[1, 2, 3]` |

## Correspondencia con las pruebas

| CP | Prueba en `tests/test_bubble_sort.py` |
|----|----------------------------------------|
| CP1 | `test_cp1_empty_list`, `test_cp1_single_element` |
| CP2 | `test_cp2_already_sorted` |
| CP3 | `test_cp3_single_swap` |
| CP4 | `test_cp4_multiple_passes_with_swaps` |
