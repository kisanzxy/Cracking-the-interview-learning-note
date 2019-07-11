"""
Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters,
and that you are given the "true" length of the string. 
(Note: If implementing in Java,please use a character array so that you can perform this operation in place.)
EXAMPLE
Input: "Mr John Smith ", 13
Output: "Mr%20John%20Smith"

count the string from back to front
"""

def urlify(string, length):
    '''function replaces single spaces with %20 and removes trailing spaces'''
    new_index = len(string)

    for i in range(length-1,-1,-1):
        if string[i] == ' ':
            # Replace spaces
            string[new_index - 3:new_index] = '%20'
            new_index -= 3
        else:
            # Move characters
            string[new_index-1] = string[i]
            new_index -= 1

    return string
