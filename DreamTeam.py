def solution(A, B, F):
    # write your code in Python 3.6
    diff = [B[i] - A[i] for i in range(len(A))]
    diff.sort()
    return sum(B) - sum(diff[:F])