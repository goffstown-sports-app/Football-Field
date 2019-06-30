import unittest
import utility_functions as UF


class TravisTests(unittest.TestCase):
    """
    Will run unittests for functions.
    """

    ###############################################
    #Testing the functions in utility_functions.py#
    ###############################################

    def test_check_type(self):
        """
        Tests the check_type function
        """
        string_result = UF.check_type("", "string")
        int_result = UF.check_type(0, "int")
        float_result = UF.check_type(0.0, "float")
        tuple_result = UF.check_type((), "tuple")
        list_result = UF.check_type([], "list")
        dict_result = UF.check_type({}, "dict")
        bool_result = UF.check_type(True, "bool")
        self.assertEqual(string_result, "<class 'str'>")
        self.assertEqual(int_result, "<class 'int'>")
        self.assertEqual(float_result, "<class 'float'>")
        self.assertEqual(tuple_result, "<class 'tuple'>")
        self.assertEqual(list_result, "<class 'list'>")
        self.assertEqual(dict_result, "<class 'dict'>")
        self.assertEqual(bool_result, "<class 'bool'>")

    def test_safe_cast(self):
        """
        Tests the safe_cast function
        """
        string_result = UF.safe_cast("string", False)
        number_result = UF.safe_cast("0", False)
        zero_to_false_result = UF.safe_cast("0", True)
        one_to_true_result = UF.safe_cast("1", True)
        self.assertEqual(string_result, "string")
        self.assertEqual(number_result, 0)
        self.assertEqual(zero_to_false_result, False)
        self.assertEqual(one_to_true_result, True)


if __name__ == '__main__':
    unittest.main()
