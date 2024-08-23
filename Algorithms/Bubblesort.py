def bubblesort(a: list):
    # Loop through each element in the list
    for i in range(len(a)):
        # Inner loop to compare adjacent elements
        for j in range(0, len(a) - i - 1):
            # If the current element is greater than the next, swap them
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a  # Return the sorted list


arr = [9, 3, 1, 5, 7, 4, 9, 6, 2]

print(bubblesort(arr))
