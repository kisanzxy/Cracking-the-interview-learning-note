"""
Given an image represented by an NxN matrix, where each pixel in the image is 4 bytes,
write a method to rotate the image by 90 degrees. Can you do this in place?
"""

def rotate_matrix(m):
    if len(m) == 0 or len(m[0]) == 0 or len(m) != len(m[0]):
        return False
    n = len(m)
    for layer in range(n// 2):
        first = layer #current arr start pos
        last = n - 1 - layer #current arr end pos

        #iterate through the "four" arrs
        for i in range(first,last):
            offset = i - first 
            #save top
            top = m[first][i]
            m[first][i] = m[last - offset][first]
            m[last - offset][first] = m[last][last - offset]
            m[last][last - offset] = m[i][last - offset]
            m[i][last - offset] = top
    return True
