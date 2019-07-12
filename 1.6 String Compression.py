"""
 Implement a method to perform basic string compression using the counts of repeated characters. 
 For example, the string aabcccccaaa would become a2blc5a3. If the "compressed" string would not become smaller than the original string, 
 your method should return the original string. You can assume the string has only uppercase and lowercase letters (a - z).


for java use StringBuilder
for python, use conventionlist and join
"""

def string_compression(string):
    compressed = []
    count = 0
    i, j = 0, 1
    for i in range(len(string)):
        count += 1
        if i+1 < len(string) and string[i] != string[i+1]:
            compressed.append(string[i]+str(count))
            count = 0

    compressed.append(string[-1]+str(count))
    return min(string, "".join(compressed), key = len)


class Test(unittest.TestCase):
    '''Test Cases'''
    data = [
        ('aabcccccaaa', 'a2b1c5a3'),
        ('abcdef', 'abcdef')
    ]

    def test_string_compression(self):
        for [test_string, expected] in self.data:
            actual = string_compression(test_string)
            self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()
