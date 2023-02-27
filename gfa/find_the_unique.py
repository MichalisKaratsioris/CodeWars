"""
here is an array. All elements are the same except for one. Try to find it!
"""


def find_the_unique(arr: list):
    """
    This function takes as an input a list where all but one are of the same data type and returns the unique element.

    Example:
        (1) arr = [4, 4, 'foo', 4]
            find_the_unique_string(arr) => 'foo'
    """

    types = []
    for e in arr:
        types.append(type(e))
    t_set = set(types)
    dic = {}
    for t in t_set:
        dic[t] = 0
    for element in arr:
        if type(element) in dic.keys():
            dic[type(element)] = dic[type(element)] + 1
    for element in arr:
        if dic[type(element)] == 1:
            return element
    if type(arr[0]) == type(''):
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
    elif type(arr[0]) == type(1):
        dic = {}
        numbers = set(arr)
        for number in numbers:
            dic[number] = 0
        for number in arr:
            dic[number] = dic[number] + 1
        for number in dic.keys():
            if dic[number] == 1:
                return number
    else:
        return "Sorry, but I can not sort out this data type elements."


# ----------------- TESTS -----------------

arr_1 = [1, 1, 1, 2, 1, 1]
print(find_the_unique(arr_1))
# Expected Output: 2

arr_2 = [4, 4, 'foo', 4]
print(find_the_unique(arr_2))
# Expected Output: foo

arr_3 = ['Aa', 'aaa', 'aaaaa', 'BbBb', 'Aaaa', 'AaAaAa', 'a']
print(find_the_unique(arr_3))
# Expected Output: BbBb

arr_4 = ['abc', 'acb', 'bac', 4, 'bca', 'cab', 'cba']
print(find_the_unique(arr_4))
# Expected Output: 4

arr_5 = ['abc', 'acb', 'bac', [1, 2, 3, 4], 'bca', 'cab', 'cba']
print(find_the_unique(arr_5))
# Expected Output: [1, 2, 3, 4]

arr_6 = [{}, {}, {}, {}, {}, {}, {}]
print(find_the_unique(arr_6))
# Expected Output: Sorry, but I can not sort out this data type elements.
