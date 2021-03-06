def palindrome_substring(str):
    str = "#" + "#".join(str) + "#" # Convert the original string so
                                    # that, every palindrome substring
                                    # in the new string has odd number
                                    # of elements.
    palindrome_len = [0] * len(str) # Store the half width (include the
                                    # center point) of the longest
                                    # palindrome substring with index
                                    # being the substring's center.
                                    # palindrome_len[i]-1 means the full
                                    # length of palindrome substring in
                                    # the original string.
    bound = 0   # Record the first positin, that the previous computed
                # palindrome substrings chould NOT achieve.
    center = 0  # Record the center position of the substring, which
                # is corresponding to "bound".
    for index in xrange(len(str)):
        if bound > index:
            # Part of current substring has already been compared.
            # For point "index", 2*center-index is the point
            # symmetrical to the points "center".
            palindrome_len[index] = min( palindrome_len[2*center-index], bound-index )
        else:
            # None of current substring has been compared.
            palindrome_len[index] = 1
        # Compare the uncompared elements one by one.
        while index-palindrome_len[index] >= 0 and index+palindrome_len[index] < len(str) and str[index-palindrome_len[index]] == str[index+palindrome_len[index]]:
                palindrome_len[index] += 1
        if bound < palindrome_len[index] + index:
            # The bound has been extended.
            center = index
            bound = palindrome_len[index] + index
    return palindrome_len
def solution(S):
    # With center point i, if the longest palindrome substring
    # has length of j, the number of palindrome substrings,
    # with the same center, is j//2.
    count = sum([
        (length-1)/2 for length in palindrome_substring(S) if length>2
        ])
    if count > 100000000:
        return -1
    else:
        return count