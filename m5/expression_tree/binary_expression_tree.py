from dataclasses import dataclass
from typing import Optional, List, Callable
from .stack import Stack


_OPERATORS: dict[str, Callable[[float, float], float]] = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b,
}

@dataclass
class _Node:
    value: str
    left: Optional["_Node"] = None
    right: Optional["_Node"] = None

class BinaryExpressionTree:
    def __init__(self):
        self.root: Optional[_Node] = None

    # Core ops 
    def is_empty(self) -> bool:
        return self.root is None

    def clear_tree(self) -> None:
        self.root = None

    def build_from_postfix(self, postfix: str) -> None:
        """
        Build tree from a whitespace-separated postfix expression.
        Errors: unsupported token; insufficient operands; leftover tokens.
        """
        s = Stack()
        tokens = [t for t in postfix.strip().split() if t]

        for tok in tokens:
            if tok.replace('.', '', 1).isdigit():  # number (int/float)
                s.push(_Node(tok))
            elif tok in _OPERATORS:
                # Need right then left (LIFO)
                if s.is_empty():
                    raise ValueError("Too few operands (missing right operand)")
                right = s.pop()

                if s.is_empty():
                    raise ValueError("Too few operands (missing left operand)")
                left = s.pop()

                s.push(_Node(tok, left, right))
            else:
                raise ValueError(f"Unsupported token: {tok}")

        if s.is_empty():
            raise ValueError("No expression provided")

        self.root = s.pop()
        if not s.is_empty():
            raise ValueError("Extra operands/operators left after building")

    def evaluate_tree(self) -> float:
        if self.root is None:
            raise ValueError("Empty expression tree")
        return self._evaluate(self.root)

    def infix_traversal(self) -> str:
        if self.root is None:
            raise ValueError("Empty expression tree")
        out: List[str] = []
        self._inorder(self.root, out)
        return "".join(out)

    def postfix_traversal(self) -> str:
        if self.root is None:
            raise ValueError("Empty expression tree")
        out: List[str] = []
        self._postorder(self.root, out)
        return " ".join(out)

    # Helpers (recursive)
    def _inorder(self, node: Optional[_Node], out: List[str]) -> None:
        if not node:
            return
        if node.value in _OPERATORS:
            out.append("(")
            self._inorder(node.left, out)
            out.append(f" {node.value} ")
            self._inorder(node.right, out)
            out.append(")")
        else:
            out.append(node.value)

    def _postorder(self, node: Optional[_Node], out: List[str]) -> None:
        if not node:
            return
        self._postorder(node.left, out)
        self._postorder(node.right, out)
        out.append(node.value)

    def _evaluate(self, node: _Node) -> float:
        if node.value not in _OPERATORS:
            return float(node.value)
        op = _OPERATORS[node.value]
        x = self._evaluate(node.left)   
        y = self._evaluate(node.right)  
        if node.value == '/' and y == 0:
            raise ZeroDivisionError("division by zero")
        return op(x, y)