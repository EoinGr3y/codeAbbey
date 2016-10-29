input = [131, 63, 81, 120, 96, 83, 3, 107, 78, 74, 98, 150, 165, 41, 156, 132, 52, 180, 20, 82, 100, 32, 34, 50, 88, 15, 109, 146, 23, 77, 86, 179, 197, 181, 199, 89, 140, 186, 91, 40, 28, 196, 159, 39, 176, 76, 12, 154, 126, 99, 169, 35, 45, 191, 133, 122, 112, 119, 59, 174, 148, 115, 192, 135, 6, 33, 162, 29, 31, 102, 114, 105, 8, 14, 42, 65, 142, 87, 2, 61, 19, 175, 11, 85, 44, 48, 172, 73, 72, 153, 185, 58, 166, 198, 9, 57, 183, 38, 139, 70, 136, 141, 155, 106, 10, 24, 193, 62, 160, 16, 51, 49, 5, 95, 79, 143, 149, 80, 1, 173, 93, 167, 194, 53, 90, 182, 97, 124]

def main():
    result = insertionSort(input)


def insertionSort(array):
    for index in range(1, len(array) - 1):
        insertAtCorrectIndex(array, index)

def insertAtCorrectIndex(array, currentIndex):
    for index in range(1, currentIndex - 1):
        if array[currentIndex] < array[index]:
            shiftRemainingArray(index, array)

def shiftRemainingArray(index)


main()
