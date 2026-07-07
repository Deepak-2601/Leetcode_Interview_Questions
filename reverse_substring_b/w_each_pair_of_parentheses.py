def reverseParentheses(s):
    stack = []
    for char in s:
        if char == ')':
            temp = []
            while stack and stack[-1] != '(':
                temp.append(stack.pop())
            stack.pop() 
            stack.extend(temp) 
        else:
            stack.append(char)
    return ''.join(stack)

s = "(u(love)i)"
result = reverseParentheses(s)
print(result)