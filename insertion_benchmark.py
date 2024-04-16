#!/usr/bin/pypy3
'''Benchmarking Insertion Sort

After reading the correctness proof of insertion sort during discussion for week 1,
Konstantinos is wondering how many times line 6 is performed for a given array.
He could simply count, but it took too long for big arrays, so instead he wants
you to write a faster algorithm to compute that result.
'''

temp = [0] * 10000000

def merge(array, left, mid, right):
    i, j, k = left, mid, left
    swaps = 0
    
    while (i < mid and j <= right):
        if (array[i] <= array[j]):
            temp[k] = array[i]
            i += 1
        else:
            temp[k] = array[j]
            j += 1
            swaps += mid - i
        k += 1
    
    while (i < mid):
        temp[k] = array[i]
        i += 1
        k += 1
    
    while (j <= right):
        temp[k] = array[j]
        j += 1
        k += 1
    
    for x in range(left, right + 1):
        array[x] = temp[x]
    
    return swaps

def mergeSort(array, left, right):
    swaps = 0
    if left < right:
        mid = (left + right) // 2
        swaps += mergeSort(array, left, mid)
        swaps += mergeSort(array, mid + 1, right)
        swaps += merge(array, left, mid + 1, right)
    return swaps

def solve(N, array):
    # Compute the correct number of swaps (inversions) that
    # insertion sort would perform on this array with N elements.
    return mergeSort(array, 0, N-1)

def main():
    N = int(input())
    array = [int(i) for i in input().split()]
    solution = solve(N, array)
    print(solution)

if __name__ == '__main__':
    main()
