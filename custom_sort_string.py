def custom_sort_string(order, s):
    char_order = {char: i for i, char in enumerate(order)}
    sorted_chars = sorted(s, key=lambda x: char_order.get(x, len(order)))
    return ''.join(sorted_chars)

order = "cba"
s = "abcd"
result = custom_sort_string(order, s)
print(result)