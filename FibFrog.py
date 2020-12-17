def solution(A):
    # write your code in Python 3.6
    A.append(1)
    N = len(A)

    fib_table = [0]*27
    fib_table[1] = 1

    for idx in range(2, 27):
        fib_table[idx] = fib_table[idx-1] + fib_table[idx-2]
        if fib_table[idx] > N:
            break
    
    fib_table = fib_table[2:idx]

    next_try = [-1]*N
    for idx in range(len(fib_table)):
        next_try[fib_table[idx] - 1] = 1

    for idx, leaf in enumerate(A):
        if next_try[idx] > 0 and leaf == 1:
            for fib in fib_table:
                if idx + fib >= N:
                    break
                if next_try[idx+fib] < 0 or next_try[idx+fib] > next_try[idx]+1:
                    next_try[idx+fib] = next_try[idx]+1

    return next_try[-1]
