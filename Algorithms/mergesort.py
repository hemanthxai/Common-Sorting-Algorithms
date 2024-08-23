def merge(l, r):

    newlst = []
    i = 0
    j = 0

    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            newlst.append(l[i])
            i += 1
        else:
            newlst.append(r[j])
            j += 1

    newlst.extend(l[i:])
    newlst.extend(r[j:])

    return newlst


def mergesort(arr):

    mid = len(arr) // 2

    if len(arr) <= 1:
        return arr
    l = arr[:mid]
    r = arr[mid:]

    l = mergesort(l)
    r = mergesort(r)

    return merge(l, r)


arr = [8, 5, 3, 6, 4, 6, 8, 4, 2, 4]


print(mergesort(arr))
