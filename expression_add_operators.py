def addOperators(num, target):
    def backtrack(index, path, value, last):
        if index == len(num):
            if value == target:
                result.append(path)
            return
        for i in range(index + 1, len(num) + 1):
            current_str = num[index:i]
            current_num = int(current_str)
            if len(current_str) > 1 and current_str[0] == '0':
                continue
            if index == 0:
                backtrack(i, current_str, current_num, current_num)
            else:
                backtrack(i, path + '+' + current_str, value + current_num, current_num)
                backtrack(i, path + '-' + current_str, value - current_num, -current_num)
                backtrack(i, path + '*' + current_str, value - last + last * current_num, last * current_num)
    result = []
    backtrack(0, '', 0, 0)
    return result

num = "123"
target = 6
result = addOperators(num, target)
print(f"Expressions that evaluate to {target}: {result}")
