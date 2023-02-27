"""
You are doing an exercise for chess class. Your job given a bishop's start position (start) find if the end position
(end) given is possible within n moves.
"""


def bishop_movement_check(start: str, end: str, n: int) -> bool:
    """
    This function takes as an input three parameters:
        - bishop's starting position as a string
        - bishop's ending position as a string
        - number of moves as an integer
    and returns if it is possible (True) or not (False).

    Example:
        (1) start = 'a1'
            end = 'h8'
            n = 2
            bishop_movement_check(start, end, n) => True
    """

    white_sq = ['a2', 'a4', 'a6', 'a8', 'c2', 'c4', 'c6', 'c8', 'e2', 'e4', 'e6', 'e8', 'g2', 'g4', 'g6', 'g8', 'b1',
                'b3', 'b5', 'b7', 'd1', 'd3', 'd5', 'd7', 'f1', 'f3', 'f5', 'f7', 'h1', 'h3', 'h5', 'h7']
    black_sq = ['a1', 'a3', 'a5', 'a7', 'c1', 'c3', 'c5', 'c7', 'e1', 'e3', 'e5', 'e7', 'g1', 'g3', 'g5', 'g7', 'b2',
                'b4', 'b6', 'b8', 'd2', 'd4', 'd6', 'd8', 'f2', 'f4', 'f6', 'f8', 'h2', 'h4', 'h6', 'h8']
    files = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    if n == 0 and start == end:
        # print("1")
        return True
    elif n == 0 and start != end:
        # print("2")
        return False
    elif start in white_sq:
        if end in white_sq:
            if n > 1:
                # print("3")
                return True
            else:
                if start[0] == end[0]:
                    # print("4")
                    return False
                else:
                    if end[0] == files[abs(files.index(start[0]) - (int(start[1]) - int(end[1])))]:
                        # print("5")
                        return True
                    print("6")
                    return False
        # print("7")
        return False
    elif start in black_sq:
        if end in black_sq:
            if n > 1:
                # print("8")
                return True
            else:
                if start[0] == end[0]:
                    # print("9")
                    return False
                else:
                    if end[0] == files[abs(files.index(start[0]) - (int(start[1]) - int(end[1])))]:
                        # print("10")
                        return True
                    # print("11")
                    return False
        # print("12")
        return False
    else:
        # print("13")
        return False


# ----------------- TESTS -----------------

start_1 = 'a1'
end_1 = 'h8'
n_1 = 1
print(bishop_movement_check(start_1, end_1, n_1))
# Expected Output: True

start_2 = 'a1'
end_2 = 'h8'
n_2 = 0
print(bishop_movement_check(start_2, end_2, n_2))
# Expected Output: False

start_3 = 'a1'
end_3 = 'h7'
n_3 = 10
print(bishop_movement_check(start_3, end_3, n_3))
# Expected Output: False

start_4 = 'a1'
end_4 = 'h6'
n_4 = 2
print(bishop_movement_check(start_4, end_4, n_4))
# Expected Output: True

start_5 = 'a1'
end_5 = 'h6'
n_5 = 1
print(bishop_movement_check(start_5, end_5, n_5))
# Expected Output: False

start_6 = 'a1'
end_6 = 'h6'
n_6 = 6
print(bishop_movement_check(start_6, end_6, n_6))
# Expected Output: True

start_7 = 'a1'
end_7 = 'b7'
n_7 = 10
print(bishop_movement_check(start_7, end_7, n_7))
# Expected Output: False

start_8 = 'h1'
end_8 = 'b7'
n_8 = 2
print(bishop_movement_check(start_8, end_8, n_8))
# Expected Output: True
