from dsl_parser import parse_file 

for line in parse_file("input_files/correct.txt"):
    print(line)