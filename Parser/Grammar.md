# Lexer Grammar

// (DEFAULT_MODE) <br>
BLOG_START: 'Blog Name:' WS* -> mode(TEXT_MODE);<br><br>






WS : [\r\n\t ] -> channel(HIDDEN);<br>
// hidden channel <br>

mode TEXT_MODE;<br>
TEXT: ~[[|\]\r\n]+ -> mode(DEFAULT_MODE);<br> 
// go back to DEFAULT after done text and dont want [ | and ] characters in Text



# Parser Grammar
program : start create commands* EOF; <br>
start : BLOG_START TEXT;
command : create | edit | loop | conditional
create : 
edit :
loop :
conditional :
