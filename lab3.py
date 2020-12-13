# help funcs
import math
import random


def create_ex_data():
    with open('example.txt', 'w') as file:
        for it in range(10000):
            if it < 1:
                file.write(str(random.randint(0, 3200)))
            else:
                file.write("\n" + str(random.randint(0, 3200)))


def convert_base(num, to_base=10, from_base=10):
    # first convert to decimal number
    if isinstance(num, str):
        n = int(num, from_base)
    else:
        n = int(num)
    # now convert decimal to 'to_base' base
    alphabet = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if n < to_base:
        return alphabet[n]
    else:
        return convert_base(n // to_base, to_base) + alphabet[n % to_base]


def _len(num):
    return len(str(num))


# lab funcs
class HashArray:
    size = 4
    divider = 2
    to_num_sys = 2
    _dict = {}

    def adding(self, key_a, value):
        flag = True
        for key in self._dict.keys():
            if key_a == key:
                flag = False
                self._dict.get(key_a).append(value)
        if flag:
            self._dict.update({key_a: [value]})

    def searching(self, key_a, value_a):
        for key in self._dict.keys():
            if key == key_a:
                for value in self._dict.get(key):
                    if value == value_a:
                        return key
        return -1

    def add_num_divider(self, num):
        conv = int(num // self.divider) + 1
        self.adding(conv, num)

    def search_divider(self, num):
        conv = int(num // self.divider) + 1
        self.searching(conv, num)

    def add_num_sys(self, num):
        conv = int(str(convert_base(num, self.to_num_sys))[:self.size])
        self.adding(conv, num)

    def search_num_sys(self, num):
        conv = int(str(convert_base(num, self.to_num_sys))[:self.size])
        self.searching(conv, num)

    def add_num_square(self, num):
        conv = str(num)[
               int(int(_len(num) / 2) - self.size):
               int(_len(num) / 2) + math.ceil(self.size)]
        self.adding(conv, num)

    def search_num_square(self, num):
        conv = str(num)[
               int(int(_len(num) / 2) - self.size):
               int(_len(num) / 2) + math.ceil(self.size)]
        self.searching(conv, num)

    def add_coagulation(self, num):
        pre = 0
        dec_counter = 0
        for a_iter in str(num):
            if dec_counter != self.size:
                dec_counter += 1
                pre += int(a_iter) * 10 ** dec_counter
            else:
                dec_counter = 0

        self.adding(int(str(pre)[-self.size:]), num)

    def search_coagulation(self, num):
        pre = 0
        dec_counter = 0
        for a_iter in str(num):
            if dec_counter != self.size:
                dec_counter += 1
                pre += int(a_iter) * 10 ** dec_counter
            else:
                dec_counter = 0
        self.searching(pre, num)


if __name__ == '__main__':

    array = HashArray()
    with open('example.txt', 'r') as f:
        for i in f.readlines():
            array.add_num_square(int(i))
        f.close()

    array = HashArray()
    with open('example.txt', 'r') as f:
        for i in f.readlines():
            array.add_coagulation(int(i))
        f.close()

    array = HashArray()
    with open('example.txt', 'r') as f:
        for i in f.readlines():
            array.add_num_sys(int(i))
        f.close()

    array = HashArray()
    with open('example.txt', 'r') as f:
        for i in f.readlines():
            array.add_num_divider(int(i))
        f.close()
