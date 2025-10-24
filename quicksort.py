# QuickSort Algorithm
# A divide-and-conquer sorting algorithm that selects a pivot element,
# partitions the array into elements less than and greater than the pivot,
# and recursively sorts the subarrays. Efficient for large datasets with
# an average time complexity of O(n log n).

lis = [2,5,1,3,9,6,4,10,8,7]


# for take middle element as pivot 

# Using the middle element as the pivot helps avoid the worst-case scenario
# that happens when the array is already sorted or nearly sorted.
# Choosing the first element as pivot in a sorted list causes unbalanced partitions,
# leading to O(n^2) time instead of the optimal O(n log n).

def middle(arr):
    start = 0
    end = len(arr)

    midIndex = round((start + end) / 2) 
    return midIndex


def quick_sort(arr):

    # base case :
    #   len(arr) => [] or [1]
    if len(arr) < 2 :
        return arr

    else :

        pivot = arr[middle(arr)]

        smaller = [i for i in arr if i < pivot]
        mid =  [i for i in arr if i == pivot]
        greater = [i for i in arr if i > pivot]

        return quick_sort(smaller) + mid + quick_sort(greater)

print(quick_sort(lis))

