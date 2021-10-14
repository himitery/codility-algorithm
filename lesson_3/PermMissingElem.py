from functools import reduce


def solution(A):
    if len(A) == 0:
        return 1

    length = len(A) + 1
    return (length * (length + 1) // 2) - reduce(lambda x, y: x + y, A)
