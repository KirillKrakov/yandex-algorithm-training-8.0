import sys

def tokenize(s):
    tokens = []
    i = 0
    while i < len(s):
        if s[i] in '+-*/^()':
            tokens.append(s[i])
            i += 1
        elif s[i].isalpha():
            tokens.append(s[i])
            i += 1
        elif s[i] == ' ':
            i += 1
        else:
            raise Exception("Invalid character")
    return tokens

def parse_expression(tokens):
    left = parse_term(tokens)
    while tokens and tokens[0] in ['+', '-']:
        op = tokens.pop(0)
        right = parse_term(tokens)
        left = (op, left, right)
    return left

def parse_term(tokens):
    left = parse_factor(tokens)
    while tokens and tokens[0] in ['*', '/']:
        op = tokens.pop(0)
        right = parse_factor(tokens)
        left = (op, left, right)
    return left

def parse_factor(tokens):
    left = parse_element(tokens)
    if tokens and tokens[0] == '^':
        op = tokens.pop(0)
        right = parse_factor(tokens)
        left = (op, left, right)
    return left

def parse_element(tokens):
    if tokens[0] == '(':
        tokens.pop(0)
        expr = parse_expression(tokens)
        if tokens[0] != ')':
            raise Exception("Expected )")
        tokens.pop(0)
        return expr
    else:
        return tokens.pop(0)

def draw_tree(node):
    if isinstance(node, str):
        return ([node], len(node), 0)
    
    op, left, right = node
    left_lines, left_width, left_root = draw_tree(left)
    right_lines, right_width, right_root = draw_tree(right)
    
    total_width = left_width + 5 + right_width
    root_x = left_width + 2
    left_root_abs = left_root
    right_root_abs = left_width + 5 + right_root

    top_line = [' '] * total_width
    top_line[left_root_abs] = '.'
    top_line[root_x - 1] = '['
    top_line[root_x] = op
    top_line[root_x + 1] = ']'
    top_line[right_root_abs] = '.'
    
    for i in range(left_root_abs + 1, root_x - 1):
        top_line[i] = '-'
    for i in range(root_x + 2, right_root_abs):
        top_line[i] = '-'
    
    mid_line = [' '] * total_width
    mid_line[left_root_abs] = '|'
    mid_line[right_root_abs] = '|'
    
    left_height = len(left_lines)
    right_height = len(right_lines)
    total_height = max(left_height, right_height) + 2
    
    result_lines = [''.join(top_line), ''.join(mid_line)]
    
    for i in range(total_height - 2):
        left_line = left_lines[i] if i < left_height else ' ' * left_width
        right_line = right_lines[i] if i < right_height else ' ' * right_width
        result_lines.append(left_line + ' ' * 5 + right_line)
    
    return (result_lines, total_width, root_x)

def main():
    data = input().strip()
    tokens = tokenize(data)
    tree = parse_expression(tokens)
    lines, width, root_x = draw_tree(tree)
    for line in lines:
        print(line)

if __name__ == '__main__':
    main()