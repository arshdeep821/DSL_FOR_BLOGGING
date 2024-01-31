import unittest 
import dsl_parser

# TO RUN: python -m unittest test_dsl_parser.py

class TestParse(unittest.TestCase):
    def test_parse_array(self):
        parser_input = "list displayed_blog_posts\n"
        expected_output = ["list", "displayed_blog_posts"]
        self.assertEqual(dsl_parser.parse(parser_input), expected_output)
        parser_input2 = "list displayed_blog_postsssss"
        self.assertTrue(dsl_parser.parse(parser_input2).startswith("SYNTAX ERROR"))


    def test_parse_add(self):
        # Correct
        parser_input = "add yeet to displayed_blog_posts"
        expected_output = ["add", "yeet", "displayed_blog_posts"]
        self.assertEqual(dsl_parser.parse(parser_input), expected_output)

        # Extra Words
        parser_input = "add yeet from displayed_blog_postss"
        expected_output = "SYNTAX ERROR: invalid add declaration"
        self.assertEqual(dsl_parser.parse(parser_input), expected_output)
        
        # No Spaces
        parser_input = "addyeettodisplayed_blog_posts"
        expected_output = "SYNTAX ERROR: invalid keyword"
        self.assertEqual(dsl_parser.parse(parser_input), expected_output)

        # Numbers as variable names
        parser_input = "add 1234 to displayed_blog_posts"
        expected_output = "SYNTAX ERROR: invalid add declaration"
        self.assertEqual(dsl_parser.parse(parser_input), expected_output)

        # Sy as variable names
        parser_input = "add 1234 to displayed_blog_posts"
        expected_output = "SYNTAX ERROR: invalid add declaration"
        self.assertEqual(dsl_parser.parse(parser_input), expected_output)
        

        
    def test_parse_remove(self):

        parser_inputs = [
            "remove var_name from displayed_blog_posts",
            "remove 999_invalid_var_name from displayed_blog_posts",
            "remove variable_name from invalid_array_name",
        ]
        
        expected_outputs = [
            ["remove", "var_name", "displayed_blog_posts"], 
            "SYNTAX ERROR: invalid remove declaration",
            "SYNTAX ERROR: invalid remove declaration",
        ]

        for i in range(len(parser_inputs)):
            self.assertEqual(dsl_parser.parse(parser_inputs[i]), expected_outputs[i])


    def test_parse_variable(self):
        parser_inputs = [
            'var var_name = create_day_blog with text "Here is some valid text for a blog"\n',
            'varvar_name = no_space with test "this should not work"\n',
            'var var_name= forgot_a_space with test "this should not work"\n',
        ]
        
        expected_outputs = [
            ["var", "var_name", "create_day_blog", "Here is some valid text for a blog"], 
            "SYNTAX ERROR: invalid keyword",
            "SYNTAX ERROR: invalid variable declaration",
        ]

        for i in range(len(parser_inputs)):
            self.assertEqual(dsl_parser.parse(parser_inputs[i]), expected_outputs[i])


    def test_parse_function(self):
        parser_inputs = [
            'function function_name = create blog with (key1=value1, key2=value2)\n',
            'function function_name = create blog with (key1=value1,key2=value2)\n',
            'function function_name= create blog with (key1=value1, key2=value2)\n',
            'function function_name =create blog with (key1=value1, key2=value2)\n',
            'functionfunction_name = create blog with (key1=value1, key2=value2)\n',
        ]
        
        expected_outputs = [
            ["function", "function_name", "key1=value1", "key2=value2"], 
            "SYNTAX ERROR: invalid function declaration",
            "SYNTAX ERROR: invalid function declaration",
            "SYNTAX ERROR: invalid function declaration",
            "SYNTAX ERROR: invalid keyword",
        ]

        for i in range(len(parser_inputs)):
            self.assertEqual(dsl_parser.parse(parser_inputs[i]), expected_outputs[i])


    def test_parse_conditional(self):
        # Correct
        parser_input = "if night then add yeet to displayed_blog_posts\n"
        expected_output = ["if", "night", "then", "add", "yeet", "displayed_blog_posts"]
        self.assertEqual(dsl_parser.parse(parser_input), expected_output)

        # No Spaces
        parser_input = "ifnightthen add yeet to displayed_blog_posts"
        expected_output = "SYNTAX ERROR: invalid keyword"
        self.assertEqual(dsl_parser.parse(parser_input), expected_output)

        # Wrong Syntax
        parser_input = "if night thens add yeet to displayed_blog_posts"
        expected_output = "SYNTAX ERROR: invalid conditional declaration"
        self.assertEqual(dsl_parser.parse(parser_input), expected_output)

        # Statement has wrong syntax
        parser_input = "if night then add yeet todo displayed_blog_posts"
        expected_output = "SYNTAX ERROR: statement has syntax error"
        self.assertEqual(dsl_parser.parse(parser_input), expected_output)

        # Double Correct
        parser_input = 'if night then if midnight then var var_name = create_day_blog with text "Here is some valid text for a blog"\n'
        expected_output = ["if", "night", "then", "if", "midnight", "then", "var", "var_name", "create_day_blog", "Here is some valid text for a blog"]
        self.assertEqual(dsl_parser.parse(parser_input), expected_output)

        



