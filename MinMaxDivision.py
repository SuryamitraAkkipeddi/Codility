    # write your code in Python 3.6
def check(A, K, max_block_sum):
    block_sum = 0
    count = 0

    for elem in A:
        if block_sum + elem > max_block_sum:
            block_sum = elem
            count += 1
        else:
            block_sum += elem
        
        if count >= K:
            return False

    return True


def solution(K, M, A):

    lower_bound = max(A)
    upper_bound = sum(A)

    if K == 1:
        return upper_bound

    if K >= len(A):
        return lower_bound

    while lower_bound <= upper_bound:
        possible_candidate = (lower_bound + upper_bound) // 2

        if check(A, K, possible_candidate):
            upper_bound = possible_candidate - 1
        else:
            lower_bound = possible_candidate + 1

    return lower_bound