"""
Write a function that takes in a string of one or more words, and returns the same string, but with all five or
more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and
spaces. Spaces will be included only when more than one word is present.
"""


def reverse_selected_strings(s: str) -> str:
    """
    This function takes as an input a string of words (separated by space), and returns a string with the same
    number of words, but the words that have 5 or more letters, are reversed.
    """

    s_arr = s.split(" ")
    for i in range(len(s_arr)):
        if len(s_arr[i]) > 4:
            s_arr[i] = s_arr[i][::-1]
    return " ".join(s_arr)


# --------------- TESTS ---------------

s1 = "Hey fellow warriors"
print(reverse_selected_strings(s1))
# Expected Output: Hey wollef sroirraw

s1 = "This is a test"
print(reverse_selected_strings(s1))
# Expected Output: This is a test

s1 = "This is another test"
print(reverse_selected_strings(s1))
# Expected Output: This is rehtona test

s1 = "!ate!"
print(reverse_selected_strings(s1))
# Expected Output: eta

s1 = "?anna!"
print(reverse_selected_strings(s1))
# Expected Output: eta

s1 = "abcdefghijklmnopqrstuvwxyz"
print(reverse_selected_strings(s1))
# Expected Output: zyxwvutsrqponmlkjihgfedcba
