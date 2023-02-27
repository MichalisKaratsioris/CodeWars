import re
"""
Complete the method/function so that it converts dash/underscore delimited words into camel casing.
The first word within the output should be capitalized only if the original word was capitalized
(known as Upper Camel Case, also often referred to as Pascal case). The next words should be always capitalized.
"""


def convert_string_camel_case(s: str) -> str:
    """
    This function takes as an input a string and returns a string i
    :param s:
    :return:
    """
    result = ""
    s_arr = re.split('-|_', s)
    if s:
        for i in range(len(s_arr)):
            if i == 0:
                result += s_arr[i]
            else:
                result += s_arr[i].capitalize()
    return result


# ------------ TESTS ----------------

s1 = "the-stealth-warrior"
print(convert_string_camel_case(s1))
# Expexted Output: theStealthWarrior

s1 = "The_Stealth_Warrior"
print(convert_string_camel_case(s1))
# Expected Output: TheStealthWarrior

s1 = ""
print(convert_string_camel_case(s1))
# Expected Output:

s1 = "1"
print(convert_string_camel_case(s1))
# Expected Output: 1
