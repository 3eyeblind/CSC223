from .binary_expression_tree import BinaryExpressionTree

def run_samples():
    samples = [
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
    print("----- Binary Expression Tree -----\n")
    for pf in samples:
        T = BinaryExpressionTree()
        T.build_from_postfix(pf)
        inf = T.infix_traversal()
        post = T.postfix_traversal()
        val = T.evaluate_tree()
        print(f"Infix Expression:   {inf}")
        print(f"Postfix Expression: {post}")
        print(f"Evaluated Result:   {val}\n")

if __name__ == "__main__":
    run_samples()