array = list(
    map(
        int,
        input().split(),
    )
)
x = int(input())

# инвариант (l, r]


def lower_bound_non_recursive(arr, x):
    l, r = -1, len(arr) - 1
    while r - l > 1:
        m = (l + r) // 2
        if x <= arr[m]:
            r = m
        else:
            l = m

    return r


def upper_bound_non_recursive(arr, x):
    return lower_bound_non_recursive(arr, x + 1)


def lower_bound(arr, l, r, x):
    if r - 1 == l:
        return r
    m = (l + r) // 2

    if x <= arr[m]:
        return lower_bound(arr, l, m, x)
    else:
        return lower_bound(arr, m, r, x)


def upper_bound(arr, l, r, x):
    return lower_bound(arr, l, r, x + 1)


l_b_x = lower_bound(array, -1, len(array) - 1, x)
l_b_x_nr = lower_bound_non_recursive(array, x)
u_b_x = upper_bound(array, -1, len(array) - 1, x)
u_b_x_nr = upper_bound_non_recursive(array, x)
print(array)
print(list(range(len(array))))
print(l_b_x)
print(l_b_x_nr)
print(u_b_x)
print(u_b_x_nr)
