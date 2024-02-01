# Define Functions

function create_day_blog = create blog with (category=day, color=blue) <br>
function create_night_blog = create blog with (category=night, color=black)

- function <FUNCTION_NAME> = create blog with (category=<CAT_NAME>, color =<BLOG_COLOR>)

# Define mutable variables

var blog_day = create_day_blog with text "How I stay awake during the day" <br>
var blog_night = create_health_blog with text "How I fall asleep at night"

- var <BLOG_NAME> = <FUNCTION_NAME> with text "<BLOG_TEXT>"

# Define displayed_blog_posts as array

## list displayed_blog_posts

list displayed_blog_posts <br>
list <LIST_NAME>

# Update

add blog_day to displayed_blog_posts <br>
remove blog_day from displayed_blog_posts

- add <BLOG_NAME> to <LIST_NAME> <br>
  remove <BLOG_NAME> from <LIST_NAME>

# Conditional

if is_night then add blog_day to displayed_blog_posts

if is_2025 then var blog_day = create_day_blog with text "How I stay awake during the day"

- if <PREDEFINED_CONDITION> then <COMMAND_LINE>
  e.g. night-time
