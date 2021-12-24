import time
from functools import reduce


def mult(iterable):
    return reduce(lambda a, b: a * b, iterable)


def time_call(f, *args):
    t1 = time.time()
    result = f(*args)
    print(f'Time taken: {time.time() - t1}')
    return result


def remove_empty(l):
    return filter(None, l)


def safe_split(text, delim='\n'):
    return list(remove_empty(text.split(delim)))


def read_input(filename='input'):
    with open(filename) as f:
        return f.read()


def read_input_split(filename, delim):
    return safe_split(read_input(filename=filename), delim)


def read_input_as_lines(filename='input'):
    return read_input_split(filename, '\n')


def read_input_as_numbers(filename='input'):
    return list(map(lambda l: int(l), read_input_as_lines(filename=filename)))


def read_input_as_digit_grid(filename='input'):
    return [list(map(int, list(l))) for l in (read_input_as_lines(filename=filename))]


def read_input_as_passports(filename='input'):
    return map(lambda p: p.strip(), read_input_split(filename, '\n\n'))


def convert_hex_into_bit_string(hex_string):
    bit_groups = []
    for c in list(hex_string):
        value = int(c, 16)
        bit_groups.append(bin(value)[2:].zfill(4))
    return ''.join(bit_groups)


def string_to_digits(string):
    return list(map(int, list(string)))
