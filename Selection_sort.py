# first of all we have to find the smallest number in a list and the append it to our new list
# For Bog O :
# you don’t have to check a list of n elements each time.
# You check n elements, then n – 1, n - 2 … 2, 1. On average, you check a
# list that has 1/2 × n elements. The runtime is O(n × 1/2 × n).
# But constants like 1/2 are ignored in Big O notation
# so ==> O(n**2)

listOfNum = [30,60,33,45,87,13,9,56,100,34,77,69,20,2]

def find_smallest(arr):

    smallest = arr[0]
    smallest_index = 0

    for item in range(1,len(arr)):
        if arr[item] < smallest :
            smallest = arr[item]
            smallest_index = item
    return smallest_index

def selection_sort(arr):
    sorterArr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        sorterArr.append(arr.pop(smallest))
    return sorterArr

print(selection_sort(listOfNum))
# output => [2, 9, 13, 20, 30, 33, 34, 45, 56, 60, 69, 77, 87, 100] 

