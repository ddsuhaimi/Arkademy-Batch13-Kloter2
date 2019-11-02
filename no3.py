import random


def randomize(n):
    array = [random.randint(1, 10) for _ in range(n)]
    print(array)
    print(sum(array))


randomize(6)
