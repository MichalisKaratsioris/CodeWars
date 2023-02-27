"""
You will be given an array of strings and your task is to remove all consecutive duplicate letters from each
string in the array.
"""


def string_array_duplicates(arr: list) -> list:
    """
    This function takes as an input an array of strings and returns an array of strings after deleting any duplicate
    adjacent characters

    Example:
        (1) arr = ["abracadabra","allottee","assessee"]
            string_array_duplicates(arr) => ["abracadabra","alote","asese"]
    """

    temp = []
    for word in arr:
        t = word[0]
        for i in range(1, len(word)):
            if word[i] != t[-1]:
                t = t + word[i]
        temp.append(t)
    return temp


# ----------------- TESTS -----------------

arr_1 = ["abracadabra", "allottee", "assessee"]
print(string_array_duplicates(arr_1))
# Expected Output: ["abracadabra", "alote", "asese"]

arr_2 = ["kelless", "keenness"]
print(string_array_duplicates(arr_2))
# Expected Output: ["keles", "kenes"]
