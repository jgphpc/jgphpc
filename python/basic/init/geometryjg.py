#!/usr/bin/env python

""" test jg:
#ok: dir(geometryjg)
#ok: help(geometryjg)
#ok: help(geometryjg.circ_perim)
#ok: help(jg1.geo.circ_perim)
#ok: jg1.geo.circ_perim.__doc__
# python -v ./doc.py  # -m doctest 
>>> import math
>>> circ_perim(0.5)
3.141592653589793
>>> circ_area(1)
3.141592653589793
>>> sphere_area(0.5)
3.141592653589793
>>> sphere_volume(1)
3.141592653589793

"""
# math.pi ?

import math

def circ_perim(r):
    """ perimetre jg """
    if not r >= 0:
        raise ValueError("r must be >= 0")
    return (2*math.pi*r)

def circ_area(r):
    """ area jg """
    if not r >= 0:
        raise ValueError("r must be >= 0")
    return (math.pi*r*r)

def sphere_area(r):
    """ sphere area jg """
    if not r >= 0:
        raise ValueError("r must be >= 0")
    return (4*math.pi*r*r)

def sphere_volume(r):
    """ sphere volume jg """
    if not r >= 0:
        raise ValueError("r must be >= 0")
    return (4*math.pi*r*r*r/3.)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
