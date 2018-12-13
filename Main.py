# Created by: Victor Huicochea
# Course: CS 2302
# Instructor: Diego Aguirre
# TA: Manoj Pravaka
# Last Day Edited: 12/13/2018
# Lab 7 purpose: practice the use of dynamic programming

from Edit_Distance import edit_distance


# Main program that compares two different strings
def main():
    str1 = "elephant"
    str2 = "relevant"

    print("---Strings to compare--- \n")
    print("String 1: ", str1)
    print("String 2: ", str2)
    num_changes = edit_distance(str1, str2)
    print("\nTotal number of changes needed to get same strings: ", num_changes)


main()