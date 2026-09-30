#  File geotest.py

################################################################
#  You should not modify anything in this file
################################################################

import math
import geometry


def do_distance(x1: float, y1: float, x2: float, y2: float) -> None:
    print(end=f'The distance between ({x1}, {y1}) and ({x2}, {y2}) is ')
    print(f'{geometry.distance(x1, y1, x2, y2)}')

def do_slope(x1: float, y1: float, x2: float, y2: float) -> None:
    print(end='The slope of the line between ')
    print(f'({x1}, {y1}) and ({x2}, {y2}) is', end=' ')
    m = geometry.slope(x1, y1, x2, y2)
    if m == math.inf:
        print("undefined")
    else:
        print(m)

def do_intercept(x1: float, y1: float, x2: float, y2: float) -> None:
    if geometry.slope(x1, y1, x2, y2) == math.inf:
        print(end='The x-')
    else:
        print(end='The y-')
    print(end='intercept of the line between ')
    print(end=f'({x1}, {y1})')
    print(end=' and ')
    print(end=f'({x2}, {y2})')
    print(f' is {geometry.intercept(x1, y1, x2, y2)}')

def do_equation(x1: float, y1: float, x2: float, y2: float) -> None:
    print(end='The equation of the line between ')
    print(end=f'({x1}, {y1})')
    print(end=' and ')
    print(end=f'({x2}, {y2})')
    print(f' is {geometry.line_equation_mb(geometry.slope(x1, y1, x2, y2), 
                                           geometry.intercept(x1, y1, x2, y2))}')


if __name__ == '__main__':
    while True:   #  Infinite loop, use Control-C to quit
        # Get user input
        in_vals = input("Enter the point coordinates x1 y1 x2 y2 (z quits): ")
        if in_vals == 'z' or in_vals == 'Z':
            break
        arglist = in_vals.strip().split()
        p_x1 = float(arglist[0])
        p_y1 = float(arglist[1])
        p_x2 = float(arglist[2])
        p_y2 = float(arglist[3])

        # Exercise the functions
        do_distance(p_x1, p_y1, p_x2, p_y2)
        do_slope(p_x1, p_y1, p_x2, p_y2)
        do_intercept(p_x1, p_y1, p_x2, p_y2)
        do_equation(p_x1, p_y1, p_x2, p_y2)
        print("-----------------")