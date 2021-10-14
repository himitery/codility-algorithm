def solution(A, K):
    if not len(A) > 0:
        return A

    rotation = K % len(A)
    for _ in range(rotation):
        A.insert(0, A.pop())
    return A
