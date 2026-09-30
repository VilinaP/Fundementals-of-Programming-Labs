#Vilina Prenko
"""
List processing routines
"""

from typing import Callable, Any


def maximum(a: list[int]) -> int | None:
    """
    Returns the maximum value in list a.
    Returns None if a is empty.
    """
    n = len(a)
    max = 0

    if a == []:
        return None
    
    for i in range(0, n-1):
        move = i+1
        if a[i] >= a[move] and a[max] <= i:
                max = i
         
    return a[max] 


def equivalent(v1: list[int], v2: list[int]) -> bool:
    """  
    Returns true if lists v1 and v2 contain 
    exactly the same elements, regardless of their
    order; otherwise, the function returns false. 
    The quantity of each element must be the same in both
    lists for the lists to be equivalent.
    """
    n_list1 = len(v1)
    n_list2 = len(v2)
    value = True

    if n_list1 != n_list2:
        value = False
    
    for i in range(0, n_list1):
        if v1[i] not in v2:
            value = False

    return value 


def is_ascending(seq: list[int]) -> bool:
    """
    Returns True if the elements of list seq are arranged
    in ascending order.
    """
    value = True
    n = len(seq)

    if seq == []:
        value = True
    
    for i in range(0, n-1):
        move = i+1
        if seq[i] > seq[move]:
            value = False
        elif seq[i] == seq[move]:
            value = False

    return value


def rotate(v: list[int], distance: int) -> None:
    """
    Physically rearranges the elements of v so that 
    all the elements are shifted towards the back 
    by a given distance. As an element "falls off" 
    the rear, it is placed at the front in the 
    space vacated when the first element was shifted backwards.
    For example, if list contains the elements 
    [1, 2, 3, 4, 5, 6], the call rotate(list, 2) 
    rearranges list to contain [5, 6, 1, 2, 3, 4].
    Notice that if distance is equal to the size of the list, 
    after the rotation all the elements rotate to 
    their original locations.
    If distance is negative, the elements are shifted forward 
    distance spots instead of backwards. As an element "falls off" 
    the front it is placed on the rear in the space 
    vacated when the last element was shifted forwards.
    For example, if list contains the elements 
    [1, 2, 3, 4, 5, 6], the call rotate(list, -2) 
    rearranges list to contain [3, 4, 5, 6, 1, 2]. 
    This function can affect the contents of the list v.
    """
    n = len(v)
    num = distance % n
    

    def reverse(start, end):
        for i in range(0, (end-start + 1)//2):
            v[start+i], v[end-i] = v[end-i], v[start+i]

   
    if num > 0:
        reverse(0, n - 1)     
        reverse(0, num - 1)     
        reverse(num, n - 1)     
    else:
        reverse(0, num-1)
        reverse(num, n-1)
        reverse(0, n - 1)   









