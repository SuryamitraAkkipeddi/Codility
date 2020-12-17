def solution(A):
    max_slice_ending_here = A[0]
    max_slice = A[0]
    for element in A[1:]:
        max_slice_ending_here = max(element, max_slice_ending_here+element)
        max_slice = max(max_slice, max_slice_ending_here)
    return max_slice