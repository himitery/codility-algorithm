def solution(X, Y, D):
    return (Y - X) // D + (0 if (Y - X) % D == 0 else 1)
