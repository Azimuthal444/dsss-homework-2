""" Unit Test file for Math Quiz"""
import unittest
from math_quiz import get_random_int, get_math_operator, generate_question


class TestMathGame(unittest.TestCase):
    """Unit Test class file for Math Quiz"""

    def test_get_random_int(self):
        """Unit test for get_random_int()"""
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = get_random_int(min_val, max_val)
            self.assertTrue(
                min_val <= rand_num <= max_val,
                f"Random value {rand_num} does not fall within the range",
            )

    def test_get_math_operator(self):
        """Unit test for get_math_operator()"""
        for _ in range(1000):  # Test a large number of random values
            operator = get_math_operator()
            operator_list = ["+", "-", "*"]
            self.assertIn(
                operator,
                operator_list,
                f"Operator {operator} does not fall in {operator_list}",
            )

    def test_generate_question(self):
        """Unit test for generate_question()"""
        test_cases = [
            (5, 2, "+", "5 + 2", 7),
            (1, 1, "+", "1 + 1", 2),
            (5, 5, "+", "5 + 5", 10),
            (3, 2, "+", "3 + 2", 5),
            (1, 1, "-", "1 - 1", 0),
            (1, 2, "-", "1 - 2", -1),
            (3, 2, "-", "3 - 2", 1),
            (5, 10, "-", "5 - 10", -5),
            (1, 2, "*", "1 * 2", 2),
            (5, 2, "*", "5 * 2", 10),
            (3, 7, "*", "3 * 7", 21),
            (9, 10, "*", "9 * 10", 90),
        ]

        for num_1, num_2, operator, expected_problem, expected_answer in test_cases:
            problem, answer = generate_question(num_1, num_2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
