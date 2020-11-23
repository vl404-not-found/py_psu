from loremipsum import get_sentences
import random

from pip._vendor.msgpack.fallback import xrange


def iter_func(k):
    global iter_operations
    iter_operations += k


# zzz_ - is a prefix
def zzz_is_equal_str(str_x: str, str_y: str):
    iter_func(1)
    counter = 0
    while (counter < len(str_y) or counter < len(str_x)) \
            and str_x[counter] == str_y[counter]:
        iter_func(9)
        counter += 1
    iter_func(2)
    return counter == len(str_x)


def zzz_search_in_list(search_item: str, _list: list):
    iter_func(1)
    check = False
    for iteration in range(0, len(_list)):
        iter_func(1)
        if zzz_is_equal_str(_list[iteration], search_item):
            print(f'\n {search_item} find at: {iteration}')
            check = True
    if not check:
        iter_func(1)
        raise BaseException("Not found")


def zzz_inline_search(_list, str_y):
    iter_inline = 0
    _list1 = _list
    _list1.append(str_y)
    while True:
        iter_inline += 1
        j = 0
        while j < len(str_y) and _list1[iter_inline].split()[j]:
            j += 1
        if j > len(str_y):
            if iter_inline >= len(_list):
                raise BaseException('Not found')
            else:
                print(f'\n {str_y} find at: {iter_inline}')


def prefix(_str):
    v = [0] * len(_str)
    for i in xrange(1, len(_str)):
        k = v[i - 1]
        while k > 0 and _str[k] != _str[i]:
            k = v[k - 1]
        if _str[k] == _str[i]:
            k = k + 1
        v[i] = k
    return v


def kmp(_str, _list):
    index = -1
    f = prefix(_str)
    k = 0
    for i in xrange(len(_list)):
        while k > 0 and _str[k] != _list[i]:
            k = f[k - 1]
        if _str[k] == _list[i]:
            k = k + 1
        if k == len(_str):
            index = i - len(_str) + 1
            break
    return index


if __name__ == '__main__':
    iter_operations = 0
    # Взято из библиотеки генерации рандомных текстов
    _list = get_sentences(50000)

    # искомая строка
    # Случайно задаётся их всего массива строк
    search = _list[random.randint(0, len(_list) - 1)]

    for i in range(100):
        try:
            iter_func(-iter_operations)
            zzz_inline_search(search, _list)
        except BaseException as e:
            print(e)
    print(iter_operations)
