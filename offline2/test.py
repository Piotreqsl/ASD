def largest_container(A):
    def partition(arr, p, r, perm):
        i, j = p - 1, p
        while j < r:
            if arr[j] < arr[r]:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
                perm[i], perm[j] = perm[j], perm[i]
            j += 1
        arr[i + 1], arr[r] = arr[r], arr[i + 1]
        perm[i+1], perm[r] = perm[r], perm[i+1]
        return i + 1

    def qs_rec(arr, p, r, perm):
        while p < r:
            q = partition(arr, p, r, perm)
            if q - p > r - q:
                qs_rec(arr, q + 1, r, perm)
                r = q - 1
            else:
                qs_rec(arr, p, q - 1, perm)
                p = q + 1

    ln = len(A)
    starts = [A[i][0] for i in range(ln)]
    start_indexes = [i for i in range(ln)]
    qs_rec(starts, 0, ln - 1, start_indexes)
    start_inds_rev = [0]*ln
    for i in range(ln):
        start_inds_rev[start_indexes[i]] = i

    ends = [A[i][1] for i in range(ln)]
    end_indexes = [i for i in range(ln)]
    qs_rec(ends, 0, ln - 1, end_indexes)
    end_inds_rev = [0]*ln
    for i in range(ln):
        end_inds_rev[end_indexes[i]] = i

    max_container = 0
    max_range = tuple()
    for i in range(ln):
        f = start_inds_rev[i]
        while f > 0 and starts[f - 1] == starts[f]:
            f -= 1

        g = end_inds_rev[i]
        while g < ln - 1 and ends[g + 1] == ends[g]:
            g += 1

        conts = g - f
        if conts > max_container:
            max_container = conts
            max_range = A[i]

    print(max_range, max_container)


largest_container([(1, 3), (5, 6), (2, 6), (2, 3), (3, 5), (4, 6), (2, 4), (1, 6), (3,15), (1,25)])