import math

class ElementNotFoundException(Exception):
    pass
class NumberInvalidInputException(Exception):
    pass

def binarySearch(elementList, firstIndex, lastIndex, searchElement):
    try:
        mid = (firstIndex + lastIndex) / 2

        if (firstIndex > lastIndex):
            raise ElementNotFoundException

        elif (searchElement > elementList[mid]):
            firstIndex = mid + 1
            binarySearch(elementList, firstIndex, lastIndex, searchElement)

        elif (searchElement < elementList[mid]):
            lastIndex = mid - 1
            binarySearch(elementList, firstIndex, lastIndex, searchElement)

        else:
            print "element is present at index " + str(mid)

    except ElementNotFoundException:
        print("Element Not found")


myList = sorted([2,324,454,543,652,875])    #making sure they are sorted
try:


    searchElement = raw_input("enter search element:")
    '''if math.isnan(searchElement):
        raise NumberInvalidInputException'''

#function call here
    binarySearch(myList, 0, len(myList) - 1, float(searchElement))

except NumberInvalidInputException: #to check valid input
    print("You should enter a number")