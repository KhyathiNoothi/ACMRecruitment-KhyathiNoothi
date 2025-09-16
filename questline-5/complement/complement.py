def twos_complement(value, bits=8):
    if value >= 0:
        return format(value, '08b')
    else:
        return format((1 << bits) + value, '08b')

number = -42
binary_repr = twos_complement(number)
print(f"8-bit 2's complement of {number} is: {binary_repr}")
