"""
Q1) In the example code above, why do states 4, 5 and 6 contain empty lists?

States 4, 5 and 6 contain empty lists because they represent inaccessible states.
Once we get there we shouldn't be able to get out!

Q2) Can you complete the rest of the grid?

Following the method from the example, the rest of the grid can be completed as below.

Q3) The tree structure covers the states and actions,
    but how would you represent the initial state and the goal state of our problem?

The initial state and the goal state can be represented with integers:
initialState = 0
goalState = 27

"""

tree = [
    # 0
    [1, 7, 8],
    # 1
    [0, 2, 7, 8, 9],
    # 2
    [1, 3, 8, 9, 10],
    # 3
    [2, 9, 10],
    # 4
    [],
    # 5
    [],
    # 6
    [],
    # 7
    [0, 1, 8, 15],
    # 8
    [0, 1, 2, 7, 9, 15, 16],
    # 9
    [1, 2, 3, 8, 10, 15, 16],
    # 10
    [2, 3, 9, 16, 18],
    # 11
    [],
    # 12
    [],
    # 13
    [],
    # 14
    [],
    # 15
    [7, 8, 9, 16, 23],
    # 16
    [8, 9, 10, 15, 23, 24],
    # 17
    [],
    # 18
    [10, 19, 24, 25, 26],
    # 19
    [18, 25, 26, 27],
    # 20
    [],
    # 21
    [],
    # 22
    [],
    # 23
    [15, 16, 24],
    # 24
    [16, 18, 23, 25],
    # 25
    [18, 19, 24, 26],
    # 26
    [18, 19, 25, 27],
    # 27
    [19, 26],
]