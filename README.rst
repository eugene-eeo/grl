grl
===

grl is a library of utility functions for points. It
includes functions for computing distances, whether a
point is included in a given proximity to another
point, etc.

.. code-block:: python

    import grl
    assert grl.distance([0,1], [1,1]) == 1.0
    assert (0,1) in grl.proximity(1, [0,0])

grl does not ship with a graphing class. Instead it
is up to the user to choose which graph implementation
to use. grl simply provides algorithms.
