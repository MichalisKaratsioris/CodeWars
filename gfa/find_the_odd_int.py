"""
Given an array of integers, find the one that appears an odd number of times.
There will always be only one integer that appears an odd number of times.
"""


def find_the_odd_int(arr: list) -> int:
    """
    This function takes as an input
    and returns

    Example:
        (1)
    """

    n_set = set(arr)
    n_dic = {}
    for number in n_set:
        n_dic[number] = 0
    for number in arr:
        n_dic[number] = n_dic[number] + 1
    for number in n_dic.keys():
        if n_dic[number] % 2 != 0:
            return number


# ----------------- TESTS -----------------

arr_1 = [7]
print(find_the_odd_int(arr_1))
# Expected Output: 7

arr_2 = [0]
print(find_the_odd_int(arr_2))
# Expected Output: 0

arr_3 = [1, 1, 2]
print(find_the_odd_int(arr_3))
# Expected Output: 2

arr_4 = [0, 1, 0, 1, 0]
print(find_the_odd_int(arr_4))
# Expected Output: 0

arr_5 = [1, 2, 2, 3, 3, 3, 4, 3, 3, 3, 2, 2, 1]
print(find_the_odd_int(arr_5))
# Expected Output: 4
