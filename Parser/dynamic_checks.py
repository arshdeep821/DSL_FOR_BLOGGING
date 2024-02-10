# Dynamic checks to do
# 1. have a running list of all declared functions and variables

def undeclared_function_error():
    return "DYNAMIC ERROR: You cannot use a function that has not been declared"

def undeclared_variable_error():
    return "DYNAMIC ERROR: You cannot use a variable that has not been declared"

# Returns True if passes dynamic checks, otherwise returns error message
def dynamic_checks(tokens):
    
    declared_functions = set()  # contains function names
    declared_variables = set()  # contains variable names


    def check_line(line):

        keyword = line[0]

        if keyword == "function":
            declared_functions.add(line[1])

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
        
        elif keyword == "if": # all conditionals previously declared
            return check_line(line[3:])
        
        else:
            return "DYNAMIC ERROR: This should never happen! Should be caught by static parser"
        
        return True



    for line in tokens:
        line_check_result = check_line(line)
        if line_check_result != True:
            return line_check_result
    
    return True