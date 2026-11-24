def partition_point(start, end, pred):
    if end - start == 0:
        return start
    mid = (start + end) // 2
    if pred(mid):
        return partition_point(mid + 1, end, pred)
    else:
        return partition_point(start, mid, pred)

def partition_stable(xs, start, end, pred):
    if (end - start) == 0:
        return start
    if (end - start) == 1:
        if pred(xs[start]):
                return end
        else:
                return start
    mid = (start + end) // 2
    a = bipartition_stable(xs, start, mid, pred)
    b = bipartition_stable(xs, mid, end, pred)
    reverse(xs, a, mid)
    reverse(xs, mid, b)
    reverse(xs, a, b)
    return a + b - mid

# [ STABLE pred(x) ][ !pred(x) ]
#                   ^writer
def partition_left(xs, start, end, pred):
        writer = start
        for i in range(start, end):
                if pred(xs[i]):
                        xs[writer], xs[i] = xs[i], xs[writer]
                        writer += 1
        return writer

# [ !pred(x) ][ STABLE pred(x) ]
#             ^writer
def partition_right(xs, start, end, pred):
        writer = end
        for i in reversed(range(start, end)):
                if pred(xs[i]):
                        writer -= 1
                        xs[writer], xs[i] = xs[i], xs[writer]
        return writer

def quicksort(xs, start, end):
    if end - start <= 1:
        return
    pivot = xs[randrange(start, end)]
    mid = partition_left(xs, start, end, lambda x: x < pivot)
    partition_left(xs, mid, end, lambda x: x == pivot)
    quicksort(xs, start, mid)
    quicksort(xs, mid + 1, end)


def quickselect(k, xs, start, end):
    pivot = xs[randrange(start, end)]
    mid = partition_left(xs, start, end, lambda x: x < pivot)
    partition_left(xs, mid, end, lambda x: x == pivot)
    if k < mid:
        return quickselect(k, xs, start, mid)
    if mid < k:
        return quickselect(k, xs, mid + 1, end)
    return xs[mid]