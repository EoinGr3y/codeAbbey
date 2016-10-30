import time

input = [83, 11, 196, 125, 119, 141, 160, 86, 8, 192, 54, 64, 176, 146, 131, 157, 136, 163, 49, 180, 6, 68, 164, 181, 48, 194, 173, 84, 156, 166, 92, 98, 33, 47, 183, 41, 39, 38, 104, 16, 36, 172, 120, 198, 22, 100, 4, 89, 65, 184, 137, 59, 158, 21, 187, 76, 79, 112, 114, 152, 56, 168, 178, 90, 162, 94, 52, 63, 188, 122, 9, 32, 75, 186, 139, 53, 195, 87, 161, 34, 124, 71, 175, 96, 149, 18, 155, 143, 44, 62, 31, 142, 169, 15, 197, 70, 28, 121, 102, 99, 97, 61, 171, 179, 2, 46, 154, 108, 134, 77, 69, 13, 116, 82, 37, 189, 133, 182, 193, 74, 27, 29, 7, 123, 140, 151]

def main():
    result = insertionSort(input)
    print('Result = ' + result)

def insertionSort(array):
    result = ''
    solutionArray = []
    for index in range(0, len(array)):
        if index == 0:
            solutionArray.append(array[index])
        else:
            result += (str(insertAtCorrectIndex(array, index, solutionArray)) + ' ')
    return result

def insertAtCorrectIndex(array, currentIndex, solutionArray):
    for index in range(0, len(solutionArray)):
        if array[currentIndex] < solutionArray[index]:
            numberOfElementsShifted = shiftRemainingArrayAndInsert(array, solutionArray, index, currentIndex)
            return numberOfElementsShifted
        else:
            continue
    solutionArray.append(array[currentIndex])
    return 0

def shiftRemainingArrayAndInsert(array, solutionArray, index, currentIndex):
    temp = array[currentIndex]
    solutionArray[index:index] = [temp]
    numberOfElementsShifted = (len(solutionArray) - 1) - index
    return numberOfElementsShifted

main()
