# Created by: Victor Huicochea
# Course: CS 2302
# Instructor: Diego Aguirre
# TA: Manoj Pravaka
# Last Day Edited: 12/13/2018
# Lab 7 purpose: practice the use of dynamic programming


# Algorithm that returns the number of changes you need to make to a word
# in order to make it exactly as the second one.
def edit_distance(str1, str2):

    # This creates a 2D array with the length of both strings
    table = [[0 for i in range(len(str1) + 1)] for j in range(len(str2) + 1)]

    # First we fill the first line and column
    for i in range(len(str1) + 1):
        table[0][i] = i

    for i in range(len(str2) + 1):
        table[i][0] = i

    # Following loops checks how many number of changes we need to make
    for i in range(len(str2)):
        for j in range(len(str1)):
            # If characters are the same, we use the diagonal value
            if str1[j] == str2[i]:
                table[i + 1][j + 1] = table[i][j]
            # If characters are different, we get the smallest value from the surrounding 3 and add 1 to it.
            else:
                table[i+1][j+1] = min(table[i][j], table[i][j+1], table[i+1][j]) + 1

    # The method returns the bottom right value, which is the total number of changes we need to make
    num_changes = table[len(str2)][len(str1)]

    return num_changes


