"""
There is an array of strings. All strings contain similar letters except one. Try to find it!
"""


def find_the_unique_string(arr: list) -> str:
    """
    This function takes as an input a list of integers where all but one are equal and returns the unique integer.

    Example:
        (1) arr = ['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']
            find_the_unique_string(arr) => 'BbBb'
    """

    unique_str = ''
    common = ''
    if arr[0][0].lower() == arr[-1][0].lower():
        common = common + arr[-1].lower()
    elif arr[0][0].lower() == arr[-2][0].lower():
        common = common + arr[-2].lower()
    else:
        common = common + arr[-1].lower()
    common_arr = []
    for i in range(len(common)):
        common_arr.append(common[i])
    delta = 0
    for string in arr:
        for j in range(len(string)):
            if not string[j].lower() in common_arr:
                unique_str = string
                delta = 1
                break
        if delta != 0:
            break
    return unique_str


# ----------------- TESTS -----------------

arr_1 = ['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']
print(find_the_unique_string(arr_1))
# Expected Output: BbBb

arr_2 = ['abc', 'acb', 'bac', 'foo', 'bca', 'cab', 'cba']
print(find_the_unique_string(arr_2))
# Expected Output: foo
