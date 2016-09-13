numbers = [154, 66, 139, 178, 156, 150, 44, 195, 67, 122, 20, 176, 129, 144, 115, 91, 102, 34, 134, 2, 175, 118, 82, 99, 96, 125, 114, 50, 190, 54, 28, 147, 4, 72, 142, 71, 22, 65, 137, 171, 84, 101, 29, 191, 130, 62, 126, 131, 37, 121, 49, 194, 187, 181, 93, 123, 188, 199, 86, 73, 113, 186, 141, 31, 3, 104, 161, 40, 26, 11, 158, 46, 155, 180, 149, 36, 167, 17, 159, 140, 179, 128, 21, 1, 133, 52, 74, 132, 77, 117, 160, 75, 6, 59, 76, 185, 9, 111, 153, 127, 112, 45, 24, 90, 88, 97, 162, 106, 85, 57, 94, 18, 10, 12, 7, 32, 100, 173, 145, 58, 189, 53, 13, 56, 168, 35, 174, 19]

def main():
    resultArray = numbers
    sortArray(resultArray, numbers)
    print('Result:' + str(resultArray))
    return

def sortArray(resultArray, array):
    length = len(array)
    if length == 1:
        print('Finished sorting')
        return
    else:
        maxIndex = getMaxIndex(array)
        swapWithLastElement(maxIndex, array)
        populateResultArray(resultArray, array)
        sortArray(resultArray, array[0:length - 1])
        return

def getMaxIndex(array):
    maxIndex = 0
    max = array[0]
    for index in range(len(array)):
        if array[index] > max:
            maxIndex = index
            max = array[index]
    return maxIndex

def swapWithLastElement(index, array):
    copyOfLastElement = array[len(array) - 1]
    array[len(array) - 1] = array[index]
    array[index] = copyOfLastElement

def populateResultArray(resultArray, array):
    length = len(array)
    resultArray[0:length] = array

main()
