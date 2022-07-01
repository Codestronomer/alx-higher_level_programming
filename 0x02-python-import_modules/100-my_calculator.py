#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    from calculator_1 import add, sub, div, mul

    def operation(a, op, b):
        if op == '+':
            return f"{a} + {b} = {add(a, b)}"
        elif op == '-':
            return f"{a} - {b} = {sub(a, b)}"
        elif op == '/':
            return f"{a} / {b} = {div(a, b)}"
        elif op == '*':
            return f"{a} * {b} = {mul(a, b)}"
        else:
            return "Unknown operator. Avaliable operators: +, -, *, and /"

    i = len(sys.argv) - 1
    if i != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    str = operation(int(sys.argv[1]), sys.argv[2], int(sys.argv[3]))
    if str.startswith('U'):
        print(str)
        sys.exit(1)
    print(str)
