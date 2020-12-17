def solution(A):
    # write your code in Python 2.7
    N = len(A)

    if N == 0:
        return 0

    A.sort()

    distinct = 1
    for ind in range(1, N):
        if A[ind] != A[ind - 1]:
            distinct += 1

    return distinct
