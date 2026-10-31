# AI Assignment: Uninformed (Blind) Search

**Algorithms:** BFS, DFS, DLS, IDDFS, UCS
**Language:** Python 3 (standard library only)
**Run:** `python search.py`

## Problem Graph

Directed, weighted. Start = `S`, Goal = `G`.

| From | To (step cost) |
|------|----------------|
| S | A (1), B (4) |
| A | C (2), D (5) |
| B | D (1), E (3) |
| C | G (6) |
| D | G (2) |
| E | G (5) |

## Output

| Algorithm | Path | Cost | Expansion Order |
|-----------|------|------|-----------------|
| BFS | S → A → C → G | 9 | S A B C D E G |
| DFS | S → A → C → G | 9 | S A C G |
| DLS (limit 2) | not found (cutoff) | - | S A C D B D E |
| DLS (limit 3) | S → A → C → G | 9 | S A C G |
| IDDFS | S → A → C → G (depth 3) | 9 | S / S A B / S A C D B D E / S A C G |
| UCS | S → B → D → G | **7** | S A C B D E G |

**Key observation:** BFS, DFS, DLS and IDDFS ignore edge costs, so they return the
path with the fewest edges (cost 9). Only UCS returns the cheapest path (cost 7).

## Comparison

(b = branching factor, d = depth of shallowest goal, m = max depth, l = depth limit, C* = optimal cost, ε = min step cost)

| Algorithm | Complete | Optimal | Time | Space | Data Structure |
|-----------|----------|---------|------|-------|----------------|
| BFS | Yes | Yes (unit cost) | O(b^d) | O(b^d) | Queue (FIFO) |
| DFS | No (infinite depth) | No | O(b^m) | O(bm) | Stack (LIFO) |
| DLS | No (if l < d) | No | O(b^l) | O(bl) | Stack / recursion |
| IDDFS | Yes | Yes (unit cost) | O(b^d) | O(bd) | Stack / recursion |
| UCS | Yes (ε > 0) | Yes | O(b^(1+C*/ε)) | O(b^(1+C*/ε)) | Priority queue (min-heap) |

## Files

- `search.py`: implementation and demo
- `README.md`: this report
