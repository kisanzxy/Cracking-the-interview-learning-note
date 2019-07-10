"""
Given two strings,write a method to decide if one A is a permutation of the
other B.

use hashtable? O(N) space O(N)time, check length hash set B, then iterate A if every char in A is in b
or sort and iterate? O(NlogN)time O(1)space


"""

#more pythonic
def check_permutation(str1, str2):
    if len(str1) != len(str2):
        return False
    counter = Counter()
    for c in str1:
        counter[c] += 1
    for c in str2:
        if counter[c] == 0:
            return False
        counter[c] -= 1
    return True
