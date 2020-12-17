def solution(A):
    abs_distinct = 1
    current = max(abs(A[0]), abs(A[-1]))
    index_head = 0
    index_tail = len(A)-1
    while index_head <= index_tail:
        # We travel the array from the greatest
        # absolute value to the smallest.
        former = abs(A[index_head])
        if former == current:
            # Skip the heading elements, whose
            # absolute values are the same with
            # current recording one.
            index_head += 1
            continue
        latter = abs(A[index_tail])
        if latter == current:
            # Skip the tailing elements, whose
            # absolute values are the same with
            # current recording one.
            index_tail -= 1
            continue
        # At this point, both the former and
        # latter has different absolute value
        # from current recorded one.
        if former >= latter:
            # The next greatest value is former
            current = former
            index_head += 1
        else:
            # The next greatest value is latter
            current = latter
            index_tail -= 1
        # Meet with a new absolute value
        abs_distinct += 1
    return abs_distinct