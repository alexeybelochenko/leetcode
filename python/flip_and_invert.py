# Given a binary matrix A, we want to flip the image horizontally, then invert it, and return the resulting image.

# To flip an image horizontally means that each row of the image is reversed.  For example, flipping [1, 1, 0] horizontally results in [0, 1, 1].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [0, 1, 1] results in [1, 0, 0].

#My own 
def flipAndInvertImage(A):
    result = []
    for first in A:
        temp = []
        for second in first[::-1]:
            temp.append(second ^ 1)
        
        result.append(temp)

    return result


# Complexity Analysis

# Time Complexity: O(N), where N is the total number of elements in A.

# Space Complexity: O(1) in additional space complexity.

def flipAndInvertImage_example(self, A):
    for row in A:
        for i in range((len(row) + 1) / 2):
            """
            In Python, the shortcut row[~i] = row[-i-1] = row[len(row) - 1 - i]
            helps us find the i-th value of the row, counting from the right.
            """
            row[i], row[~i] = row[~i] ^ 1, row[i] ^ 1
    return A

def flipAndInvertImage_example_gen(A):
    invert = lambda x: x ^ 1
    return [list(map(invert, item)) for item in [row[::-1] for row in A]]
    #return [[i ^ 1 for i in r[::-1]] for r in A]

print(flipAndInvertImage_example_gen([[1,1,0],[1,0,1],[0,0,0]]))