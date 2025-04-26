def check_num(num):
    """Lanza una exepción si el número no es un entero mayor a 0.

    Args:
        num: El número a verificar.

    Raises:
        ValueError: Si el número es menor o igual a 0.
        TypeError: Si el número es de tipo flotante.
    """
    if num <= 0:
        raise ValueError
    if isinstance(num, float):
        raise TypeError


def iterative_fibonacci(pos: int) -> int:
    """Calcula el número de Fibonacci para una posición dada de forma iterativa.

    Args:
        pos (int): La posición en la secuencia de Fibonacci para la cual
                   calcular el número. Debe ser un entero mayor a 0.

    Returns:
        int: El número de Fibonacci correspondiente a la posición.

    Raises:
        TypeError: Si `pos` no es un entero.
        ValueError: Si `pos` no es un entero mayor a 0.
    """
    check_num(pos)
    if pos == 1:
        return 0
    if pos == 2:
        return 1
    fib_prev = 0
    fib_res = 1
    for _ in range(pos - 1):
        fib_prev, fib_res = fib_res, fib_prev + fib_res
    return fib_prev


def recursive_fibonacci(pos: int) -> int:
    """Calcula el número de Fibonacci para una posición dada de forma recursiva.

    Args:
        pos (int): La posición en la secuencia de Fibonacci para la cual
                   calcular el número. Debe ser un entero mayor a 0.

    Returns:
        int: El número de Fibonacci correspondiente a la posición.

    Raises:
        TypeError: Si `pos` no es un entero.
        ValueError: Si `pos` no es un entero mayor a 0.
    """
    check_num(pos)
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
