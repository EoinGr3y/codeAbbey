numbers = [109, 106, 8, 113, 159, 141, 42, 173, 7, 14, 192, 156, 50, 88, 182, 28, 74, 69, 35, 167, 123, 16, 70, 171, 36, 194, 90, 37, 199, 142, 175, 112, 101, 116, 153, 75, 138, 4, 98, 165, 78, 1, 45, 91, 17, 115, 62, 23, 150, 56, 187, 24, 111, 129, 198, 31, 176, 105, 39, 136, 193, 155, 52, 131, 96, 117, 97, 82, 9, 196, 135, 147, 126, 48, 134, 149, 64, 148, 95, 103, 59, 125, 18, 21, 54, 118, 132, 93, 80, 19, 168, 172, 180, 114, 84, 166, 30, 60, 185, 26, 162, 40, 13, 89, 81, 152, 164, 94, 47, 100, 67, 169, 197, 63, 58, 83, 61, 102, 181, 183, 73, 79, 119]

def main():
    maxIndexString = ''
    resultArray = numbers
    maxIndexString = sortArray(resultArray, numbers, maxIndexString)
    print('Result:' + str(resultArray))
    print('Max index string: ' + maxIndexString)
    return

def sortArray(resultArray, array, maxIndexString):
    length = len(array)
    if length == 1:
        print('Finished sorting')
        return maxIndexString
    else:
        maxIndex = getMaxIndex(array)
        maxIndexString += ' ' + str(maxIndex)
        swapWithLastElement(maxIndex, array)
        populateResultArray(resultArray, array)
        maxIndexString = sortArray(resultArray, array[0:length - 1], maxIndexString)
        return maxIndexString

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
