def findMedian(A, B, AFrom, ATo, BFrom, BTo):
    # A classic question: find median in two sorted array
    # For more details, please Google it.
    result = 0
    while True:
        # AMid and BMid are current medians for A and B
        # sub-arrays respectively
        AMid = A[(AFrom+ATo)/2]
        BMid = B[(BFrom+BTo)/2]
        if AFrom == ATo:
            # Only one element in A's sub-array. No need
            # for further iteration
            if AMid < B[(BFrom+BTo)/2]:
                result = B[(BFrom+BTo)/2]
            elif AMid > B[(BFrom+BTo)/2+1]:
                result = B[(BFrom+BTo)/2+1]
            else:
                result = AMid
            break
        elif BFrom == BTo:
            # Only one element in B's sub-array. No need
            # for further iteration
            if BMid < A[(AFrom+ATo)/2]:
                result = A[(AFrom+ATo)/2]
            elif BMid > A[(AFrom+ATo)/2+1]:
                result = A[(AFrom+ATo)/2+1]
            else:
                result = BMid
            break
        elif AMid == BMid:
            # Median is found
            result = AMid
            break
        elif AMid > BMid:
            # Median must be in the left part of A's
            # sub-array OR the right part of B's sub-
            # array
            reduced = (min(ATo-AFrom, BTo-BFrom)+1)/2
            ATo -= reduced
            BFrom += reduced
        else:
            # Median must be in the right part of A's
            # sub-array OR the left part of B's sub-
            # array
            reduced = (min(ATo-AFrom, BTo-BFrom)+1)/2
            AFrom += reduced
            BTo -= reduced
    return result
def solution(A, B, P, Q, R, S):
    questionCount = len(P)
    answer = [0] * questionCount
    for i in xrange(questionCount):
        # Find the median for each query
        answer[i] = findMedian(A, B, P[i], Q[i], R[i], S[i])
    answer.sort()
    return answer[questionCount/2]