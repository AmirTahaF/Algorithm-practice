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