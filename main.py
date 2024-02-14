from Parser.dsl_parser import parse_file 
from Parser.dynamic_checks import dynamic_checks
import requests 


def run_program():

    tokens_result = parse_file("Parser/input.txt")
    if type(tokens_result) == str:
        print(tokens_result)
        return

    dynamic_checks_result = dynamic_checks(tokens_result)
    if dynamic_checks_result != True:
        print(dynamic_checks_result)
        return
    
    # Call backend using API call
    url = "http://localhost:3000/api/v1/data"

    headers = {
        "Content-Type": "application/json"
    }

    # data = {
    #     "tokens": [
    #         ["list", "displayed_blog_posts"]
    #     ]
    # }

    data = {
        "tokens": [
            ["list", "displayed_blog_posts"],
            ["function", "create_day_blog", "category=day", "color=blue"],
            ["var", "blog_day", "create_day_blog", "How I stay awake during the day"],
            ["add", "blog_day", "displayed_blog_posts"]

        ]
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.text)


run_program()