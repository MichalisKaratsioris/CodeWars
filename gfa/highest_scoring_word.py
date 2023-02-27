"""
Given a string of words, you need to find the highest scoring word. Each letter of a word scores points according
to its position in the alphabet: a = 1, b = 2, c = 3 etc. You need to return the highest scoring word as a string.
If two words score the same, return the word that appears earliest in the original string. All letters will be
lowercase and all inputs will be valid.
"""


def highest_scoring_word(s: str) -> str:
    """
    This function takes as an input a string with a random number of words and returns the word with the highest score.

    Example:
        (1) s = "today I went to the park" :    today=20+15+4+1+25=65, I=9, went=23+5+14+20=62, to=20+15=35,
                                                the=20+8+5=33, park=16+1+18+11=46
            highest_scoring_word(s) => today
    """
    letters = {
        "a": 1,
        "b": 2,
        "c": 3,
        "d": 4,
        "e": 5,
        "f": 6,
        "g": 7,
        "h": 8,
        "i": 9,
        "j": 10,
        "k": 11,
        "l": 12,
        "m": 13,
        "n": 14,
        "o": 15,
        "p": 16,
        "q": 17,
        "r": 18,
        "s": 19,
        "t": 20,
        "u": 21,
        "v": 22,
        "w": 23,
        "x": 24,
        "y": 25,
        "z": 26
    }
    words = s.split(" ")
    max_score = 0
    word_max = [words[0]]
    for word in words:
        score = 0
        for i in range(len(word)):
            score = score + letters[word[i].lower()]
        if score > max_score:
            word_max[0] = word
            max_score = score
    return word_max[0]


# ----------------- TESTS -----------------

s_1 = "a b c d"
print(highest_scoring_word(s_1))
# Expected Output: d

s_2 = "today I went to the park"
print(highest_scoring_word(s_2))
# Expected Output:

s_3 = "a and b equals three"
print(highest_scoring_word(s_3))
# Expected Output: equals

s_4 = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
print(highest_scoring_word(s_4))
# Expected Output:

s_5 = "a b c d e f g h i j k l m n o p q r s t u v w x y z ya yb"
print(highest_scoring_word(s_5))
# Expected Output:
