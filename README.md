memgraph
========

Python package for in-memory integer-indexed, 2D
graphs. Provides some algorithms and a base graph
object. Usage example:

```python
from memgraph import Graph
from memgraph.utils import proximity

g = Graph()
g[1,1] = 3
g[1,0] = 2

for x, y in proximity(1, (0,0)):
    item = g[x,y]
    if not item:
        continue
    print(item)
```

Mainly used for some experiments, and in the
future probably stuff to do with math.
