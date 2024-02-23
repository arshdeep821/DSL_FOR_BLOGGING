import re

def parse_file(file_name):

    result = []

    with open(file_name, 'r') as f:
        for loc in f:

            parse_result = parse(loc)

            if type(parse_result) == str:
                return parse_result
            
            if len(parse_result) == 0:
                continue
            
            result.append(parse(loc))
    
    return result


def parse(loc):

    if len(loc.strip()) == 0:
        return []

    keyword = list(loc.split(" "))[0]

    if keyword == "function":
        return parse_function(loc)

    if keyword == "var":
        return parse_variable(loc)
    
    if keyword == "list":
        return parse_array(loc)
    
    if keyword == "add":
        return parse_add(loc)
    
    if keyword == "remove":
        return parse_remove(loc)
    
    if keyword == "if":
        return parse_conditional(loc)
    
    if keyword == "\n":
        return []
    
    return "SYNTAX ERROR: invalid keyword"
    

def parse_function(loc):
    regex_pattern = r'function [a-zA-Z_]\w* = create blog with \([a-zA-Z_]\w*=[\w\-./]+(, [a-zA-Z_]\w*=[\w\-./:]+)*\)'
    if not re.match(regex_pattern, loc):
        return "SYNTAX ERROR: invalid function declaration"
    parts = loc.split()
    attributes = loc[loc.index("(")+1:-2].split(", ")
    return ["function", parts[1]] + attributes  
    

def parse_variable(loc):
    regex_pattern = r'var [a-zA-Z_]\w* = [a-zA-Z_]\w* with text \(([^"]*)\)'
    if not re.match(regex_pattern, loc):
        return "SYNTAX ERROR: invalid variable declaration"
    
    parts = loc.split(" ")
    return ["var", parts[1], parts[3], loc[loc.index('(')+1:-2]]
    

def parse_array(loc):
    if loc == "list displayed_blog_posts\n":
        return list(loc[:-1].split(" "))
    return "SYNTAX ERROR: invalid array declaration"
    

def parse_conditional(loc):
    # TODO: we should check the conditional is one of the predefined ones (for now only is_night)
    regex_pattern = r'if \([a-zA-Z_]\w*\) then .*'
    if not re.match(regex_pattern, loc):
        return "SYNTAX ERROR: invalid conditional declaration"
    parts = loc.split()
    second_part = loc[loc.index("then ") + len("then "):]
    if isinstance(parse(second_part), str):
        return "SYNTAX ERROR: statement has syntax error"
    return ["if", parts[1][1:-1], "then"] + parse(second_part)


def parse_add(loc):
    regex_pattern = r'add [a-zA-Z_]\w* to displayed_blog_posts'
    if not re.match(regex_pattern, loc):
        return "SYNTAX ERROR: invalid add declaration"
    tokens = loc.split(" ")
    return ["add", tokens[1], "displayed_blog_posts"]


def parse_remove(loc):
    regex_pattern = r'remove [a-zA-Z_]\w* from displayed_blog_posts'
    if not re.match(regex_pattern, loc):
        return "SYNTAX ERROR: invalid remove declaration"
    tokens = loc.split()
    return ["remove", tokens[1], "displayed_blog_posts"]
