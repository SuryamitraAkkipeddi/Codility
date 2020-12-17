def solution(A):
    heading = 0       # The sum of A[0] + A[1] + ... + A[P-1]
    tailing = sum(A)  # The sum of A[P] + A[P+1] + ... + A[N-2] + A[N-1]
    for index in xrange(len(A)):
        tailing -= A[index] # The sum of A[P+1] + ... + A[N-2] + A[N-1]
        if heading == tailing:
            # A[0] + A[1] + ... + A[P-1] == A[P+1] + ... + A[N-2] + A[N-1]
            return index
        heading += A[index]
    else:
        # No equilibrium is found.
        return -1