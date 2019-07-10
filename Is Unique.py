"""
Is Unique: Implement an algorithm to determine if a string has all unique characters. 
What if you cannot use additional data structures?
O(NlogN)

thoughts, sort the string then use 2 pointers
"""
def is_unique(s):
  l = list(s)
  l.sort()
  i, j = 0, 1
  while (i < j):
    if l[i] == l[j]:
      reutrn false
    else:
      i += 1
      j += 1
