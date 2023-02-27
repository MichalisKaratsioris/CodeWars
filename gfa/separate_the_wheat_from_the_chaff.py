"""
With Cereal crops like wheat or rice, before we can eat the grain kernel, we need to remove that inedible hull,
or to separate the wheat from the chaff.

Task
Given a sequence of n integers , separate the negative numbers (chaff) from positive ones (wheat).
"""


def wheat_from_chaff(arr: list) -> list:
    """
    This function takes as an input a list of integers and returns a list of integers keeping all negative integers in
    the beginning of the list followed by the positive ones.

    Example:
        (1) arr = [7, -8, 1, -2]
            wheat_from_chaff(arr) => [-2, -8, 1, 7]
    """

    temp = arr.copy()
    for number in arr:
        if number > 0:
            temp.remove(number)
            temp.append(number)
    # sort() function has O(NlogN) time complexity which is worse than O(N).
    # arr.sort()
    return temp


# ----------------- TESTS -----------------

arr_1 = [7, -8, 1, -2]
print(wheat_from_chaff(arr_1))
# Expected Output: [-2, -8, 1, 7]

arr_2 = [-31, -5, 11, -42, -22, -46, -4, -28]
print(wheat_from_chaff(arr_2))
# Expected Output: [-31, -5,- 28, -42, -22, -46 , -4, 11]

arr_3 = [-25, -48, -29, -25, 1, 49, -32, -19, -46, 1]
print(wheat_from_chaff(arr_3))
# Expected Output: [-25, -48, -29, -25, -46, -19, -32, 49, 1, 1]

arr_4 = [5, 4, 3, 2, 1, -1, -2, -3, -4, -5]
print(wheat_from_chaff(arr_4))
# Expected Output: [-1, -2, -3, -4, -5, 5, 4, 3, 2, 1]
