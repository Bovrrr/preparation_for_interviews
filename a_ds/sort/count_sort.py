array = list(map(int, input().split()))


def count_sort(arr):
    max_elem = int(-1e10)
    min_elem = int(1e10)

    for elem in arr:
        if elem > max_elem:
            max_elem = elem
        if elem < min_elem:
            min_elem = elem

    m = max_elem - min_elem + 1
    c = [0] * m

    for i in range(len(arr)):
        arr[i] -= min_elem

    for elem in arr:
        c[elem] += 1

    i = 0
    j = 0
    while i < len(arr):
        while c[j] > 0:
            arr[i] = j + min_elem
            c[j] -= 1
            i += 1
        j += 1


count_sort(array)
print(array)
