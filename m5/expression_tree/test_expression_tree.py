import unittest
from m5.expression_tree.binary_expression_tree import BinaryExpressionTree

class TestExpressionTree(unittest.TestCase):
    def test_basic_add(self):
        t = BinaryExpressionTree()
        t.build_from_postfix("3 2 +")
        self.assertEqual(t.evaluate_tree(), 5.0)
        self.assertEqual(t.postfix_traversal(), "3 2 +")
        self.assertEqual(t.infix_traversal(), "(3 + 2)")

    def test_mixed_ops(self):
        t = BinaryExpressionTree()
        t.build_from_postfix("3 7 + 14 *")
        self.assertEqual(t.evaluate_tree(), 140.0)

    def test_bad_token(self):
        t = BinaryExpressionTree()
        with self.assertRaises(ValueError):
            t.build_from_postfix("3 x +")

    def test_too_few_operands(self):
        t = BinaryExpressionTree()
        with self.assertRaises(ValueError):
            t.build_from_postfix("3 +")

    def test_divide_by_zero(self):
        t = BinaryExpressionTree()
        t.build_from_postfix("4 0 /")
        with self.assertRaises(ZeroDivisionError):
            t.evaluate_tree()


if __name__ == "__main__":
    print("\n----- Running Binary Expression Tree Tests -----\n")
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestExpressionTree)
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)

    n_run = result.testsRun
    n_fail = len(result.failures)
    n_err = len(result.errors)
    n_skip = len(getattr(result, "skipped", []))
    n_xfail = len(getattr(result, "expectedFailures", []))
    n_xsucc = len(getattr(result, "unexpectedSuccesses", []))
    n_pass = n_run - n_fail - n_err - n_skip - n_xfail - n_xsucc

    print("\n----- Test Summary -----")
    print(f"Total tests run: {n_run}")
    print(f"Passed: {n_pass}")
    print(f"Failed: {n_fail}")
    print(f"Errors: {n_err}")
    if n_skip:  print(f"Skipped: {n_skip}")
    if n_xfail: print(f"Expected failures: {n_xfail}")
    if n_xsucc: print(f"Unexpected successes: {n_xsucc}")

    if result.wasSuccessful():
        print("\n All tests passed successfully!\n")
    else:
        print("\n Some tests failed. See details above.\n")