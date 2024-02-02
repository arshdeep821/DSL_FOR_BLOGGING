Use this file to commit information clearly documenting your check-ins' content. If you want to store more information/details besides what's required for the check-ins that's fine too. Make sure that your TA has had a chance to sign off on your check-in each week (before the deadline); typically you should discuss your material with them before finalizing it here.


## Check-in 1

#### Brief Description

###### High Level Purpose
Utilizing the concept of literate programming, the DSL provides a low-code solution to generate CSS, HTML files with minimum effort.

The high-level purpose of our DSL is to provide non-programmers with the ability to make and maintain their own blog website. Aiming for users that are not accustomed to programming or prefer a simplistic mode of blogging on the internet. It will allow users to create and update different posts on the blog page.

###### Rich Features

**Functions:** User can define functions in our DSL that quickly create new blogs with less duplicate code. 

**Array:** Users can add, remove (possibly sort) blog posts from an array. This array could represent the blog posts currently being shown on the screen.

**Variables:** Users can store blog posts in variables so they can be referenced or updated in later code (perhaps inside a future conditional statement).

**Conditionals:** Users can perform actions conditionally (e.g. reassign blog post variable, add and remove from displayed blog post array).

###### Example Snippets
The example snippet below shows how the above features can work together.

<img width="625" alt="Screenshot 2024-01-19 at 3 03 21 PM" src="https://media.github.students.cs.ubc.ca/user/16895/files/accbdaf9-cdb5-493f-a2b0-368be7a43f51">

#### TA Changes/Feedback

TA recommended to use conditionals in order to add more functionality (display blog depending on time of day)

#### Planned Follow-up

Further developping features with more specificity. 

## Check-in 2

#### Planned Division

###### Modular design

The design of the system is separated into two parts; the parser and the backend. Parser will take in the user’s input and turn into an AST containing all the commands. Backend will take that list and formulate a website for the user’s blog. At the moment, Sahib and Ilya are responsible for working on the parser with Arshdeep, Mickey and Jackson taking over the backend. If the situation calls for it, team members may move between parser and backend but that is dependent on progress and difficulty. 

###### Data at Interface Points

The parser takes in a String and turns into its respective AST. 
The backend takes the AST and turns it into HTML components. 
At the moment, the structure of the AST will be an ordered list of parsed commands.

###### Build/Test

Both components can be tested for and built separately as the parser will generate and the backend will use the AST.  <br>
The same people writing the code will write their respective tests as they know how to test the component they are working on the best

###### Other Project Tasks

As for our group so far, there are no other project tasks that are currently assigned other than these components.

#### RoadMap

The plan is to frontload the schedule due to other midterms appearing closer to the deadline. By next week, there should be a functioning parser that is able to do simple commands. For the backend, we should have a website that can visualize the elements of a blog. The group plans to meet up 1-2 times a week to check in and see how everyone is doing, as well as to resolve problems that each person is having. If someone falls behind due to the difficulty of a task, other group members who are done their part will coordinate to get them back on track to continue finishing the project on time

#### Summary

None as of yet, will update with time. 


## Check-in 3

#### Explain a mockup of your concrete language design

###### Define Functions

function create_day_blog = create blog with (category=day, color=blue) <br>
function create_night_blog = create blog with (category=night, color=black)<br>

- function <FUNCTION_NAME> = create blog with (category=<NAME>, color =<COLOR>)

###### Define mutable variables

var blog_day = create_day_blog with text "How I stay awake during the day"<br>
var blog_night = create_health_blog with text "How I fall asleep at night"

- var <BLOG_NAME> = <FUNCTION_NAME> with text "<BLOG_TEXT>"

###### Define displayed_blog_posts as array

list displayed_blog_posts


###### Update

add blog_day to displayed_blog_posts<br>
remove blog_day from displayed_blog_posts

- add <BLOG_NAME> to <LIST_NAME><br>
- remove <BLOG_NAME> from <LIST_NAME>

###### Conditional

if is_night then add blog_day to displayed_blog_posts <br>

if is_2025 then var blog_day = create_day_blog with text "How I stay awake during the day"<br>

- if <PREDEFINED_CONDITION> then <COMMAND_LINE> <br>
  e.g. night-time
  
#### Notes about your first user study
  
###### Code Written by User

<img width="654" alt="Screenshot 2024-02-02 at 10 08 27 AM" src="https://media.github.students.cs.ubc.ca/user/16895/files/f563376b-1808-4735-8840-2b00df253c82">
  
###### User's thoughts

One user thought that the syntax was relatively easy to understand, and was glad with the amount of customisation. However, user did find that the switching between brackets and quotation marks was not the most intuitive, as well as had few questions on the amount of whitespace.
  
###### Going forward with User study

Using the feedback form the user, we will use their valuable information to further develop our syntax for the DSL, working on the whitespace as well as using brackets and quotations in a way that feels reasonable to the user. 
  
#### Changes 

We are definitely considering expanding the customisation, allowing for different lists to be made, as well as further developing the conditional variables.  
  
#### Timeline
No big changes to be made. 
  
#### Tests
There definitely can be unit tests made for the parser, as we decided against using ANTLR for our project. Each statement will have its own set of tests as well as the specific eror codes that get sent. 
