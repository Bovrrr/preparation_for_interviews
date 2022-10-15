from math import log2


def ter_search(arr, l, r, f, eps):
    itn = int(log2((r - l) / eps))

    for i in range(itn):
        m1 = (l + r) / 3
        m2 = 2 * (l + r) / 3
        if f(m1) < f(m2):
            r = m2
        else:
            l = m1

    return r
