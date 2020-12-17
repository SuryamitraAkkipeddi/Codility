def solution(A):
    alphabet = set()
    for element in A:
        alphabet.add(element)
    for index in xrange(len(A)):
        alphabet.discard(A[index])
        if len(alphabet) == 0:
            return index