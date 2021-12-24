def replace_bit(n, bit, value):
    return n[:bit] + str(value) + n[bit + 1:]