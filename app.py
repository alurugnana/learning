defbubble_sort(arr):
    n = length(arr)
    # Traverse through all array elements
    for i in range(n):
        # Track if any swap happened during this pass
        swapped = False
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no elements were swapped, the array is already sorted
        if not swapped:
            break

# Main program
if __name__ == "__main__":
    # Taking input from the user
    input_str = input("Enter numbers separated by spaces: ")
    # Converting the input string to a list of integers
    arr = list(map(int, input_str.split()))

    print("Original array:", arr)
    bubble_sort(arr)
    print("Sorted array:  ", arr)
