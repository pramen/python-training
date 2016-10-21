#!/usr/bin/env python2.7

def knapsack(capacity, items):
    """Be greedy!

    One item:
    >>> knapsack(100, ((1, 1),))
    [100]
    >>> knapsack(100, ((100, 1),))
    [1]

    Two items:
    >>> knapsack(100, ((1, 1), (3, 4)))
    [1, 33]
    >>> knapsack(100, ((60, 80), (50, 50)))
    [1, 0]

    Three items:
    >>> knapsack(100, ((10, 10), (30, 40), (56, 78)))
    [1, 1, 1]
    >>> knapsack(100, ((11.2,  7.4), (25.6, 17.8), (51.0, 41.2), (23.9, 15.6), (27.8, 19.0)))
    [2, 1, 1, 0, 0]

    Corner cases:

    >>> knapsack(0, ((11.2,  7.4), (25.6, 17.8)))
    [0, 0]
    >>> knapsack(0, ((),))
    [0]

    Is it correct test?
    >>> knapsack(0, ())
    []

    >>> knapsack(100, ((11.2,  0), (0, 1), ('a', 2), (3, 'b'), (50, 2)))
    [0, 0, 0, 0, 2]
    >>> knapsack(100, (('2', 1), (4, '3')))
    [0, 25]
    >>> knapsack(100, ((0, 0),))
    [0]
    >>> knapsack(100, ((25, 1), (50, 2)))
    [4, 0]
    >>> knapsack(100, ((50, 2), (25, 1)))
    [2, 0]

    >>> knapsack(100, ((-50, 2), (25, -1)))
    [0, 0]
    """

    def to_float(arr, ind):
        try:
            f = float(arr[ind])
            if f < 0:
                f = 0
            return f
        except (ValueError, IndexError):
            return 0

    # Create sorted by 'ratio' collection [[src_ind, size, ratio, item_counter], [...], ...]

    items_prepaired = []
    for ind, item in enumerate(items):

        value = to_float(item, 1)
        size = to_float(item, 0)

        try:
            ratio = value / size
        except ZeroDivisionError:
            ratio = 0

        items_prepaired.append(
            [ind, size, ratio, 0]
        )

    items_prepaired.sort(key=lambda it_p: it_p[2], reverse=True)

    # Fitting things into the bag and count them

    bag = 0
    for it_p in items_prepaired:
        if it_p[2] != 0:
            while bag + it_p[1] <= capacity:
                bag += it_p[1]
                it_p[3] += 1

    items_prepaired.sort(key=lambda it_p: it_p[0])

    return [it_info[3] for it_info in items_prepaired]

if '__main__' == __name__:
    import doctest
    doctest.testmod()
