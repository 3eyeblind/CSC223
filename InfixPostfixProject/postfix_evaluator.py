from stack import Stack
import operator

class PostfixEvaluator:
    """
    Evaluates space-separated postfix (RPN) expressions using a Stack.

    Supports +, -, *, / as per project spec.
    - Numbers may be integers (treated as Python float if / is used).
    - Tokens must be separated by spaces (e.g., '5 3 +', '6 2 / 3 +').

    Usage:
        ev = PostfixEvaluator()
        result = ev.evaluate("5 3 +")  # -> 8
    """

    _ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv, 
    }

    def evaluate(self, expr: str):
        """
        Evaluate a postfix expression and return a numeric result (int or float).

        Algorithm (stack-based):
          - Scan tokens left-to-right.
          - If token is a number -> push
          - If token is an operator -> pop rhs, pop lhs, compute, push result
          - At end, the single stack item is the answer.
        """
        tokens = [t for t in expr.split() if t]
        s = Stack()

        for tok in tokens:
            if tok in self._ops:
                if s.size() < 2:
                    raise ValueError(f"Malformed postfix expression near operator '{tok}'")
                rhs = s.pop()
                lhs = s.pop()
                try:
                    res = self._ops[tok](lhs, rhs)
                except ZeroDivisionError:
                    raise ZeroDivisionError("division by zero in postfix evaluation")
                s.push(res)
            else:
                try:
                    if '.' in tok:
                        num = float(tok)
                    else:
                        num = int(tok)
                except ValueError:
                    raise ValueError(f"Invalid operand '{tok}' in postfix expression")
                s.push(num)

        if s.size() != 1:
            raise ValueError("Malformed postfix expression (extra operands/operators).")
        return s.pop()