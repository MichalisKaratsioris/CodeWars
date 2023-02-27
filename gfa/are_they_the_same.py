"""
Given two arrays a and b write a function comp(a, b) (or compSame(a, b)) that checks whether the two arrays have the
"same" elements, with the same multiplicities (the multiplicity of a member is the number of times it appears).
"Same" means, here, that the elements in b are the elements in a, but squared, regardless of the order.


"""


def comp_same(a: list, b: list) -> bool:
    """
    This function takes as an input two arrays of integers and returns True or False, depending of the elements of the
    first array, when squared reproduce the second array.

    Example:
        (1) a = [121, 144, 19, 161, 19, 144, 19, 11]
            b = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
            => b = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]
            comp_same(a, b) => True
    """

    if len(a) != len(b):
        return False
    sq = []
    for number in a:
        sq.append(number * number)
    sq.sort()
    b.sort()
    count = 0
    for i in range(len(sq)):
        if sq[i] == b[i]:
            count = count + 1
    if count == len(b):
        return True
    return False


# ----------------- TESTS -----------------

a_1 = [121, 144, 19, 161, 19, 144, 19, 11]
b_1 = [121, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp_same(a_1, b_1))
# Expected Output: True

a_2 = [121, 144, 19, 161, 19, 144, 19, 11]
b_2 = [132, 14641, 20736, 361, 25921, 361, 20736, 361]
print(comp_same(a_2, b_2))
# Expected Output: False

a_3 = [121, 144, 19, 161, 19, 144, 19, 11]
b_3 = [121, 14641, 20736, 36100, 25921, 361, 20736, 361]
print(comp_same(a_3, b_3))
# Expected Output: False
