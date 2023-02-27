"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.
"""


def valid_parentheses(s: str) -> bool:
    """
    This function takes as an input a string of parentheses and returns True or False, depending on the order of
    the parentheses.

    Example:
        (1) s = "()"
            valid_parentheses(s) => True
    """

    if s[0] == ")" or s[-1] == "(":
        return False
    arr = []
    for i in range(len(s)):
        arr.append(s[i])
    st = set(arr)
    count_open= 0
    count_close = 0
    for item in arr:
        if item == "(":
            count_open = count_open + 1
        else:
            count_close = count_close + 1
    if count_close != count_open:
        return False
    count = 0
    neg = 0
    for item in arr:
        if item == "(":
            count = count + 1
        else:
            count = count - 1
        if count < 0:
            neg = neg + 1
    if neg == 0:
        return True
    return False


# ----------------- TESTS -----------------

s_1 = '()'
print(valid_parentheses(s_1))
# Expected Output: True

s_2 = ')(()))'
print(valid_parentheses(s_2))
# Expected Output: False

s_3 = '('
print(valid_parentheses(s_3))
# Expected Output: False

s_4 = '(())((()())())'
print(valid_parentheses(s_4))
# Expected Output: True
