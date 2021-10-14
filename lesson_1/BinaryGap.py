def solution(N):
    binary = str(bin(N)).split("0b")[1].strip("0").split("1")
    return max(list(map(lambda x: len(x), binary)))
