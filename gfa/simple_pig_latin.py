"""
Move the first letter of each word to the end of it, then add "ay" to the end of the word.
Leave punctuation marks untouched.
"""


def simple_pig_latin(s: str) -> str:
    """
    This function takes as an input a string and returns a string where the first letter of each word is moved
    to the end of it and then addede "ay" to the end as well. Punctuation marks were left untouched.

    Example:
        (1) s = "Hello world !"
            simple_pig_latin(s) => elloHay orldway !
    """

    words = s.split(" ")
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for i in range(len(words)):
        if words[i][0] in letters:
            words[i] = words[i][1:] + words[i][0] + "ay"
    return " ".join(words)


# ----------------- TESTS -----------------

s_1 = "Hello world !"
print(simple_pig_latin(s_1))
# Expected Output: elloHay orldway !

s_2 = "Pig latin is cool"
print(simple_pig_latin(s_2))
# Expected Output: igPay atinlay siay oolcay
