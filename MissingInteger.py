def solution(A):
    missing = 1
    for elem in sorted(A):
        if elem == missing:
            missing += 1
        if elem > missing:
            break
    return missing