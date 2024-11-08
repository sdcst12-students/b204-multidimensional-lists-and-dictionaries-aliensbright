#!python3

# data from
# Advanced Dungeons and Dragons Dungeon Masters Guide p74 Cleric Table
# https://s3.amazonaws.com/arena-attachments/804915/348b48a0cbd967122dcb76f5cc6f5a01.pdf
"""
This list of lists contains Table 1a Attack Matrix for Clerics, Druids and Monks 
The index specifies the level of the character, and the entry within the row specifies the 
target to hit Armor Class with 10 on the far left, and -10 on the far right.

Write a function that finds the target based on the level and the armor class
Check the assertion tests for expected output.

Note that this could also be done with a single list and a formula to modify the list content!
"""
global table
table = [
    [],
    #10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10
    [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25], #1
    [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25], #2
    [10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23,24,25], #3
    [ 8, 9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23], #4
    [ 8, 9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23], #5
    [ 8, 9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21,22,23], #6
    [ 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21], #7
    [ 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21], #8
    [ 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20,20,21], #9
    [ 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20], #10
    [ 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20], #11
    [ 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,20,20,20,20], #12
    [ 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,20,20], #13
    [ 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,20,20], #14
    [ 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20,20,20], #15
    [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20], #16
    [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20], #17
    [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19,20], #18
    [-1, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19]  #19
]

def target(lvl,ac):
    m = table[lvl]
    ac = 10 - ac
    m = m[ac]
    return m

def tests():
    assert target(5,7) == 11
    assert target(10,-10) == 20
    assert target(17,-3) == 13

tests()