def solution(A, B):
    # write your code in Python 3.6
    max_num  = max(A)
    N = len(A)
    fib_table = [0, 1] + [-1]*max_num
    result = [0]*N

    for idx in range(2, max_num + 2):
        fib_table[idx] = fib_table[idx - 2] + fib_table[idx - 1]

    fib_table = fib_table[2:]

    for idx in range(N):
        value = fib_table[A[idx] - 1]
        result[idx] = value & ((1 << B[idx]) - 1)

    return result