################################################
# Lab 6 - Performance of algorithm
# This lab seeks to help you better undrestand O(N), O(N logN), and O(N^2)

# What you should do:
# 1) Run the code and observe the output.  Note - the last two columns should be rougly the same
# 2) Modify the function duplicateSearchSorted() below so it is O(N).  
# 3) Re-run the code - the last column values should now be MUCH smaller than the third column
# 4) Modify the main out loop to include larger values of numElements (you can increase by larger increments than 2000), 
#    keep going until the last line takes at least a minute to run.
#    (the value of numElements that does this can differ for different computers due to processor speed)
# 5) In your group, decide with is the performance of the sections 2, 3, 4, and 5 below.   O(N)?  O(N logN)?  O(N^2)?
# 6) Write up a short report and upload the report.  The report sould include:
#     A) Your code for duplicateSearchSorted()
#     B) Your output showing the perfomance after you have modified duplicateSearchSorted().  Again, you should go up to a numElements value 
#        that results in the sum of the 4 columns on the last row being at least a minute
#     C) State the complexity of the algoirithms in section 2, 3, 4, and 5 and why you think that is correct
################################################

import random
import time

verbose = False   # used to quell print students used for debugging/undersatning running code

def linearSearch(elementList, item):
    ''' Returns the index of parameter "item" in the parameter "elementList", False if not found
    Starting with the first list element, check to see if match and if move on to next list element
    If a match is found, then variable "found" is set to true to terminate loop
    If make it to end of loop the element is not in the list, return False.
    If a match is found, return the index of the found elment'''
    
    i = 0 
    found = False
    while (not found and i < len(elementList)):
        if elementList[i] == item:
            if verbose:
                print("Found it.  i = " + str(i))
            found = True
        i += 1
    if not found:
        if verbose:
            print("item " + str(i) + " not in the list")
        return False
    else:
        return i-1


def binarySearch(arr, x):
    ''' Returns the index of element "x" is the list "arr" if found, returns False if not found
    THIS FUNCTION ONLY WORKS FOR SORTED LISTS as arguments
    It finds a mid point between a high and low bound (starting with the full list), and:
        if the midpoint element == "x", return the index of "x", i.e. the value of mid
        if the midpoint element is > than "x" reduce the bounds to the left half of the list
        if midpoint element < "x" reduce the bounds to the right half of the list'''
    
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:  # x in right half
            low = mid + 1
        else:                # x in left half
            high = mid - 1
    return False  # x is not found


def duplicateSearch(elementList):
    ''' Takes a list of elements as an argument and prints out (if verbose is set to True) the index of all duplicate values
    This is a "classic" double-nested loop to compare every pair of possible values modified slightly so that 
    the inner loops starts and the outer-loop index value + 1   (no need to check for duplicates before an element, 
    if there already found)'''
    
    duplicateFound = False
    for i in range(0,len(elementList)):
        for j in range(i+1, len(elementList)):
            if (elementList[i] == elementList[j]): 
                if verbose:
                    print(str(elementList[i]) + " is a duplicate, at locations: " + str(i) + " " + str(j))
                duplicateFound = True
    if not duplicateFound:
        if  verbose:
            print("No duplicates found")
                

def duplicateSearchSorted(elementList):
    ''' 
    Searches for duplicates in a sorted list.
    Returns True if duplicates are found, False otherwise.
    This function runs in O(N) time complexity.
    '''

    duplicateFound = False
    prev_element = None

    for element in elementList:
        if element == prev_element:
            if verbose:
                print(str(element) + " is a duplicate")
            duplicateFound = True
        prev_element = element
    
    if not duplicateFound:
        if verbose:
            print("No duplicates found")
    
    return duplicateFound



######################## code below uses the functions above to run the experiments
# The outer loop just run all the code contiains for increasing values of N
# Inside the outer loop there are 5 sections:
# Section 1: Create a list of random integers. Note, the range is 10,000 the number of entries so there should be few duplicate values in the list
# Section 2: Run numElements linear searches 
# Section 3: Run numElements binary searches 
# Section 4: Call/run duplicateSearch()
# Section 5: Call/run duplicateSearchSorted()   => you need to modify this function above to have MUCH faster performance, 
#         right now it is the same as duplicateSeach()
###########################################

