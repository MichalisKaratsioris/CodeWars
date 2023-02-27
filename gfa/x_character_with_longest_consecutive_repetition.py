"""
For a given string s find the character c (or C) with the longest consecutive repetition and return: (c, l)
where l is the length of the repetition. If there are two or more characters with the same l return the first in order
of appearance.

For empty string return: ('', 0)
"""


def character_with_longest_consecutive_repetition(s: str) -> tuple:
    """
    This function takes as an input a string of random characters and returns a tuple with the most occurred character,
    consecutively, along with the number of consecutive repetitions.

    Example:
        (1) s = "aaaaaABAAavrgggg"
            character_with_longest_consecutive_repetition(s) => ('a', 5)
    """

    if len(s) == 0:
        return "('', 0)"
    if len(s) == 1:
        return f"({s}, 1)"
    max_l = 1
    c = ''
    c_l = 0
    result = [s[0], 1]
    for i in range(len(s)-1):
        c = s[i]
        c_l = 1
        for j in range(i + 1, len(s)):
            if s[j] == s[i]:
                c_l = c_l + 1
            else:
                break
        if c_l > max_l:
            max_l = c_l
            result[0] = c
            result[1] = c_l
    return f"('{result[0]}', {result[1]})"


# ----------------- TESTS -----------------

s_1 = ""
print(character_with_longest_consecutive_repetition(s_1))
# Expected Output: ('', 0)

s_2 = "aaaaaaAaAAAAaa"
print(character_with_longest_consecutive_repetition(s_2))
# Expected Output: ('a', 6)

s_3 = "aaaaaaAaAAbBaa"
print(character_with_longest_consecutive_repetition(s_3))
# Expected Output: ('a', 6)

s_4 = "aAaAAbBaa"
print(character_with_longest_consecutive_repetition(s_4))
# Expected Output: ('A', 2)

s_5 = "aaaaaABAAavrgggg"
print(character_with_longest_consecutive_repetition(s_5))
# Expected Output: ('a', 5)
