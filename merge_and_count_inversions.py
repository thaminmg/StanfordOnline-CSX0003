# This file contains all of the 100,000 integers between 1 and 100,000 (inclusive) in some order, 
# with no integer repeated.
# Your task is to compute the number of inversions in the file given, where the 𝑖𝑡ℎ row of the file indicates 
# the 𝑖𝑡ℎ entry of an array.
# Because of the large size of this array, you should implement the fast divide-and-conquer algorithm covered 
# in the video lectures.

def Sort_and_CountInv(a, n):
    if n == 0 or n == 1:
        return (a, 0)
    else:
        half = int(n/2)
        (c, left_inversion) = Sort_and_CountInv(a[:half], len(a[:half]))
        (d, right_inversion) = Sort_and_CountInv(a[half:], len(a[half:]))
        (b, split_inversion) = Merge_and_CountInv(c, d, len(c), len(d))
        return (b, left_inversion + right_inversion + split_inversion)

def Merge_and_CountInv(c, d, nc, nd):
    i = 0
    j = 0
    split_inversion = 0
    b = [0 for i in range(nc + nd)]
    for k in range(nc + nd):
        if i == nc:
            b[k] = d[j]
            j += 1
        elif j == nd:
            b[k] = c[i]
            i += 1
        elif c[i] < d[j]:
            b[k] = c[i] 
            i += 1
        else:
            b[k] = d[j]
            j += 1
            split_inversion = split_inversion + (nc - i)
    return (b, split_inversion)


def brute_force(a, n):
    number_of_inversions = 0
    for i in range(n):
        for j in range(i+1, n):
            if a[i] > a[j]:
                number_of_inversions += 1   
    return number_of_inversions


with open('IntegerArray.txt', 'r') as file:
    all_file = file.read().strip()  # Read and remove any extra new line
    all_file_list = all_file.split('\n')  # make a list of lines
    # make list and convert to int 
    a = []
    for line in all_file_list:
        for each_int in line.split():
            a.append(int(each_int))


a = [10,9,8,7,6,5,4,3,2,1]
length = len(a)
# count = brute_force(a, length)
# print(count)
output, count = Sort_and_CountInv(a, len(a))
print(output)
print(count)
