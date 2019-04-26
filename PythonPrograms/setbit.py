#program to count set bits

def set_bits(n):
    c = 0
    while n:
        n &= n - 1
        c += 1
    return c


n = int(input())
print('no of set bits:',set_bits(n))
