def solution(K, A):
    N = len(A)
    maxINT = 2000000000
    maxQ = [0] * (N + 1)
    posmaxQ = [0] * (N + 1)
    minQ = [0] * (N + 1)
    posminQ = [0] * (N + 1)
    firstMax, lastMax = 0, -1
    firstMin, lastMin = 0, -1
    i, j, result = 0, 0, 0
    while i < N:
        while j < N:
            # added new maximum element
            while (lastMax >= firstMax and maxQ[lastMax] <= A[j]):
                lastMax -= 1
            lastMax += 1
            maxQ[lastMax] = A[j]
            posmaxQ[lastMax] = j
            # added new minimum element
            while (lastMin >= firstMin and minQ[lastMin] >= A[j]):
                lastMin -= 1
            lastMin += 1
            minQ[lastMin] = A[j]
            posminQ[lastMin] = j
            if (maxQ[firstMax] - minQ[firstMin] <= K):
                j += 1
            else:
                break
        if posminQ[firstMin] < posmaxQ[firstMax]:
            result += (j - i + j - posminQ[firstMin]) * (posminQ[firstMin] - i + 1)
            i = posminQ[firstMin] + 1
            firstMin += 1
        else:
            result += (j - i + j - posmaxQ[firstMax]) * (posmaxQ[firstMax] - i + 1)
            i = posmaxQ[firstMax] + 1
            firstMax += 1
        if result >= maxINT:
            return maxINT/2
    return result/2