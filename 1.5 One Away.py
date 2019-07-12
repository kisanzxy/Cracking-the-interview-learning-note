"""
There are three types of edits that can be performed on strings: insert a character, 
remove a character, or replace a character. Given two strings, write a function to check 
if they are one edit (or zero edits) away.

EXAMPLE
pale, ple true pales, pale -> true pale, bale -> true pale, bae -> false
"""

def one_away (s1, s2):
    if len(s1) == len(s2):
        return isReplacement(s1, s2)
    elif len(s1) + 1 == len(s2):
        return isInsertion(s1, s2)
    elif len(s1) - 1 == len(s2):
        return isInsertion(s2, s1)
    return False

def isReplacement(s1, s2):
    isFound = False
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if isFound:
                return False
            isFound = True
    return True
"""
s1 is the shorter string
"""
def isInsertion(s1, s2):
    hasInsert = False
    j = 0
    for i in range(len(s2)):
        if j < len(s1):
            if s1[j] == s2[i]:
                j += 1
            else:
                if hasInsert: return False
                hasInsert = True
    return True
