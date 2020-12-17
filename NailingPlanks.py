    # write your code in Python 3.6
BEGIN_POS = 0
END_POS = 1
NAIL_COUNT_ADDRESS = 0
HIT_POS = 1

def binary_search_nail_pos(nails, plank):
    beg = 0
    end = len(nails) - 1
    ptr = -1

    while beg <= end:
        mid = (beg + end) // 2

        if nails[mid][HIT_POS] < plank[BEGIN_POS]:
            beg = mid + 1
        elif nails[mid][HIT_POS] > plank[END_POS]:
            end = mid - 1
        else:
            end = mid - 1
            ptr = mid

    return ptr

def solution(A, B, C):

    count = 0
    planks = zip(A, B)
    nails = sorted(enumerate(C), key =  lambda var: var [HIT_POS])

    for plank in planks:
        nail_pos =  binary_search_nail_pos(nails, plank)

        if nail_pos == -1:
            return -1

        nail_count = nails[nail_pos][NAIL_COUNT_ADDRESS]

        while nail_pos < len(nails) and nails[nail_pos][HIT_POS] <= plank[END_POS]:
            nail_count = min(nail_count, nails[nail_pos][NAIL_COUNT_ADDRESS])

            if nail_count <= count:
                break
            
            nail_pos += 1

        count = max(count, nail_count)

    return count + 1