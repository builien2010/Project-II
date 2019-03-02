'''
import re

string = "ABCDEFabcdef123450"

charRe = re.compile(r'[a-zA-Z]')
string = charRe.match(string)
print(string)
'''
'''
my_string = "↵      tryit1.tar↵      " 
acceptable_characters = string.letters + string.digits + "-_*." 
filter(lambda c: c in acceptable_characters, my_string) 
'''

import re 
string = "1234aaaabc12:" 
print(re.sub(r'[^a-zA-Z]', '', string) )