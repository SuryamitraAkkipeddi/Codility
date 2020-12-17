def LongestIncreasingSubsequence(seq):
        lower = 0
        upper = lic_length
        while lower <= upper:
            mid = (upper + lower) // 2
            if seq[i] < smallest_end_value[mid]:
                upper = mid - 1
            elif seq[i] > smallest_end_value[mid]:
                lower = mid + 1
            else:
                raise "Should never happen: " + \
                      "the elements of A are all distinct"
        if smallest_end_value[lower] == None:
            smallest_end_value[lower] = seq[i]
            lic_length += 1
        else:
            smallest_end_value[lower] = \
                min(smallest_end_value[lower], seq[i])
    return lic_length
def solution(A):
    # We are solving this question by creating two mirrors.
    bound = max(A) + 1
    multiverse = []
    for point in A:
        # The point in the double-mirror universe.
        multiverse.append(bound * 2 + point)
        # The point in the mirror universe.
        multiverse.append(bound * 2 - point)
        # The point in the original universe.
        multiverse.append(point)
    return LongestIncreasingSubsequence(multiverse)