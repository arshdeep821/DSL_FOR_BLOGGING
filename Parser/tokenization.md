# TOKENIZATION

## Functions

```
function function_name = create blog with (key1=value1, key2=value2)
-> ["function", "function_name", "key1=value1", "key2=value2"]

function create_day_blog = create blog with (category=day, color=blue)
-> ["function", "create_day_blog", "category=day", "color=blue"]
```

## Variables

```
var var_name = function_name with text (text)
-> ["var", "var_name", "function_name", "text"]

var blog_day = create_day_blog with text (How I stay awake during the day)
-> ["var", "blog_day", "create_day_blog", "How I stay awake during the day"]
```

## Lists

```
list displayed_blog_posts
-> ["list", "displayed_blog_posts"]

add var_name to displayed_blog_posts
-> ["add", "var_name", "displayed_blog_posts"]

remove var_name from displayed_blog_posts
-> ["remove", "var_name", "displayed_blog_posts"]
```

## Conditionals

```
NOTE: after "then" must be identical to previous operation (above)
if (predefined_conditional_variable) then ...
-> ["if", "predefined_conditional_variable", "then", ...]
```
