def answer(n):
    # power = 1
    # count = 0
    # while eval(str(power) + "<" + n):
    #     power <<= 1
    #     count += 1
    # if power == n:
    #     return count
    # prev = power >> 1
    # prev_count = count - 1
    # return min(count + eval(str(power) + "-" + n), prev_count + eval(n + "-" + str(prev)))
    n = int(n)
    res = 0
    while n != 1:
        if n & 1 == 0:
            n >>= 1
        elif n == 3  or ((n + 1) & n) > ((n - 1) & (n - 2)):
            n -= 1
        else:
            n += 1
        res += 1
    return res


print answer("4") == 2
print answer("15") == 5
print answer("13") == 5
print answer("9") == 4
print answer("2") == 1
print answer("1") == 0