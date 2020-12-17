def solution(A, B):
    # Find the smallest diameter to achieve each position
    min_diameter_so_far = [A[0]] * len(A)
    for index in xrange(1, len(A)):
        min_diameter_so_far[index] = min(min_diameter_so_far[index-1], A[index])
    rings_index = len(A) - 1    # Travel the well from bottom to top
    fit_disks = 0               # The number of fitted disks
    for disks_index in xrange(len(B)):
        while min_diameter_so_far[rings_index] < B[disks_index]:
            rings_index -= 1
            if rings_index == -1:
                # No way to fit into the well for current disk, and
                # therefore the remaining disks.
                return fit_disks
        fit_disks += 1  # Current disk occupies this ring of well
        rings_index -= 1
        if rings_index == -1:
            # The toppest ring of well is used. No way to fit any
            # more disk.
            break
    return fit_disks