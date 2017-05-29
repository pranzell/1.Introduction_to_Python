import re

line = "Hello my name   is     Pranjal Pathak. I am 23 years old.  Period. ";


# ---VARIOUS STRING FUNCTIONS  --------

replace_text = line.replace(" ", "+");
print replace_text;

regex_text = re.sub(r"\s+", "+", line);
print regex_text;

split_list = line.split();
print split_list;