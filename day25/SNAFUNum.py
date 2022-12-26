def convert_from_SNAFU(num):
    i = 0
    s = 0
    while num != "":
        dig = num[-1]
        if dig == "-":
            s -= 5**i
        elif dig == "=":
            s -= 2*(5**i)
        else:
            s += 5**i*int(dig)
        num = num[:-1]
        i += 1
    return s


def if_not_SNAFU(num):
    res = ""
    while num > 0:
        dig = num % 5
        if dig > 2:
            break
        res = str(dig) + res
        num //= 5
    else:
        return res
    return False


def conv_to_SNAFU(num):
    def conv_r(num, s, result, i):
        if i < 0:
            if num == convert_from_SNAFU(result):
                return result
            else:
                return None
        if abs(num-s) <= sums[i]:
            j = 0

            while j < len(fillers):
                if num-s > 0:
                    filler = fillers[j]
                else:
                    filler = fillers[j*-1-1]
                resp = conv_r(num, s+(-(fillers.index(filler))+2)*5**i,
                              result+filler, i-1)
                if resp is not None:
                    return resp
                j += 1

    resp = if_not_SNAFU(num)
    if resp:
        return resp
    i = 1
    sums = [2]
    while sums[-1] < num:
        sums.append(sums[i-1]+2*5**i)
        i += 1
    fillers = ["2", "1", "0", "-", "="]
    res = conv_r(num, 0, "", i-1)
    return res


# file = "test.in"
file = "dane.in"

with open(file) as file:
    print(conv_to_SNAFU(sum(convert_from_SNAFU(line.strip()) for line in file)))
