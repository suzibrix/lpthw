# exercise 6.a == the first edit by VLL (or VLK, take your pick)

# Here is the first variable {types_of_people}, defined as 10 (the number)
types_of_people = 10

# Variable x is defined by an "f- string" which is a format string.
# The f-string has a frame "There are _____ types of people."
# The variable {types_of_people} inserts the variable
### Nested string #1
x = f"There are {types_of_people} types of people."


# These novel string variables are almost literally self defining
binary = "binary"
do_not = "don't"
# ...Until we get here. Somebody snuck in another f_string into this stansa
# "y" is defined by the formatting string "Those who know ___ and those who ___."
# The two variables above are "binary" and "don't"
### Nested string #2
y = f"Those who know {binary} and those who {do_not}."

# Stupid, simple print commands. They look almost like lazy programming.
#They print string "x" and "y" respectively.
print(x)
print(y)

# THIS is more like it. A more formal print function printing an f"string
# The first print fuction prints a nested string with I said ___"
# The variable x inserts the string "There are 10 types of people."
# The second line prints nested string. Frame: "I also said ___"
# The second variable inserts variable y, "Those who know binary..."
## Nested string 3 & 4
print(f"I said: {x}")
print(f "I also said: '{y}'")

# "hilarious" is defined by the boolian value "False"
hilarious = False
# The variable "joke_evaluation" is defined by a string "Isn't that so funny?" 
# I believe that the brackets at the end catch the value of "hilarious" somehow

### Either this is nested string #5 or this is a trick question.
joke_evaluation = "Isn't that joke so funny?! {}"

# I believe that this function makes the squiggly brackets catch the variable "joke)evaluation" above
print(joke_evaluation.format(hilarious))

# These are more lazy programming, defining w as a string of text ("w" = "left...")
# Second line : "e" = "right..."
w = "this is the left side of..."
e = "a string with a right side."
# The lazy programmer prints "w" + "e", "+" appends the two variables together
# Somehow. I think because algebra doesn't care about what's inside the variable it still adds them together 
print(w + e)
