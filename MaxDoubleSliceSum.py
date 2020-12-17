def solution(A):

    # write your code in Python 3.6
    L_slice, until_now, once_total = 0, 0, 0

    for Z in range(3, len(A)):
        L_slice = max(0, A[Z-2] + L_slice)
        until_now = max(L_slice, A[Z-1] + until_now)
        once_total = max(until_now, once_total)

    return once_total