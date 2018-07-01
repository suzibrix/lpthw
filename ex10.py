# -- Welcome to ex10 brought to you by VLL ## Second go around--let's document!!!
### breaking things...yes
# Here we assign some strings to some variables
# We get cute with text based lolcats
#
# "Tabby" cat demonstrates the tab function with "\t"
tabby_cat = "\ tI'm tabbed in."
#
# "persian_cat" demonstrates how \n creates a new line
# persian new line doesn't care. Sorta like honeybadger
persian_cat = "I'm split\non a line."
#
# backslash cat reminds us of the special abilities of "\"
# backslash cat even works on himself.
backslash_cat = "I'm \ a \\ cat."

# fat_cat is lazy cat. He eats up ALL the text brought to us by >
# those three double quotes of speialness
# -- on top of that, we get to see how to format lists with \t
# That last line teaches how people can be sneaky/elegant with formatting
# by formatting two lines worth of text with one line.
fat_cat = """

I'll do a list : /N \t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
# this is the "show your work" stanza
# A series of print statements that show us how all of the assigned variables
# look in the wild.
# Let's print tabby_cat and see tabs tabbed in
print(tabby_cat)
# let's print persian_cat not caring about text crowding \n
print(persian_cat)
# Lets print backslash_cat printing backslashes by using backslashes
print(backslash_cat)
# Let's watch fat_cat's shopping list grow and grow like his belly
print(fat_cat)

# Quick question : why does vim make comments and print statments the same color?
