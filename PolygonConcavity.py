def _IsClockwise(point_A, point_B, point_C):
    result =(point_B.x-point_A.x)*(point_C.y-point_A.y)-(point_B.y-point_A.y)*(point_C.x-point_A.x)
    if result > 0:      return 1    #   counter-clockwise
    elif result < 0:    return -1   #   clockwise
    else:               return 0    #   a staight line
def solution(A):
    ''' The solution refers to:
        https://www.youtube.com/watch?v=0HZaRu5IupM
    '''
    # Find the lowest point(s) in y-axis.
    lowest_y = A[0].y
    lowest_y_index = []
    for i in range(len(A)):
        if A[i].y < lowest_y:
            lowest_y = A[i].y
            lowest_y_index = [i]
        elif A[i].y == lowest_y:
            lowest_y_index.append(i)
        else:
            continue
    # Find a point, which is not the lowest in y-axis and immediately
    # after a lowest-in-y-axis point.
    start_point = lowest_y_index[0]
    lowest_y_array = [False] * len(A)
    for i in lowest_y_index: lowest_y_array[i] = True
    while lowest_y_array[start_point] == True:
        start_point = (start_point + 1) % len(A)
    start_point = (start_point - 1 + len(A)) % len(A)
    # Re-organize the points so that, it is easier to check every three
    # consecutive points in one loop (without module operation %).
    rotated_A = A[start_point : ] + A[ : start_point]
    # We find the start point such that, the direction is non-zero.
    direction = _IsClockwise(rotated_A[-1], rotated_A[0], rotated_A[1])
    extened_A = rotated_A + rotated_A[:2]
    for i in range(len(A)):
        temp = _IsClockwise(extened_A[i], extened_A[i+1], extened_A[i+2])
        if temp * direction < 0:
            # Compute the original index and return
            return (i + 1 + start_point)%len(A)
    # Every point is on the convex hull.
    return -1