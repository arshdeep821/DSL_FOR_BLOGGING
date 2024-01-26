# Lexer Grammar

// (DEFAULT_MODE) <br>
BLOG_START: 'Blog Name:' WS* -> mode(TEXT_MODE);<br>
CREATE_POST: 'Create Post: ' -> mode(TEXT_MODE);<br>
EDIT_POST
LOOP_POST
IF_POST


WS : [\r\n\t ] -> channel(HIDDEN);<br>
// hidden channel <br>

mode TEXT_MODE;<br>
TEXT: ~[[|\]\r\n]+ -> mode(DEFAULT_MODE);<br> 
// go back to DEFAULT after done text and dont want [ | and ] characters in Text



# Parser Grammar
program : start create commands* EOF; <br>
start : BLOG_START TEXT;<br>
command : create | edit | loop | conditional<br>
create : CREATE_POST TEXT; <br>
edit : EDIT_POST TEXT; <br>
loop : LOOP_POST TEXT; <br>
conditional : IF_POST TEXT; <br>
