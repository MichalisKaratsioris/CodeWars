"""
Write a function that receives two strings and returns n, where n is equal to the number of characters we should
shift the first string forward to match the second. The check should be case-sensitive. For instance, take the strings
"fatigue" and "tiguefa". In this case, the first string has been rotated 5 characters forward to produce the second
string, so 5 would be returned. If the second string isn't a valid rotation of the first string, the method returns -1.
"""


def calculate_string_rotation(si: str, sf: str) -> int:
    """
    This function takes as an input two strings and returns an integer that represents the number of forward rotations
    are needed to match the first string with the second. If it is not possible, then return -1.

    Example:
        (1) si = "coffee"
            sf = "eecoff"
            calculate_string_rotation(si, sf) => 2
    """

    count = 0
    if len(si) != len(sf):
        return -1
    si_arr = []
    sf_arr = []
    eq = 0
    for i in range(len(si)):
        si_arr.append(si[i])
        sf_arr.append(sf[i])
        if si[i] == sf[i]:
            eq = eq + 1
    if eq == len(sf):
        return 0
    while True:
        si_arr.append(si_arr[0])
        si_arr.remove(si_arr[0])
        count = count + 1
        check = ''.join(si_arr)
        if check == sf:
            return abs(len(si) - count)
        if count >= len(sf):
            break
    return -1


# ----------------- TESTS -----------------

si_1 = "coffee"
sf_1 = "eecoff"
print(calculate_string_rotation(si_1, sf_1))
# Expected Output: 2

si_2 = "eecoff"
sf_2 = "coffee"
print(calculate_string_rotation(si_2, sf_2))
# Expected Output: 4
#
si_3 = "moose"
sf_3 = "Moose"
print(calculate_string_rotation(si_3, sf_3))
# Expected Output: -1
#
si_4 = "isn't"
sf_4 = "'tisn"
print(calculate_string_rotation(si_4, sf_4))
# Expected Output: 2
#
si_5 = "dog"
sf_5 = "god"
print(calculate_string_rotation(si_5, sf_5))
# Expected Output: -1
#
si_6 = "Esham"
sf_6 = "Esham"
print(calculate_string_rotation(si_6, sf_6))
# Expected Output: 0
