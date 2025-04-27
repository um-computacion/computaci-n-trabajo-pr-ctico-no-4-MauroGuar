def list_flattener(lst: list) -> list:
    """
    Aplana una lista anidada, extrayendo todos los elementos de tipo int, float, bool o str
    y colocándolos en una nueva lista de un solo nivel.

    Args:
        lst: La lista que se desea aplanar.

    Returns:
        Una nueva lista que contiene todos los elementos soportados (int, float, bool, str)
        de la lista original, extraídos de cualquier nivel de anidamiento, en el orden
        en que aparecen.

    Raises:
        TypeError: Si la lista contiene algún elemento que no sea una lista ni uno de los
                   tipos de datos soportados (int, float, bool, str).
    """
    tmp_list = []
    for elem in lst:
        if isinstance(elem, list):
            tmp_list.extend(list_flattener(elem))
        elif (
            isinstance(elem, int)
            or isinstance(elem, float)
            or isinstance(elem, bool)
            or isinstance(elem, str)
        ):
            tmp_list.append(elem)
        else:
            raise TypeError
    return tmp_list


def main():
    pass


if __name__ == "__main__":
    main()
