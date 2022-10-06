input_array = list(map(int, input().split()))


def insertion_sort(array):
    size = len(array)
    for i in range(1, size):
        for j in range(i, 0, -1):
            if array[j - 1] > array[j]:
                array[j - 1], array[j] = array[j], array[j - 1]


insertion_sort(input_array)
print(input_array)
