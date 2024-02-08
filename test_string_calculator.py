import unittest

class StringCalculator:
    @staticmethod
    def add(numbers):
        # If string is empty, return 0
        if not numbers:
            return 0

        # Support different separators
        delimiter = ","
        if numbers.startswith("//"):
            parts = numbers.split("\n", 1)
            delimiter = parts[0][2:]
            numbers = parts[1]

        # Standardize separators (comma and newline)
        numbers = numbers.replace("\n", delimiter)
        number_list = numbers.split(delimiter)

        # Negative number check
        negatives = [int(x) for x in number_list if int(x) < 0]
        if negatives:
            raise Exception(f"negatives not allowed: {', '.join(map(str, negatives))}")

        # Add the numbers
        return sum(int(x) for x in number_list if x.isdigit())
    # Here is an example where we see that the test method works correctly with the parameter given to the method.
    print(add("1,-2,3"))

class TestStringCalculator(unittest.TestCase):

    def test_empty_string_returns_zero(self):
        self.assertEqual(StringCalculator.add(""), 0)
        

    def test_single_number_returns_value(self):
        self.assertEqual(StringCalculator.add("1"), 1)

    def test_two_numbers_comma_delimited_returns_sum(self):
        self.assertEqual(StringCalculator.add("1,2"), 3)

    def test_handle_new_lines_as_delimiters(self):
        self.assertEqual(StringCalculator.add("1\n2,3"), 6)

    def test_support_different_delimiters(self):
        self.assertEqual(StringCalculator.add("//;\n1;2"), 3)

    def test_negative_numbers_throw_exception(self):
        with self.assertRaises(Exception) as context:
            StringCalculator.add("-1,2")
        self.assertTrue("negatives not allowed" in str(context.exception))

       



