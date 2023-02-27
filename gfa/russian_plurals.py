"""
Given the array ["day", "days"] and non negative number, combine the number with the appropriate string from the array.
"""


def english_plurals(arr: list, n: int) -> str:
    """
    This function takes as an input an array of two strings and an integer and returns the correct combination of the
    integer with appropriate string.

    Example:
        (1) arr = ["day", "days"]
            n = 3
            english_plurals(arr, n) => 3 days
    """

    if n == 1:
        return f"{n} {arr[0]}"
    return f"{n} {arr[1]}"


# ----------------- TESTS -----------------

arr = ["day", "days"]
n_1 = 0
print(english_plurals(arr, n_1))
# Expected Output: 0 days

arr = ["day", "days"]
n_2 = 1
print(english_plurals(arr, n_2))
# Expected Output: 1 day

arr = ["day", "days"]
n_3 = 2
print(english_plurals(arr, n_3))
# Expected Output: 2 days

arr = ["day", "days"]
n_4 = 3
print(english_plurals(arr, n_4))
# Expected Output: 3 days

arr = ["day", "days"]
n_5 = 4
print(english_plurals(arr, n_5))
# Expected Output: 4 days

arr = ["day", "days"]
n_6 = 100
print(english_plurals(arr, n_6))
# Expected Output: 100 days
