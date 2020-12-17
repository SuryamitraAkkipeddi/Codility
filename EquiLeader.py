from collections import Counter

def solution(A):
    # write your code in Python 3.6
    result = 0
    candidate, candidate_count  = Counter(A).most_common()[0]

    
    left = 0
    for idx, value in enumerate(A):
            
        if value == candidate:
            left += 1
            
        if left > (idx + 1) // 2 and (candidate_count - left) > (len(A) - (idx + 1)) // 2:
            result +=1

    return result