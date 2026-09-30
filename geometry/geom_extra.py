""" geom_extra.py
    Contains the intersection function and support code. """

import math
import geometry  # Your geometry module


def intersection(m1: float, b1: float, m2: float, b2: float) -> tuple[float, float]:
    """ Computes the (i_x,i_x) intersection point of the lines
        y = m1x + b1 and y = m2x + b1. If m1 is math.inf, the first line equation 
        is x = b1; similarly, if m2 is math.inf, the second line equation is x = b2.
        Returns (math.inf, math.inf) if the lines do not intersect in a single point. """
    
    if m1 == m2:
        return (math.inf, math.inf)  

    elif m1 == math.inf:
        x = b1
        y = m2 * x + b1
        return (x, y)
    
    elif m2 == math.inf:
        x = b2
        y = m1 * x + b1
        return (x, y)
    
    else:
        x = (b2-b1)/(m1-m2)
        y = m1 * x + b1
        return (x, y) 

if __name__ == '__main__':
    pass