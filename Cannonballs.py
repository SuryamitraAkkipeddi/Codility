def solution(A, B):
    to_fall = [-1] * (max(B) + 1)   # Store where the ball should
                                    # fall. to_fall[i] = j means,
                                    # the cannonball, which is shot
                                    # from heigth of i, will fall
                                    # at position j.
    # Scan and find the initial falling position for cannonballs
    # from each different shooting height.
    current_pos = 0     # Index for the landscape array A.
    # For all shooting heigthes <= A[0], the cannonballs do not
    # change the landscape. Keep the content being -1 and no need
    # to try them.
    for height in xrange( A[0]+1, max(B)+1 ):
        while current_pos < len(A) and height > A[current_pos]:
            current_pos += 1
        if current_pos == len(A):
            # No position could prevent the cannonball from flying
            # beyond the bound. These cannonballs do not change
            # the landscape. Keep the content being -1.
            break
        else:
            # The cannonball meets with a high enought position,
            # and falls at the previous position.
            to_fall[height] = current_pos - 1
    for cannonball in B:
        if to_fall[cannonball] == -1:
            # This cannonball would not change the landscape.
            continue
        else:
            fall_pos = to_fall[cannonball]
            A[ fall_pos ] += 1      # increases the ground by 1
            # For shooting height > A[fall_pos], the increase
            #       is NOT enought to block/change their flying
            #       path.
            # For shooting height < A[fall_pos] <= old A[fall_pos]
            #       they cannot fly beyond this position both
            #       before and after increase. NO change is
            #       made for them.
            # ONLY for shooting height = A[fall_pos], its
            #       flying path might be changed due to the
            #       increase.
            to_fall[ A[ fall_pos ] ] = min(
                            to_fall[ A[ fall_pos ] ], fall_pos-1)
    return A