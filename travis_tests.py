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

if __name__ == '__main__':
    unittest.main()
