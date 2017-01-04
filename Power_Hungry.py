def answer(l):
    # filtered_l = filter(lambda a: a != 0, l)
    # if len(filtered_l) == 0:
    #     return "0"
    # if filter(lambda a: a < 0, l) == filtered_l:
    #     return "0"
    # sorted_l = sorted(filtered_l, key=abs)
    # res = reduce(lambda x, y: x * y, sorted_l)
    # if res < 0:
    #     for num in sorted_l:
    #         if num < 0:
    #             res /= num
    #             return str(res)
    # negs = []
    # pos = []
    # for num in l:
    #     if num < 0:
    #         negs.append(long(num))
    #     if num > 0:
    #         pos.append(long(num))
    # if len(pos) == 0 and len(negs) <= 1:
    #     return "0"
    # res_pos = 0
    # if len(pos) > 0:
    #     res_pos = reduce(lambda x, y: x * y, pos)
    # res_neg = 0
    # if len(negs) > 1:
    #     res_neg = reduce(lambda x, y: x * y, negs)
    #     if res_neg < 0:
    #         res_neg /= max(negs)
    # if res_pos > 0 and res_neg > 1:
    #     return str(res_pos * res_neg)
    # return str(max(res_pos, res_neg))
    num_neg = 0
    greatest_neg = float('-inf')
    if len(l) == 1 and l[0] < 0:
        return str(l[0])
    l = filter(lambda a: a != 0, l)
    for num in l:
        if num < 0:
            greatest_neg = max(greatest_neg, num)
            num_neg += 1
    if (num_neg == len(l) and num_neg < 2):
        return "0"
    res = reduce(lambda x, y: x * y, l)
    if res < 0:
        res /= greatest_neg
    return str(res)

print answer([2, 0, 2, 2, 0]) == "8"
print answer([-2, -3, 4, -5]) == "60"
print answer([0,0,0]) == "0"
print answer([-1, 0]) == "0"
print answer([-1]) == "-1"
print answer([-12, -12, 2, 0, 0, 0, 0, 0]) == "288"
print answer([0,-123,0,-12]) == "1476"
print answer([0,-123,0,-12, -1, -13, 2]) == "38376"
print answer([0, 1, -12, 0]) == "1"
print answer([1000]*50) == "1000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
