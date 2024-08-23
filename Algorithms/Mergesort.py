def merge(l, r):
    # Initialize an empty list to store the merged result
    newlst = []
    # Initialize pointers for both left (l) and right (r) sublists
    i = 0
    j = 0

    # Loop through both sublists until one is exhausted
    while i < len(l) and j < len(r):
        # Compare elements from both sublists and append the smaller one to 'newlst'
        if l[i] < r[j]:
            newlst.append(l[i])
            i += 1  # Move the pointer in the left sublist
        else:
            newlst.append(r[j])
            j += 1  # Move the pointer in the right sublist

    # Append any remaining elements from the left sublist (if any)
    newlst.extend(l[i:])
    # Append any remaining elements from the right sublist (if any)
    newlst.extend(r[j:])

    return newlst  # Return the merged list

def mergesort(arr):
    # Base case: if the list has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr

    # Find the middle point to divide the array into two halves
    mid = len(arr) // 2
    # Recursively sort the first half
    l = mergesort(arr[:mid])
    # Recursively sort the second half
    r = mergesort(arr[mid:])

    # Merge the two sorted halves
    return merge(l, r)

# Sample
arr = [8, 5, 3, 6, 4, 6, 8, 4, 2, 4]

# Call the mergesort function and print the sorted list
print(mergesort(arr))
