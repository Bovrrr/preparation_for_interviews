# целочисленный бин поиск
array = list(
    map(
        int,
        input().split(),
    )
)

# вещественный бин поиск
# array = list(
#     map(
#         int,
#         input().split(),
#     )
# )

x = int(input())
print(f"arr = {array}")
print(f"x = {x}")


def bin_search(arr, l, r, x):
    if l == r - 1:
        return arr[l] == x
    m = (l + r) // 2

    if arr[m] == x:
        return True
    elif arr[m] < x:
        return bin_search(arr, m, r, x)
    elif arr[m] > x:
        return bin_search(arr, l, m, x)


elem_is_in_array = bin_search(array, 0, len(array) - 1, x)

answ = ""
if elem_is_in_array:
    answ = f"{x} is in massive"
else:
    answ = f"{x} is not in massive"

print(answ)
