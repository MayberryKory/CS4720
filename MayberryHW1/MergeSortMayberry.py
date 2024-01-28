import time


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2 # Do integer division on the length of the array
        L = arr[:mid]
        R = arr[mid:]

        L = merge_sort(L)  # Sorting the first half and updating L
        R = merge_sort(R)  # Sorting the second half and updating R

        return merge(L, R, arr)  # Merge the sorted halves

    return arr  # If the array is of length 1, just return it


def merge(L, R, arr):
    i = j = k = 0

    # Merge elements from L and R into arr
    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements of L, if there are any
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements of R, if there are any
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1

    return arr


# Function for reading file
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


# Main
file_path = input("Enter your file path: ")

array_to_sort = read_file(file_path)
if array_to_sort:
    print("Original Array:", array_to_sort)
    # start a timer for the sort
    start_time = time.perf_counter_ns()
    merge_sort(array_to_sort)
    # end the timer
    end_time = time.perf_counter_ns()
    total_time = end_time - start_time

    print("Sorted Array:", array_to_sort)
    print("Time taken: {} nanoseconds".format(total_time))
