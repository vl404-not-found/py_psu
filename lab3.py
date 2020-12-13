# help funcs
import math


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
    size = 2
    divider = 2
    to_num_sys = 10
    _dict = {}

    def adding(self, key_a, value):
        flag = True
        for key in self._dict.keys():
            if key_a == key:
                flag = False
                self._dict.update({key_a: self._dict.get(key_a).append(value)})
        if flag:
            self._dict.update({key_a: [value]})

    def add_num_divider(self, num):
        conv = int(num // self.divider) + 1
        self.adding(conv, num)

    def add_num_sys(self, num):
        conv = convert_base(self.divider, self.to_num_sys)
        self.adding(conv, num)

    def add_num_square(self, num):
        conv = str(num)[
               int(int(_len(num) / 2) - self.size):
               int(_len(num) / 2) + math.ceil(self.size)]
        self.adding(conv, num)

    def add_coagulation(self, num):
        pre = 0
        dec_counter = 0
        for i in str(num):
            if dec_counter != self.size:
                dec_counter += 1
                pre += i * 10 ** dec_counter
            else:
                dec_counter = 0

        self.adding(int(str(pre)[-self.size:]), num)


if __name__ == '__main__':
    sss = 123456789
    print(str(sss)[-3:])
