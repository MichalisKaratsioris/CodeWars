"""
There is an array with some numbers. All numbers are equal except for one. Try to find it!
"""


def find_the_unique_number(arr: list) -> int:
    """
    This function takes as an input a list of integers where all but one are equal and returns the unique integer.

    Example:
        (1) arr = [1, 1, 1, 2, 1, 1]
            find_the_unique_number(arr) => 2
    """

    dic = {}
    numbers = set(arr)
    for number in numbers:
        dic[number] = 0
    for number in arr:
        dic[number] = dic[number] + 1
    for number in dic.keys():
        if dic[number] == 1:
            return number


# ----------------- TESTS -----------------

arr_1 = [1, 1, 1, 2, 1, 1]
print(find_the_unique_number(arr_1))
# Expected Output: 2

arr_2 = [0, 0, 0.55, 0, 0]
print(find_the_unique_number(arr_2))
# Expected Output: 0.55

arr_3 = [1, 0, 0, 0, 0]
print(find_the_unique_number(arr_3))
# Expected Output: 1
