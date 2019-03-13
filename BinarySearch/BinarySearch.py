import os
import sys

def binary_search(value, array):
    return binary_search_rec(value, array, 0, len(array)-1)

def binary_search_rec(value, array, lo, hi):
    mid = (lo+hi)/2
    if(value < array[lo] or value > array[hi]):
        return -1
    if (array[mid] < value):
        return binary_search_rec(value, array, mid+1, hi)
    elif (array[mid] > value):
        return binary_search_rec(value, array, lo, mid-1)
    else:
        return array[mid]

def main():
    array = sys.stdin.readline().split(" ")
    array = [int(i) for i in array]
    array.sort()
    line = sys.stdin.readline()
    while(line != ""):
        value_to_search = int(line)
        print(binary_search(value_to_search, array))
        line = sys.stdin.readline()
main()
