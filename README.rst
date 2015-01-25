grl
===

grl is a library that can be used to compose
high level algorithms for coordinates geometry.
It has basic functions that operate on and
generate points. It is not a graphing library.
Rather it should be used in concert with such
a library. The proximity functions can also be
used for sight radii/cell manipulation on grids.


.. code-block:: python

    import grl
    assert grl.distance((0,0), (3,4)) == 5.0
    assert (0,1) in grl.proximity(1, (0,0))
