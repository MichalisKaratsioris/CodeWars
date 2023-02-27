"""
In mathematics, Pascal's triangle is a triangular array of the binomial coefficients:
    (n k) = n! / ( k! (n-k)! )
where n denotes the row of the triangle and k is a position of a term in the row.

Task
Write a function that, given a depth n, returns n top rows of Pascal's Triangle flattened into a one-dimensional
list/array.
"""

import functools
import operator


def pascals_triangle(n: int) -> list:
    """
    This function takes as an input an integer (n) denoting the depth in Pascal's triangle, and returns the elements of
    the triangle as a 1D array.

    Example:
        (1) n = 3
            pascals_triangle(n) => [1, 1, 1, 1, 2, 1]
    """

    pascals_t = [[1], [1, 1]]
    pascals_list = []
    if n <= 0:
        return "n should be at least 1."
    if n == 1:
        return [1]
    while len(pascals_t) < n:
        last = pascals_t[-1]
        new = [1]
        for i in range(len(last) - 1):
            new.append(last[i] + last[i + 1])
        new.append(1)
        pascals_t.append(new)
    for row in pascals_t:
        for number in row:
            pascals_list.append(number)
    return pascals_list


# ----------------- TESTS -----------------

n_1 = 1
print(pascals_triangle(n_1))
# Expected Output: [1]

n_2 = 2
print(pascals_triangle(n_2))
# Expected Output: [1, 1, 1]

n_3 = 3
print(pascals_triangle(n_3))
# Expected Output: [1, 1, 1, 1, 2, 1]

n_4 = 4
print(pascals_triangle(n_4))
# Expected Output: [1, 1, 1, 1, 2, 1, 1, 3, 3, 1]

n_5 = 5
print(pascals_triangle(n_5))
# Expected Output: [1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1]

n_6 = 6
print(pascals_triangle(n_6))
# Expected Output: [1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, 1, 5, 10, 10, 5, 1]

n_7 = 7
print(pascals_triangle(n_7))
# Expected Output: [1, 1, 1, 1, 2, 1, 1, 3, 3, 1, 1, 4, 6, 4, 1, 1, 5, 10, 10, 5, 1, 1, 6, 15, 20, 15, 6, 1]
