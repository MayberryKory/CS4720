import time


def bubble_sort(arr):
    # Get the length of the array to be used as the maximum value in the loops
    n = len(arr)

    # The outer loop represents each pass through the array.
    # After each pass, the largest element in the unsorted part will bubble up to its correct position.
    for i in range(n):
        # The inner loop compares adjacent elements and swaps them if they are in the wrong order.
        # The range of the inner loop decreases with each pass, as the last elements are already sorted.
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if the element on the left is greater than the element on the right
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return [int(line.strip()) for line in file]
    except FileNotFoundError:
        print("File not found. Please check the file path.")
        return []
    except ValueError:
        print("File contains non-numeric data.")
        return []

file_path = input("Enter your file path: ")

array_to_sort = read_file(file_path)
if array_to_sort:
    print("Original Array:", array_to_sort)
    print("\nSorting.......")
    start_time = time.perf_counter_ns()
    bubble_sort(array_to_sort)
    end_time = time.perf_counter_ns()
    total_time = end_time - start_time

    print("Sorted Array:", array_to_sort)
    print("Time taken: {} nanoseconds".format(total_time))
