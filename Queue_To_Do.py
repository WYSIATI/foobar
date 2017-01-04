def answer(start, length):
    # res = 0
    # for i in xrange(length):
    #     s = start + i * length
    #     res ^= reduce(xor, xrange(s, s + length - i), 0)
    # return res

    res = 0
    for i in xrange(length):
        s = start + i * length
        e = s + length - i - 1
        if s == 0:
            res ^= (f(s) ^ f(e))
        else:
            res ^= (f(s - 1) ^ f(e))
    return res

def f(a):
    res = [a, 1, a + 1, 0]
    return res[a % 4]

print answer(0, 3)
print answer(17, 4)
print answer(5, 3)
print answer(0, 0)
