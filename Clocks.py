def lexicographically_min(A):
    ''' Return the given array in a Lexicographically Minimal
        Rotation (LMR)
    '''
    double_array = A + A
    array_len = len(A)
    start = 0       # The start point of the LMR so far
    testing = 1     # The start point of the next trying rotation
    offset = 0      # The offset in comparing two rotations
    while testing < array_len:
        if offset == array_len:
            # Pass all the test, the "start" begins the
            # lexicographically minimal array rotation
            break
        if double_array[start+offset] == double_array[testing+offset]:
            # So far, both rotations have the same lexicographically
            # value. So we move on to compare the next element.
            offset += 1
        elif double_array[start+offset] < double_array[testing+offset]:
            # The current trying rotation is lexicographically larger
            # The start point of LMR could not in the range
            # [testing, testing + offset]
            testing += offset + 1
            offset = 0
        else:
            # The current trying rotation is lexicographically smaller
            # The start point of LMR could not in the range
            # [start, start + offset]. AND
            # all the points in [start+1, testing-1] have been tested
            # not to be the start point of LRM
            start = max( start+offset+1, testing )
            testing = start + 1
            offset = 0
    return A[start:]+A[:start]
def solution(A, P):
    columns = len(A[0])
    same_after_rotation = []
    # Compute the Lexicographically Minimal Rotation for the hands'
    # distance array. And use the LMR array as signature to identify
    # the same clocks
    for row_index in xrange(len(A)):
        A[row_index].sort()         # Make the hands in order
        distance = [(A[row_index][column_index] -
                            A[row_index][column_index-1]) % P
                            for column_index in xrange(columns)]
        same_after_rotation.append( lexicographically_min(distance) )
    # Sort the LMR array for better counting the same clocks
    same_after_rotation.sort()
    # Count the same clocks. Notice that all the same clocks must
    # appear consecutively.
    current = same_after_rotation[0]
    current_count = 1
    same_pairs = 0
    for clock in same_after_rotation[1:]:
        if clock == current:
            current_count += 1
        else:
            same_pairs += current_count * ( current_count - 1 ) /2
            current_count = 1
            current = clock
    same_pairs  += current_count * ( current_count - 1 ) /2
    return same_pairs