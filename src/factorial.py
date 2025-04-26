def check_num(num):
    """Lanza una exepción si el número no es un entero no negativo.

    Args:
        num: El número a verificar.

    Raises:
        ValueError: Si el número es negativo.
        TypeError: Si el número es de tipo flotante.
    """
    if num < 0:
        raise ValueError
    if isinstance(num, float):
        raise TypeError


def iterative_factorial(num: int) -> int:
    """Calcula el factorial de un número entero no negativo de forma iterativa.

    Args:
        num (int): El número entero no negativo para el cual calcular el factorial.

    Returns:
        int: El factorial del número `num`.

    Raises:
        ValueError: Si `num` es un número negativo.
        TypeError: Si `num` no es un número entero.
    """
    check_num(num)
    fact_res = 1
    for i in range(1, num + 1):
        fact_res *= i
    return fact_res


def recursive_factorial(num: int) -> int:
    """Calcula el factorial de un número entero no negativo de forma recursiva.

    Args:
        num (int): El número entero no negativo para el cual calcular el factorial.

    Returns:
        int: El factorial del número `num`.

    Raises:
        ValueError: Si `num` es un número negativo.
        TypeError: Si `num` no es un número entero.
    """
    check_num(num)
    if num == 0:
        return 1
    return num * recursive_factorial(num - 1)


def main():
    print(recursive_factorial(0))


if __name__ == "__main__":
    main()
