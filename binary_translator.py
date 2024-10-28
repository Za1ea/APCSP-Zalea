def intToBinary(integer):
    if integer == 0:
        return 0
    reversed_binary_list = []
    max = -1
    while 2**(max + 1) <= integer:
        reversed_binary_list.append(0)
        max += 1
    reversed_binary_list[max] = 1
    integer = integer - 2**max
    n = max - 1
    while n >= 0:
        if integer - 2**n >= 0:
            integer -= 2**n
            reversed_binary_list[n] = 1
        else:
            reversed_binary_list[n] = 0
        n -= 1
    binary_list = reversed_binary_list[::-1]
    binary = ''.join([str(x) for x in binary_list])
    return binary

print(intToBinary(5))