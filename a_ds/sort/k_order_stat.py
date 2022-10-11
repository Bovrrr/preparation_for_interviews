import random


k = int(input())
array = list(
    map(
        float,
        input().split(),
    )
)


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


def find_k_order_stat(arr, l, r, k):
    if r <= l:
        return arr[k]

    x = get_pivot_random(arr, l, r)
    m2, m1 = split(arr, l, r, x)

    if k < m2:
        return find_k_order_stat(arr, l, m1, k)
    else:
        return find_k_order_stat(arr, m2, r, k)


x = find_k_order_stat(array, 0, len(array) - 1, k)
print(x)
