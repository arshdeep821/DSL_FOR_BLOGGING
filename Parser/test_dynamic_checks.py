import unittest 
import dynamic_checks as dynamic_checks

# TO RUN: python -m unittest test_dynamic_checks.py
class TestDynamic(unittest.TestCase):

    def test_dynamic_checker1(self):
        test_input = [["remove", "var_name", "displayed_blog_posts"]]
        expected_output = dynamic_checks.undeclared_variable_error()
        self.assertEqual(dynamic_checks.dynamic_checks(test_input), expected_output)
    
    def test_dynamic_checker2(self):
        test_input = [["function", "function_name", "key1=value1", "key2=value2"]]
        expected_output = True
        self.assertEqual(dynamic_checks.dynamic_checks(test_input), expected_output)
    
    def test_dynamic_checker3(self):
        test_input = [["list", "displayed_blog_posts"]]
        expected_output = True
        self.assertEqual(dynamic_checks.dynamic_checks(test_input), expected_output)
        
    def test_dynamic_checker4(self):
        test_input = [["function", "create_day_blog", "category=day", "color=blue"],
                      ["var", "blog_day", "create_day_blog", "How I stay awake during the day"]]
        expected_output = True
        self.assertEqual(dynamic_checks.dynamic_checks(test_input), expected_output)
    
    def test_dynamic_checker5(self):
        test_input = [["function", "create_day_blog", "category=day", "color=blue"],
                      ["var", "blog_day", "create_night_blog", "How I stay awake during the day"]]
        expected_output = dynamic_checks.undeclared_function_error()
        self.assertEqual(dynamic_checks.dynamic_checks(test_input), expected_output)
    