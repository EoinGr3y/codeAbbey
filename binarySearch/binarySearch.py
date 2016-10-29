import math
import time

def main():
    input = initialiseInput()
    result = ''
    for array in input:
        result += str(binarySearch(array, 0, 100) + ' ')
    print(result)

def binarySearch(inputArray, min, max):
    A = inputArray[0]
    B = inputArray[1]
    C = inputArray[2]
    D = inputArray[3]
    mid = (min + max) / 2
    minFunctionResult = calculateFunction(A, B, C, D, min)
    maxFunctionResult = calculateFunction(A, B, C, D, max)
    midFunctionResult = calculateFunction(A, B, C, D, mid)
    if approxEqual(midFunctionResult, 0):
        return str(mid)
    elif midFunctionResult < 0:
        return binarySearch(inputArray, mid, max)
    else:
        return binarySearch(inputArray, min, mid)

def initialiseInput():
    list = []
    list.append([18.06423386, 0.91321805, 1444.08586782, -572.90511693])
    list.append([1.23791531, 1.86064586, 1810.91448004, 1236.51865065])
    list.append([16.55507676, 0.00128308, 43.71401018, 1165.31121041])
    list.append([17.45559281, 0.36300442, 182.83631102, 612.69649010])
    list.append([3.56028640, 1.04478170, 1168.27716826, 297.63835240])
    list.append([15.16114324, 0.26394231, 597.02863758, 841.93237772])
    return list

def calculateFunction(A, B, C, D, x):
    return A * x + B * math.sqrt(x ** 3) - C * math.exp(-x / 50) - D

def approxEqual(a, b):
    return abs(a - b) <= 0.0000001

main()
