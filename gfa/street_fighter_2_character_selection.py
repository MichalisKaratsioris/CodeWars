"""
Given the array with the Street Fighter character names:
    name = [["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
            ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison" ]]
and an array with the cursor moves, i.e.: moves = ['up', 'left', 'right', 'left', 'left']
and assuming that the cursor starts always from position (0,0) or in other words on "Ryu", find the final character
selected.
"""


def street_fighter_characters_selection(names: list, moves: list) -> list:
    """
    This function takes as an input two arrays of strings and returns a list of strings with the characters who have
    been hovered by the selection cursor after all the moves (ordered and with repetition, all the ones after a move,
    whether successful or not, see tests);


    Example:
        (1) name = [["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
                   ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison" ]]
            moves = ['up', 'left', 'right', 'left', 'left']
            street_fighter_characters_selection(names, moves) => ['Ryu', 'Vega', 'Ryu', 'Vega', 'Balrog']
    """

    if len(moves) == 0:
        return names[0][0]
    position = [0, 0]
    hover = []
    for move in moves:
        if move == 'left':
            if position[0] == 0 or position[0] == 1:
                if position[1] == 0:
                    position[1] = len(names[0]) - 1
                    hover.append(names[position[0]][position[1]])
                else:
                    position[1] = position[1] - 1
                    hover.append(names[position[0]][position[1]])
        if move == 'right':
            if position[0] == 0 or position[0] == 1:
                if position[1] == len(names[0]) - 1:
                    position[1] = 0
                    hover.append(names[position[0]][position[1]])
                else:
                    position[1] = position[1] + 1
                    hover.append(names[position[0]][position[1]])
        if move == 'up':
            if position[0] == 1:
                position[0] = 0
                hover.append(names[position[0]][position[1]])
            else:
                hover.append(names[position[0]][position[1]])
        if move == 'down':
            if position[0] == 0:
                position[0] = 1
                hover.append(names[position[0]][position[1]])
            else:
                hover.append(names[position[0]][position[1]])
    return hover


# ----------------- TESTS -----------------

names_list = [["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
              ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]]
moves_1 = ['up', 'left', 'right', 'left', 'left']
print(street_fighter_characters_selection(names_list, moves_1))
# Expected Output: ['Ryu', 'Vega', 'Ryu', 'Vega', 'Balrog']

names_list = [["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
              ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]]
moves_2 = ['right', 'down', 'left', 'left', 'left', 'left', 'right']
print(street_fighter_characters_selection(names_list, moves_2))
# Expected Output: ['E.Honda', 'Chun Li', 'Ken', 'M.Bison', 'Sagat', 'Dhalsim', 'Sagat']
