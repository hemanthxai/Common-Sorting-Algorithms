arr = [7, 4, 2, 8, 3, 1, 2, 3]

# Loop through the list starting from the second element (index 1)
for i in range(1, len(arr)):
    key = arr[i]  # Store the current element as the 'key'
    j = i - 1  # Initialize 'j' to the index before 'i'

    # Shift elements of arr[0...i-1] that are greater than 'key' to the right
    while j >= 0 and arr[j] > key:
        arr[j + 1] = arr[j]  # Move element one position to the right
        j -= 1  # Move to the next element on the left

    # Insert the 'key' in its correct position
    arr[j + 1] = key

# Print the sorted list
print(arr)
