from math import sqrt

def solution(N):
    # write your code in Python 3.6
    for i in range(int(sqrt(N)), 0, -1):
        if N % i == 0:
            return (int(N / i) + i) * 2