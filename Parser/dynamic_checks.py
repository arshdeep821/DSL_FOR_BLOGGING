# Dynamic checks to do
# 1. have a running list of all declared functions and variables

# Also img
valid_parameters = {
    "color": set(["white", "black", "red", "green", "blue", "yellow", "purple", "cyan", "magenta", "orange"]),
    "font": set(["verdana", "courier"]),
    "size": set(["small", "medium", "large"]),
}

valid_conditionals = set(["day", "night"])

def undeclared_function_error():
    return "DYNAMIC ERROR: You cannot use a function that has not been declared"

def undeclared_variable_error():
    return "DYNAMIC ERROR: You cannot use a variable that has not been declared"

def invalid_parameter_key_error():
    return "DYNAMIC ERROR: Invalid function parameter key (valid example would be color, font, size, image)"

def invalid_parameter_value_error(key):
    return "DYNAMIC ERROR: Invalid function parameter value for " + key

def invalid_conditional_variable_error():
    return "DYNAMIC ERROR: Invalid conditional variable (valid example would be day or night)"

def nested_conditionals_error():
    return "DYNAMIC ERROR: No Nested Conditionals Allowed"

# Returns True if passes dynamic checks, otherwise returns error message
def dynamic_checks(tokens):
    
    declared_functions = set()  # contains function names
    declared_variables = set()  # contains variable names


    def check_line(line):

        keyword = line[0]

        # -> ["function", "function_name", "key1=value1", "key2=value2"]
        if keyword == "function":
            declared_functions.add(line[1])
            for key_value_pair in line[2:]:
                key, value = key_value_pair.split("=")
                # handle image
                if key not in valid_parameters and key != "image":
                    return invalid_parameter_key_error()
                
                if key in valid_parameters and value not in valid_parameters[key]:
                    return invalid_parameter_value_error(key)
                
        elif keyword == "var":
            if line[2] not in declared_functions:
                return undeclared_function_error()
            declared_variables.add(line[1])
        
        elif keyword == "list":
            pass
        
        elif keyword == "add":
            if line[1] not in declared_variables:
                return undeclared_variable_error()
        
        elif keyword == "remove":
            if line[1] not in declared_variables:
                return undeclared_variable_error()
        
        # -> ["if", "predefined_conditional_variable", "then", ...]
        elif keyword == "if": # all conditionals previously declared
            if line[1] not in valid_conditionals:
                return invalid_conditional_variable_error()
            if line[3] == "if":
                return nested_conditionals_error()

            return check_line(line[3:])
        
        else:
            return "DYNAMIC ERROR: This should never happen! Should be caught by static parser"
        
        return True



    for line in tokens:
        line_check_result = check_line(line)
        if line_check_result != True:
            return line_check_result
    
    return True