# print out the header for the table of measured values              
print("    N\t\t linear \t binary \t duplicate \t dupSorted")

numElements = 1000  # Starting value of numElements
while True:
    if verbose:
        print("\n-------- starting numElements = " + str(numElements))

    # section 1
    # create and fill list
    aList = []
    for i in range(numElements):
        newNum = random.randint(1,numElements*10000)
        if (i % 97) == 0:    # save a number that is in the list to search for
            tempNum = newNum
        aList.append(newNum)
    sortedList = sorted(aList)   # also create a sorted version of aList and call it "sortedList".  Both aList and sortedList are used below

   
    # section 2
    # Do numElments linear searches.  The loop below is run numElements times and each time a linear search is done.
    # To do a linear search we start at the first elment of the list and looks 1 by 1 at the values in the list.
    # If the value we are searching for is found, we terminate the loop and return that value.  
    # If we get to the end of the list and have not found the value it is not in the list, so we return False
    if verbose:
        print("tempNum = " + str(tempNum))
    startTime = time.perf_counter()
    for i in range(numElements):      # do numElments searches, so if binary search time should be N logN
        searchNum = random.randint(1,numElements*10000)
        rVal = linearSearch(aList,tempNum)
        if rVal is not False:
            if verbose:
                print( str(aList[rVal]) + " found at location " + str(rVal))
        else:
            print("Not found in list")
    stopTime = time.perf_counter()
    timeLinearSearch = stopTime - startTime
    if verbose:
        print(f"{(timeLinearSearch):7.4f}"  + " time for linear search")

    # section 3
    # do a numElements binary searches
    # Inside the loop below is the call do binarySarch.  If you set verbose to true above, you will see when the search does/not find the value searched for
    if verbose:
        print("tempNum = " + str(tempNum))
 
    startTime = time.perf_counter()
    for i in range(numElements):    # do numElments searches, so if a linear search time should be N^2
        searchNum = random.randint(1,numElements*10000)
        rVal = binarySearch(sortedList, tempNum)
        if verbose:
            if rVal is not False:
                print( str(sortedList[rVal]) + " found at location " + str(rVal))
            else:
                print("Not found in list")
    stopTime = time.perf_counter()
    timeBinarySearch = stopTime - startTime
    if verbose:
        print(f"{(timeBinarySearch):7.4f}"  + " time for binary search")
    

    # section 4
    # search for duplicates in the unsorted list, print out all duplicates
    startTime = time.perf_counter()    
    duplicateSearch(aList)
    stopTime = time.perf_counter()
    timeDupSearch = stopTime - startTime
    if verbose:
        print(f"{(timeDupSearch):7.4f}"  + " time for duplicateSearch")


    # section 5
    # search for duplicates assuming we have a sorted list
    # IMPORTANT - you need to modify this function above so that it takes advantage of the fact that the list is sorted.
    # In particular, if you are on elment i, and you want to know if it has a duplicate, you only need to look at element i+1 since the 
    # this list is sorted.
    startTime = time.perf_counter()        
    duplicateSearchSorted(sortedList)   # function is expecting a sorted list
    stopTime = time.perf_counter()
    timeDupSearchSorted = stopTime - startTime
    if verbose:
        print(f"{(timeDupSearchSorted):7.4f}"  + " time for duplicateSearchSorted")


    # print out the values for the four algortihms in a tabular format
    print(f"{(numElements):8.0f} \t {(timeLinearSearch):8.4f}  \t{(timeBinarySearch):8.4f} \t{(timeDupSearch):8.5f} \t{(timeDupSearchSorted):8.5f}")
    
    # Check if the sum of times exceeds 60 seconds
    if (timeLinearSearch + timeBinarySearch + timeDupSearch + timeDupSearchSorted) > 60:
        break
    
    # Increase numElements by a larger increment
    numElements += 10000  # You can adjust this increment as needed