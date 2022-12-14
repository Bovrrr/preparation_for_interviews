import random


# считываю массив
array = list(map(float, input().split()))


def get_pivot(arr, l, r):
    # беру медиану 3х рандомных элементов
    idxs = [random.randint(l, r) for _ in range(3)]
    a = [arr[i] for i in idxs]
    return sum(a) - (max(a) + min(a))

def get_pivot_random(arr, l, r):
    idx = random.randint(l, r)
    return arr[idx]


def split(arr, l, r, x):
    # переставляет элементы относительно опорного
    # возвращает середины подмассива для следующего разбиения
    i, j = l, r
    while i <= j:
        while arr[i] < x:
            i += 1
        while arr[j] > x:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
    return i, j


def quick_sort(arr, l, r):
    if r - l <= 1:
        return
    x = get_pivot(arr, l, r)
    m2, m1 = split(arr, l, r, x)

    quick_sort(arr, l, m1)
    quick_sort(arr, m2, r)



quick_sort(array, 0, len(array) - 1)
print(array)
