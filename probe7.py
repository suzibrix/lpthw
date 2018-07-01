# This is the probe from ex13. VLL was here
# we are supposed to cobine argv and input
# we are not supposed to over think it
# I will try that. It will be a new experience

from sys import argv

script, something, something_else, = argv

print(f"Running this {script} resulted in {something} you may not understand.")
print(f"How do you know {something_else} has happened?")
print(f"Because you see {something_else} here.")

programming = input("How long have you been programming?")
quest = input("What is your quest through programming?")
color = input("What is your favorite color while programming?")

print(f"You have been hacking for {programming}, and your quest is to make {quest} successful. Your wish shall be granted with {color} clouds of magic.")
print(f"We want to see if {script} is running properly.")
print(f" Is it {something} or {something_else}? The world only sees in {color}.")
