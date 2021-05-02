count = 0

def QuickSort(A, l, r):
    if l >= r:
        return
    i = ChoosePivot(A, l, r)
    A[l] , A[i] = A[i], A[l] 
    j = Partition(A, l, r)
    QuickSort(A, l, j-1)
    QuickSort(A, j+1, r)


def ChoosePivot(A, l, r):
    # always pick the leftmost as pivot
    return l
    
    # always pick the rightmost as pivot
    return r

    # pick the meidan value as pivot
    result = 0
    m = (r - l) // 2 + l    # "+ l" is for the second half, l is always 0 for first half
    
    my_dict = {}
    my_dict[l] = A[l]
    my_dict[m] = A[m]
    my_dict[r] = A[r]
    key_dict = list(my_dict.keys())
    value_dict = list(my_dict.values())
    for index, i in enumerate(value_dict):
        if i != min(value_dict) and i != max(value_dict):
            result = key_dict[index]
            break
    return result
            


def Partition(A, l, r):
    global count
    count += r - l
    p = A[l]
    i = l + 1

    for j in range(l+1, r+1):
        if A[j] < p:
            A[j], A[i] = A[i], A[j]
            i += 1
            
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1

with open('QuickSort.txt', 'r') as file:
    all_file = file.read().strip()  # Read and remove any extra new line
    all_file_list = all_file.split('\n')  # make a list of lines
    # make list and convert to int 
    a = []
    for line in all_file_list:
        for each_int in line.split():
            a.append(int(each_int))


# a = [3,2,1,5,8,4,7,6]
length = len(a)
QuickSort(a, 0, length - 1)
print(a)
print(count)
