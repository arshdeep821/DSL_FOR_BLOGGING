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
  
###### Code Written by User 1

<img width="654" alt="Screenshot 2024-02-02 at 10 08 27 AM" src="https://media.github.students.cs.ubc.ca/user/16895/files/f563376b-1808-4735-8840-2b00df253c82">
  
###### User's thoughts

One user thought that the syntax was relatively easy to understand, and was glad with the amount of customisation. However, user did find that the switching between brackets and quotation marks was not the most intuitive, as well as had few questions on the amount of whitespace.
  
###### Going forward with User study

Using the feedback from the user, we will use their valuable information to further develop our syntax for the DSL, working on the whitespace as well as using brackets and quotations in a way that feels reasonable to the user. 
  
###### Code Written by User 2
  
  <img width="553" alt="Screenshot 2024-02-02 at 2 35 43 PM" src="https://media.github.students.cs.ubc.ca/user/16810/files/565991f2-faf6-400a-bf06-b9cbb1a6c8c6">
  
###### User's thoughts
  
- Add brackets to increase readability, for the conditional to make it easier to read
- Was confused about what to declare the category as, felt it was pretty open ended
- Syntax is easy to understand
- Very intuitive for someone from a non coding background
- A little wordy, maybe somethings can be shortened
  
###### Going forward with User study
  
Using this feedback from the user, we can work on improving some ambiguous functionality, and maybe shortening the wording.

#### Changes 

We are definitely considering expanding the customisation, allowing for different lists to be made, as well as further developing the conditional variables.  We also brainstormed the AST's data structure implementation, constructed mock ASTs and discussed use of ANTLR. 
  
#### Timeline
No big changes to be made. 
  
#### Tests
There definitely can be unit tests made for the parser, as we decided against using ANTLR for our project. Each statement will have its own set of tests as well as the specific eror codes that get sent. 
  
## Check-in 4
  
#### Status of Implementation
Parser is working and is implemented aside from some comments made from the first user study. There are also unit tests for static parsing. The two group members working on the parser (Sahib and Ilya) will now implement the dynamic checks to alleviate some work of backend. All tests are passing for the parser and there will be no new parser tests.
  
The evaluator for the backend is comlpete, meaning all the tokens are analyzed correctly and HTML components are made from them. We are now working on the functionality related to rendering the actual HTML components (which are already created) onto index.html so the user can view them as the site is deployed. Tests still need to be written for the backend.
 
  
#### Plans for final user study
Difference is that users should be able to see the output of their written code lines, compared to the first user study having only trying out the syntax and grammar of our DSL. 

#### Timeline
- Monday, February 12th: Minimum Viable Product (MVP) ready for manual end-to-end testing.
- Friday, February 16th: Project completion with automated testing implemented wherever feasible and practical. Also have completed final user studies.
- Later: If time allows, incorporate additional features identified through user studies.

## Check-in 5
  
#### Status of user study
  
Overall feedback from the user study was pretty good, the code is less ambiguous than before, a little bit more intuitive and fairly easy for a person with limited programming experience to grasp onto. Key elements of feedback we gained was mainly parts of code that are slightly ambiguous, having elements such as brackets around the text of the blog helped users understand directly which text the blog will display. If conditions were a little ambiguous was as well so it was simplified down to a single line if statement, which is more readable according to the users. Overall the final user studies went smoother than the first due to our improvements on the DSL and we basically asked a user to work with each one of the DSL's main features.
  
#### Status of Implementation
The backend server is implemented and tested to be functional. The evaluator is able to generate HTML file with basic styling based on test inputs. However, there will be a delay on the delivery of the production ready backend evaluator service, as that extensive testing, refactoring and bug fixing are still required
  
#### Final Video
- This week, we will mostly work on planning and creating our project video.
- We will all try to plan it together then we will choose someone to present it.
- Our TA suggested using a MacBook to create the video since you can screen and voice record at the same time.

#### Additional Tasks
- Debugging: We will continue to test our program and make sure everything works end-to-end, catching errors as we go.
- Improvements: There will always be improvements to add, so this depends on how much time we have. We will prioritize making the blog posts look nicer (improving styling) and making new features/changes collected from the user studies.

