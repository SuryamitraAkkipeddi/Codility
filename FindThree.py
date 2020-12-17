def prefixArray(S):
    # Method: Z algorithm
    # prefixes[i] is the length of the longest common prefix of
    #   string S and S[i:].
    prefixes = [0] * len(S)
    left, right = -1, -1
    for index in xrange(1, len(S)):
        if right > index:
            if prefixes[index-left] < right - index:
                # Already computed
                prefixes[index] = prefixes[index-left]
            else:
                # May extend
                offset = right - index
                while index+offset < len(S) and S[index+offset] == S[offset]:
                    offset += 1
                left, right = index, index + offset
                prefixes[index] = offset
        else:
            # Have to compute from scratch
            offset = 0
            while index+offset < len(S) and S[offset] == S[index+offset]:
                offset += 1
            left, right = index, index + offset
            prefixes[index] = offset
    return prefixes
def countThreeBorder(prefixes):
    longest = len(prefixes)/3
    longestMid = 0
    leftBound, rightBound = len(prefixes)/2, len(prefixes)/2
    while longest > 0:
        if prefixes[len(prefixes)-longest] != longest:
            # Not a border
            longest -= 1
            continue
    for index in range(len(prefixes)-2*longest, rightBound-1,- 1) + range(leftBound, longest-1, -1):  # Find the longest prefixes in the middle range.
            longestMid = max(longestMid, prefixes[index])
            if longestMid >= longest: # The border appears three times, without overlapping
                    break
            else:  # Update the values for next trying
                    leftBound = longest-1
                    rightBound = len(prefixes)-2*longest + 1
                    longest -= 1
                    return longest
def solution(S):
    prefixes = prefixArray(S)
    result = countThreeBorder(prefixes)
    return result