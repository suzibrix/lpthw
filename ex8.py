# welcome to 8 land brought to you by VLL
# we feed a variable called "formatter" series of 4 brackets 
# separated by a single space
formatter = "{} {} {} {}"

# print our "formatter" variable, then format with four integers
print(formatter.format(1 , 2, 3, 4))

# print our same formatter variable, only this time with four strings
print(formatter.format("one", "two", "three", "four"))

# print our same formatter again, this time boolian values. they work too
print(formatter.format(True, False, False, True))
# print our formatter with recursive formatters, and we get 16 brackets
# who knew that would look so cool.
print(formatter.format(formatter, formatter, formatter, formatter))
# this formats longer strings into those same square brackets? Maybe
# clearly the formatting with tabs and whatnot doesn't affect how it looks
# <--when printed.
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"

))
