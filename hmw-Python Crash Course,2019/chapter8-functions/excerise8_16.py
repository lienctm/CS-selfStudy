# Using a program you wrote that has one function in it, store that function in a separate file. 
# Import the function into your main program file

import hello
import hello as hl
from hello import hello_user
from hello import hello_user as hu

hello.hello_user('Lily')
hl.hello_user("Anna")
hello_user("Ken")
hu("Bi")