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

The design of the system is separated into two parts; the parser and the backend. Parser will take in the user’s input and turn into a list of tokens. Backend will take that list and formulate a website for the user’s blog. At the moment, Sahib and Ilya are responsible for working on the parser with Arshdeep,  Mickey and Jackson taking over the backend. If the situation calls for it, Ilya may be jointly responsible for both but that is dependent on progress and difficulty. 

###### Data at Interface Points

The parser takes in a String and turns into its respective AST. 
The backend takes the AST and turns it into HTML components. 

###### Build/Test

Both components can be tested for and built separately as the parser will generate and the backend will use the list of tokens.  <br>
The same people writing the code will write their respective tests as they know how to test the component they are working on the best

###### Other Project Tasks

As for our group so far, there are no other project tasks that are currently assigned other than these components.

#### RoadMap

The plan is to frontload the schedule due to other midterms appearing closer to the deadline. By next week, there should be a functioning parser that is able to do simple commands. For the backend, we should have a website that can visualize the elements of a blog. The group plans to meet up 1-2 times a week to check in and see how everyone is doing, as well as to resolve problems that each person is having. If someone falls behind due to the difficulty of a task, other group members who are done their part will coordinate to get them back on track to continue finishing the project on time

#### Summary

None as of yet, will update with time. 
