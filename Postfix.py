def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    output = []
    stack = []

    for token in expression:
        if token.isalnum():
            output.append(token)
        elif token in "+-*/^":
            while (stack and stack[-1] in "+-*/^" and
                   precedence[token] <= precedence[stack[-1]]):
                output.append(stack.pop())
            stack.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()

    while stack:
        output.append(stack.pop())

    return ''.join(output)

# Example usage
infix_expression = "3 + 5 * (2 - 6)"
postfix_expression = infix_to_postfix(infix_expression)
print("Infix expression:", infix_expression)
print("Postfix expression:", postfix_expression)
