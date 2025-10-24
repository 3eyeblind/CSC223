from postfix_evaluator import PostfixEvaluator
from infix_converter import InfixToPostfixConverter

def _format_result(expr: str, value):
    """
    Match the expected formatting:
      - If the expression contains '/', show as float (e.g., 6.0, 14.5).
      - Otherwise, if it's an int-like float, print as int.
    """
    has_div = '/' in expr.split()
    if has_div:
        return str(float(value))
    try:
        iv = int(value)
        if iv == value:
            return str(iv)
    except Exception:
        pass
    return str(value)

def run_postfix_tests():
    postfix = [
        "5 3 +",
        "8 2 - 3 +",
        "5 3 8 * +",
        "6 2 / 3 +",
        "5 8 + 3 -",
        "5 3 + 8 *",
        "8 2 3 * + 6 -",
        "5 3 8 * + 2 /",
        "8 2 + 3 6 * -",
        "5 3 + 8 2 / -",
    ]
    expected = [
        "8", "9", "29", "6.0", "10",
        "64", "8", "14.5", "-8", "4.0"
    ]

    ev = PostfixEvaluator()
    print("----- Postfix Evaluator -----")
    for expr, exp in zip(postfix, expected):
        val = ev.evaluate(expr)
        print(f"[{expr}] = {_format_result(expr, val)}")

def run_infix_tests():
    infix = [
        "A + B",
        "A + B * C",
        "( A + B ) * C",
        "A * B + C / D",
        "( A + B ) * ( C - D )",
        "A + B * C - D / E",
        "A * ( B + C ) / D",
        "( A + B * C ) / ( D - E )",
        "A +  ( B - C ) * D",
        "( A + B * ( C - D ) ) / E",
    ]
    expected = [
        "A B +",
        "A B C * +",
        "A B + C *",
        "A B * C D / +",
        "A B + C D - *",
        "A B C * + D E / -",
        "A B C + * D /",
        "A B C * + D E - /",
        "A B C - D * +",
        "A B C D - * + E /",
    ]

    conv = InfixToPostfixConverter()
    print("----- Infix to Postfix Converter -----")
    for expr, exp in zip(infix, expected):
        out = conv.convert(expr)
        print(f"[{expr}] -> [{out}]")

if __name__ == "__main__":
    run_postfix_tests()
    run_infix_tests()