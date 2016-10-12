numbers = [11, 21, 10, 2, 6, 18, 7, 4, 15, 13, 8, 12, 3, 14, 5, 17, 16, 1, 9, 22, 19, 20]

def main():
    passAndSwapCount = sortArray(numbers, 0, 0)
    print('Result: ' + str(passAndSwapCount))
    return

def sortArray(array, totalSwapCount, passCount):
    hasSwapped = False
    result = '0 0'
    for index in range(len(array) - 1):
        if array[index] > array[index+1]:
            swapElements(array, index, index + 1)
            totalSwapCount += 1
            hasSwapped = True
    passCount += 1
    if hasSwapped:
        return sortArray(array, totalSwapCount, passCount)
    else:
        print('Array: ' + str(array))
        result = str(str(passCount) + ' ' + str(totalSwapCount))
        print('returning value of ' + result)
    return result

def swapElements(array, index, swapIndex):
    temp = array[index]
    array[index] = array[swapIndex]
    array[swapIndex] = temp
main()
