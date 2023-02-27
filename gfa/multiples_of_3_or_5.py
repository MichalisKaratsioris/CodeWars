"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23. Find the sum of all the multiples of 3 or 5 below 1000.
"""


def sum_mult_three_five(n: int) -> int:
    """
    This function takes as an input an integer and returns an integer representing the sum of all multiples of 3 and 5
    lower than the provided integer n.

    Example:
        (1) n = 10 (3, 5, 6, 9)
            sum_mult_three_five(n) => 23
    """

    s = 0
    if n > 0:
        for i in range(n):
            if i % 3 == 0 or i % 5 == 0:
                s = s + i
        return s
    return 0


# ----------------- TESTS -----------------

n_1 = 10
print(sum_mult_three_five(n_1))
# Expected Output: 23

n_2 = 20
print(sum_mult_three_five(n_2))
# Expected Output: 78

n_3 = 30
print(sum_mult_three_five(n_3))
# Expected Output: 195
