import math

class ListInvalidInputException(Exception):
    pass
class NumberInvalidInputException(Exception):
    pass

def binarySearch(elementList, firstIndex, lastIndex, searchElement):
    mid = (firstIndex + lastIndex) / 2

    if (firstIndex > lastIndex):
        print "Element not found"

    elif (searchElement > elementList[mid]):
        firstIndex = mid + 1
        binarySearch(elementList, firstIndex, lastIndex, searchElement)

    elif (searchElement < elementList[mid]):
        lastIndex = mid - 1
        binarySearch(elementList, firstIndex, lastIndex, searchElement)

    else:
        print "element is present at index " + str(mid)




myList = sorted([2,324,454,543,652,875])    #making sure they are sorted
try:


    searchElement = raw_input("enter search element:")
    '''if math.isnan(searchElement):
        raise NumberInvalidInputException'''


    binarySearch(myList, 0, len(myList) - 1, float(searchElement))
except ListInvalidInputException:
    print("List elements contains wrong values")
except NumberInvalidInputException:
    print("You should enter a number")