def fractionToDecimal(numerator, denominator):
    if numerator == 0:
        return "0"
    result = []
    if (numerator < 0) ^ (denominator < 0):
        result.append("-")
    numerator = abs(numerator)
    denominator = abs(denominator)
    integer_part = numerator // denominator
    result.append(str(integer_part))
    remainder = numerator % denominator
    if remainder == 0:
        return "".join(result)
    result.append(".")
    remainder_map = {}
    while remainder != 0:
        if remainder in remainder_map:
            index = remainder_map[remainder]
            result.insert(index, "(")
            result.append(")")
            break
        remainder_map[remainder] = len(result)
        remainder *= 10
        result.append(str(remainder // denominator))
        remainder %= denominator
    return "".join(result)

print(fractionToDecimal(1, 2))
