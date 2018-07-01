# ex 14 land. VLL was here 
# edit // change prompt
# This statement imports argv function from sys
from sys import argv

# assign script and user_name as args for argv
script, user_name, flip = argv
# assigns "$" as "prompt" 
prompt = '$'
# printf that prints a sentence with two arguments printed
print(f"Hi, {user_name}, I'm the {script} script.")
# print statement that states what the program will do next
print("I'd like to ask you a few questions.")
# asks first question using "user_name" arg to address a person by name
print(f"Do you like me {user_name}?")
# assigns "likes" to input
likes = input(prompt)
# prints statement with user_name asking for next input
print(f"Where do you live {user_name}?")
# assigns lives for input 
lives = input(prompt)

# queries for the next input
print("what kind of computer do you have?")
# takes input assigns to computer
computer = input(prompt)
# prints out formatted sentences with two argv 
# and another argument formatted into a sentence
print(f"""
Alright so you said {likes} about liking me.
You live in {lives}. Not sure where that is. 
{flip} makes you happy. Good show.
And you have a {computer} computer. Nice.
""")

