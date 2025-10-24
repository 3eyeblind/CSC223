import re
from stack import Stack

class InfixToPostfixConverter:
    """
    Converts infix -> postfix using the Shunting Yard algorithm.
    Handles operators: +, -, *, /; parentheses; identifiers (A, B, X1) and numbers.

    Rules:
      - Precedence: * /  >  + -
      - Associativity: left for + - * /
      - Output tokens are space-separated (e.g., 'A B C * +').

    Usage:
        conv = InfixToPostfixConverter()
        out = conv.convert("( A + B ) * C")  # -> 'A B + C *'
    """

    def __init__(self):
        self._prec = {'+': 1, '-': 1, '*': 2, '/': 2}
        self._left_assoc = {'+': True, '-': True, '*': True, '/': True}

    def _tokenize(self, expr: str):
        """
        Extract tokens: identifiers, numbers, operators, parentheses.
        Accepts both spaced and tightly written forms.
        """
        pattern = r'[A-Za-z]\w*|\d+(?:\.\d+)?|[\+\-\*\/\(\)]'
        return re.findall(pattern, expr)

    def convert(self, expr: str) -> str:
        out = []
        ops = Stack()
        tokens = self._tokenize(expr)

        def is_operand(t):
           
            return bool(re.match(r'^[A-Za-z]\w*|\d+(?:\.\d+)?$', t))

        for t in tokens:
            if is_operand(t):
                out.append(t)
            elif t in self._prec:  
                while (not ops.is_empty()
                       and ops.peek() in self._prec
                       and (
                           self._prec[ops.peek()] > self._prec[t]
                           or (self._prec[ops.peek()] == self._prec[t] and self._left_assoc[t])
                       )):
                    out.append(ops.pop())
                ops.push(t)
            elif t == '(':
                ops.push(t)
            elif t == ')':
                while not ops.is_empty() and ops.peek() != '(':
                    out.append(ops.pop())
                if ops.is_empty():
                    raise ValueError("Mismatched parentheses: missing '('")
                ops.pop() 
            else:
                raise ValueError(f"Invalid token '{t}' in infix expression")

 
        while not ops.is_empty():
            top = ops.pop()
            if top in ('(', ')'):
                raise ValueError("Mismatched parentheses")
            out.append(top)

        return ' '.join(out)