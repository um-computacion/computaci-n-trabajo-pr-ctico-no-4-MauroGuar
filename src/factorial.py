def iterative_factorial(num: int) -> int:
    fact_res = 1
    for i in range(1, num + 1):
        fact_res *= i
    return fact_res


def recursive_factorial(num: int) -> int:
    if num == 0:
        return 1
    return num * recursive_factorial(num - 1)


def main():
    print(recursive_factorial(0))


if __name__ == "__main__":
    main()
