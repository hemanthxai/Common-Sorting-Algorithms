def selectionsort(a):
    # Iterate over the entire list
    for i in range(len(a)):
        # Assume the current index 'i' has the minimum value
        min = i
        
        # Iterate over the rest of the list to find the actual minimum value
        for j in range(i + 1, len(a)):
            # Update 'min' if a smaller element is found
            if a[j] < a[min]:
                min = j
        
        # Swap the found minimum element with the element at index 'i'
        a[min], a[i] = a[i], a[min]
        
        # Print the list after each swap to show progress
        print(a)

    return a  # Return the sorted list

# Sample 
a = [9, 3, 1, 5, 7, 4, 9, 6, 2]

# Call the selectionsort function and print the sorted list
print(selectionsort(a))
