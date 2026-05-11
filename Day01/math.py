#

class Node:

    def __init__(self, v: str, l=None, r=None ):
        self._v = v
        self._left = l
        self._right = r
    

def eval(node):
    stack = []
    _eval(node, stack)
    return stack.pop()


def _eval(node, stack:list):
    if node._left:
        _eval(node._left, stack)
    if node._right:
        _eval(node._right, stack)
    if isinstance(node._v, str):
        x = stack.pop()
        y = stack.pop()
        if node._v == '+':
            stack.append(x + y)
        elif node._v == '-':
            stack.append(x - y)
        elif node._v == '*':
            stack.append(x * y)
        elif node._v == '/':
            stack.append(x / y)                
    else:
        stack.append(node._v)


def pre_visit(node):
    print(node._v, end=' ')
    if node._left:
        pre_visit(node._left)
    if node._right:
        pre_visit(node._right)

def post_visit(node):
    if node:
        post_visit(node._left)
        post_visit(node._right)
        print(node._v, end=' ')


def main():
    stack = []
    expr = Node('+', l=Node(4), r=Node('*', l=Node(2), r=Node(5)))

    pre_visit(expr)
    print()

    post_visit(expr)
    print()

    print(eval(expr))


if __name__ == "__main__":
    main()
