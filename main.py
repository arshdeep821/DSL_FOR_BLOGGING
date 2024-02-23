from Parser.dsl_parser import parse_file 
from Parser.dynamic_checks import dynamic_checks
import requests 


def run_program():

    tokens_result = parse_file("Parser/Inputs/input13.txt")
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

    # input.txt
    # data = {
    #     "tokens": [
    #         ["list", "displayed_blog_posts"],
    #         ["function", "create_day_blog", "category=day", "color=blue"],
    #         ["var", "blog_day", "create_day_blog", "How I stay awake during the day"],
    #         ["add", "blog_day", "displayed_blog_posts"]

    #     ]
    # }

    # input2.txt
    # data = {
    #     "tokens": [
    #         ["list", "displayed_blog_posts"],
    #         ["function", "create_day_blog", "category=day", "color=blue"],
    #         ["function", "create_night_blog", "category=night", "color=purple"],
    #         ["var", "blog_day", "create_day_blog", "How I stay awake during the day"],
    #         ["var", "blog_night", "create_night_blog", "How I stay awake during the night"],
    #         ["add", "blog_day", "displayed_blog_posts"],
    #         ["add", "blog_night", "displayed_blog_posts"]
    #     ]
    # }

    # input3.txt
    # data = {
    #     "tokens": [
    #         ["list", "displayed_blog_posts"],
    #         ["function", "create_night_blog", "color=purple"],
    #         ["function", "create_school_blog", "font=verdana", "size=large", "color=orange"],
    #         ["function", "create_day_blog", "font=courier", "size=small", "image=https://cdn.britannica.com/79/232779-050-6B0411D7/German-Shepherd-dog-Alsatian.jpg"],
    #         ["var", "blog_day", "create_day_blog", "How I stay awake during the day"],
    #         ["var", "blog_night", "create_night_blog", "How I stay awake during the night"],
    #         ["var", "blog_school", "create_school_blog", "How I pass all my classes"],
    #         ["add", "blog_school", "displayed_blog_posts"],
    #         ["add", "blog_night", "displayed_blog_posts"],
    #         ["add", "blog_day", "displayed_blog_posts"],
    #         ["remove", "blog_school", "displayed_blog_posts"],
    #     ]
    # }

    # print("DEBUG: GOT TO HERE")

    # input4.txt
    # data = {
    #     "tokens": [
    #         ["list", "displayed_blog_posts"],
    #         ["function", "create_night_blog", "color=red", "size=medium"],
    #         ["function", "create_school_blog", "font=verdana", "size=large", "color=orange"],
    #         ["function", "create_day_blog", "font=courier", "size=small", "image=https://hips.hearstapps.com/hmg-prod/images/dog-puppy-on-garden-royalty-free-image-1586966191.jpg"],
    #         ["var", "blog_day", "create_day_blog", "How I stay awake during the day"],
    #         ["var", "blog_night", "create_night_blog", "How I stay awake during the night"],
    #         ["var", "blog_school", "create_school_blog", "How I pass all my classes"],
    #         ["add", "blog_school", "displayed_blog_posts"],
    #         ["add", "blog_day", "displayed_blog_posts"],
    #         ["if", "night", "then", "add", "blog_night", "displayed_blog_posts"],
    #     ]
    # }

        # input5.txt
    # data = {
    #     "tokens": [
    #         ["list", "displayed_blog_posts"],
    #         ["function", "create_day_blog", "color=blue"],
    #         ["var", "blog_day", "create_day_blog", "How I stay awake during the day"],
    #         ["add", "blog_day", "displayed_blog_posts"],
    #         ["add", "blog_day", "displayed_blog_posts"],
    #     ]
    # }

    # input6.txt
    # data = {
    #     "tokens": [
    #         ["function", "create_day_blog", "color=blue"],
    #         ["var", "blog_day", "create_day_blog", "How I stay awake during the day"],
    #         ["add", "blog_day", "displayed_blog_posts"],
    #     ]
    # }

    # input7.txt
    # data = {
    #     "tokens": [
    #         ["function", "create_day_blog", "color=blue"],
    #         ["var", "blog_day", "create_day_blog", "How I stay awake during the day"],
    #         ["remove", "blog_day", "displayed_blog_posts"],
    #     ]
    # }


    print("ALL CHECKS PASSED")
    print("HERE ARE THE TOKENS BEING SENT")
    print(tokens_result)
    
    payload = {"tokens": tokens_result}
    response = requests.post(url, headers=headers, json=payload)
    print(response.text)


run_program()