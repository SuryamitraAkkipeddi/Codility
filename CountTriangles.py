def solution(A):
    N = len(A)
    count = 0
    
    A.sort()
    for x in range(N):
        z = x + 2
        for y in range(x + 1, N):
            while z < N  and A[x] + A[y] > A[z]:
                z += 1    
            count += z - y - 1

    return count