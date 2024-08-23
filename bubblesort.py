def bubblesort(a: list):

    for i in range(0, len(a) + 1):
        for j in range(0, len(a) - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    return a


a = [9, 3, 1, 5, 7, 4, 9, 6, 2]
print(bubblesort(a))


# a = [9, 3, 1, 5, 7, 4, 9, 6, 2]

# for i in range(0, len(a) + 1):
#     for j in range(0, len(a) - i - 1):
#         if a[j] > a[j + 1]:
#             a[j], a[j + 1] = a[j + 1], a[j]
# print(a)
