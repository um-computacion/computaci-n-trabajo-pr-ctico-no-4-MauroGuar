def list_flattener(lst: list) -> list:
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
    return tmp_list


def main():
    pass


if __name__ == "__main__":
    main()
