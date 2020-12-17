def solution(N):
    candidate = 1
    result = 0
    while candidate * candidate < N:
        # N has two factors: candidate and N // candidate
        if N % candidate == 0:      result += 2
        candidate += 1
    # If N is square of some value.
    if candidate * candidate == N:  result += 1
    return result