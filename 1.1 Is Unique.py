"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
O(NlogN)

hints: use ASCII, convert to integer and use as index
it is basiclly a transformation of hashtable 

A common approach in string manipulation problems is to edit the string starting from the end and working backwards. 
This is useful because we have an extra buffer at the end, which allows us to change characters without worrying about 
what we're overwriting.

"""

def unique(string):
    # Assuming character set is ASCII (128 characters)
    if len(string) > 128:
        return False

    char_set = [False for _ in range(128)]
    for char in string:
        val = ord(char)
        if char_set[val]:
            # Char already found in string
            return False
        char_set[val] = True

    return True

