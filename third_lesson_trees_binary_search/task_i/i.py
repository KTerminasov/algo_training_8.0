class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def parse_to_rpn(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    output = []
    stack = []
    i = 0
    length = len(expression)
    while i < length:
        c = expression[i]
        if c.isalnum():
            start = i
            while i < length and expression[i].isalnum():
                i += 1
            output.append(expression[start:i])
            continue
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence.get(c, 0):
                output.append(stack.pop())
            stack.append(c)
        i += 1
    
    while stack:
        output.append(stack.pop())
    
    return output

def build_tree(rpn):
    stack = []
    for token in rpn:
        if token in ['+', '-', '*', '/']:
            right = stack.pop()
            left = stack.pop()
            stack.append(Node(token, left, right))
        else:
            stack.append(Node(token))
    return stack[0] if stack else None

def display_tree(root):
    def display(node):
        if node.left is None and node.right is None:
            s = str(node.value)
            width = len(s)
            height = 1
            middle = width // 2
            return [s], width, height, middle
        
        if node.value in ['+', '-', '*', '/']:
            s = '[' + node.value + ']'
        else:
            s = str(node.value)
        u = len(s)
        
        if node.right is None:
            lines, n, p, x = display(node.left)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '|' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2
        
        if node.left is None:
            lines, n, p, x = display(node.right)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '|' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2
        
        left, n, p, x = display(node.left)
        right, m, q, y = display(node.right)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '|' + (n - x - 1 + u + y) * ' ' + '|' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2
    
    lines, _, _, _ = display(root)
    return lines

def main():
    expression = input().strip().replace(" ", "")
    rpn = parse_to_rpn(expression)
    tree = build_tree(rpn)
    lines = display_tree(tree)
    for line in lines:
        print(line)

if __name__ == '__main__':
    main()