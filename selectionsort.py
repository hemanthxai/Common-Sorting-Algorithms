# a = [9, 3, 1, 5, 7, 4, 9, 6, 2]


# for i in range(len(a)):
#     minn = i
#     for j in range(i + 1, len(a)):
#         if a[j] < a[minn]:
#             minn = j

#     a[minn], a[i] = a[i], a[minn]

# print(a)

from typing import List


def selectionsort(a: List) -> List:
    print(f"unsorted array is:\n{a}\n")
    for i in range(len(a)):
        min = i
        for j in range(i + 1, len(a)):
            if a[j] < a[min]:
                min = j
        a[min], a[i] = a[i], a[min]
        print(a)
    print("\nhence sorted array is")
    return a


a = [9, 3, 1, 5, 7, 4, 9, 6, 2]
print(selectionsort(a))
