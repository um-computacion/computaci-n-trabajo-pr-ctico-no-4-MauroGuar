def iterative_fibonacci(pos: int) -> int:
    fib_prev = 0
    fib_res = 1
    for _ in range(pos):
        fib_prev, fib_res = fib_res, fib_prev + fib_res
    return fib_prev


def recursive_fibonacci(pos: int) -> int:
    if pos == 1:
        return 0
    elif pos == 2:
        return 1
    else:
        return recursive_fibonacci(pos - 1) + recursive_fibonacci(pos - 2)


def main():
    pass


if __name__ == "__main__":
    main()
