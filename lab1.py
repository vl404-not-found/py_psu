def not_optimal_bin_search(_list, value):
    l = 0
    r = len(_list) - 1
    operations = 3
    while l <= r:
        i = (l + r) / 2
        i = int(i)
        operations += 5
        if _list[i] == value:
            pass
            print(operations)
            return i
        if _list[i] < value:
            operations += 3
            l = i + 1
        else:
            r = i - 1
    print(operations + 1)
    raise BaseException("not found")


def optimal_bin_search(_list, value):
    l = 0
    r = len(_list) - 1
    operations = 3
    while l < r:
        i = int((l + r) / 2)
        operations += 5
        if _list[i] < value:
            operations += 3
            l = i + 1
        else:
            r = i
    if _list[r] == value:
        print(operations + 2)
        return r
    else:
        print(operations + 1)
        raise BaseException("not found")


def not_optimal_search(_list, value):
    iter = 0
    operations = 1
    while len(_list) - 1 > iter and _list[iter] != value:
        iter += 1
        operations += 6

    operations += 3
    print(operations)

    if iter < len(_list) - 1:
        return iter
    else:
        raise BaseException("not found")


def optimal_search(_list, value):
    iter = 0
    operations = 1
    _list.append(value)
    while _list[iter] != value:
        iter += 1
        operations += 3

    operations += 3
    print(operations)

    if iter != len(_list) - 1:
        return iter
    else:
        raise BaseException("not found")


def search_in_sort_list(_list, value):
    i = 0
    _list.append(value + 1)
    operations = 3
    while _list[i] < value:
        i += 1
        operations += 4
    operations += 5
    if i < len(_list) and _list[i] == value:
        print(operations + 1)
        return i
    else:
        print(operations + 1)
        raise BaseException("not found")


if __name__ == '__main__':
    i = [c for c in range(250000)]
    val = 125002
    try:
        for z in range(1000):
            print(optimal_bin_search(i, val))
            print(not_optimal_bin_search(i, val))
            # print(search_in_sort_list(i, val))
    except BaseException as e:
        print(e)
