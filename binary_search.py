# For any list of n items, binary search will take log base 2 of n steps to run in the worst case
# we have to find the middle element and then compare it to our target number to check that it is bigger or smaller 

# Binary search 
import random 

# 1 to 100 
numList = [n for n in range(1,101)]

# to Choose a Random number 
targetNum = random.choice(numList)

def binary_search (lis , item):
    firstIndex = 0 
    lastIndex = len(lis) - 1  
    operationCount = 0 

    while (firstIndex <= lastIndex):
        operationCount += 1 
        mid = round((firstIndex+lastIndex) / 2 )

        if (lis[mid] == item):
            return mid , operationCount
        elif (lis[mid] < item):
            firstIndex = mid + 1 
        elif (lis[mid] > item):
            lastIndex = mid -1 
    # return none if item is not existed 
    return None


print(binary_search(numList,targetNum))
