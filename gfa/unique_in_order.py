"""
Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
elements with the same value next to each other and preserving the original order of elements.
"""


def unique_in_order(s) -> list:
    """
    This function takes as an input a string with a sequence of characters and returns a list with characters in the
    same order as in the string but having deleted the adjacent duplicates.

    Example:
        (1) s = 'AAAABBBCCDAABBB'
            unique_in_order(s) => ['A', 'B', 'C', 'D', 'A', 'B']
    """

    if type(s) == str:
        s_arr = []
        for i in range(len(s)):
            s_arr.append(s[i])
        arr = [s_arr[0]]
        for i in range(len(s_arr) - 1):
            if s_arr[i] != s_arr[i + 1]:
                arr.append(s_arr[i+1])
        return arr
    elif type(s) == list:
        arr = s.copy()
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                arr.remove(s[i+1])
        return arr
    else:
        return -1


# ----------------- TESTS -----------------

s_1 = 'AAAABBBCCDAABBB'
print(unique_in_order(s_1))
# Expected Output: ['A', 'B', 'C', 'D', 'A', 'B']

s_2 = 'ABBCcAD'
print(unique_in_order(s_2))
# Expected Output: ['A', 'B', 'C', 'c', 'A', 'D']

s_3 = [1, 2, 2, 3, 3]
print(unique_in_order(s_3))
# Expected Output: [1, 2, 3]
