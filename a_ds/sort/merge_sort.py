array = list(map(float, input().split()))


def merge(arr1, arr2):
    size1 = len(arr1)
    size2 = len(arr2)

    arr_res = [0.0] * (size1 + size2)

    i, j = [0] * 2
    while i + j < size1 + size2:
        if j == size2 or (i < size1 and arr1[i] < arr2[j]):
            arr_res[i + j] = arr1[i]
            i += 1
        else:
            arr_res[i + j] = arr2[j]
            j += 1

    del arr1, arr2

    return arr_res


def merge_sort(arr):
    arr_size = len(arr)
    if arr_size == 1:
        return arr

    m = arr_size // 2
    # срезы создают копии листов
    arr1 = merge_sort(arr[:m])
    arr2 = merge_sort(arr[m:])

    return merge(arr1, arr2)


sorted_array = merge_sort(array)
print(sorted_array)
