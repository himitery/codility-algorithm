def solution(A):
    left = A[0]
    right = sum(A[1:])
    result = abs(left - right)

    for i in range(1, len(A) - 1):
        left += A[i]
        right -= A[i]
        result = result if result < abs(left - right) else abs(left - right)
    return result
