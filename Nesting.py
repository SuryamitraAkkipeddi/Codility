def solution(S):
    parentheses = 0
    for element in S:
        if element == "(":
            parentheses += 1
        else:
            parentheses -= 1
            if parentheses < 0:
                return 0
    if parentheses == 0:
        return 1
    else:
        return 0