def scramblies(s1: str, s2: str) -> bool:
    count = 0
    s1_array = []
    for c in s1:
        s1_array.append(c)
    for c in s2:
        if c in s1_array:
            count += 1
            s1_array.remove(c)
    if len(s2) == count:
        return True
    return False

print("(1)", scramblies('rkqodlw', 'world'))
# Expected: True
print("---------")
print("(2)", scramblies('cedewaraaossoqqyt', 'codewars'))
# Expected: True
print("---------")
print("(3)", scramblies('katas', 'steak'))
# Expected: False
print("---------")