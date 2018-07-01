## ex19.py FUNCTION JUNCTION VLL was here
## We are introduced to calling functions different ways
## Now we label each line and explain what it does

# This line defines the function "cheese_and_crackers"
# This line also defines args "cheese_count" and "boxes_of_crackers"
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# This line prints out the argument "cheese_count"
    print(f"You have {cheese_count} cheeses!")
# This line prints out the argument "boxes_of_crackers"
    print(f"You have {boxes_of_crackers} boxes of crackers!")
# This line prints a witty comment.
    print("man that's enough for a party!")
# This line prints out a non-sequitir
    print("Get a blanket.\n")

# This print statement is not inside the function
# It prints out a label for the next iteration of the
# > function
print("We can just give function numbers directly:")
# This assigns the numbers 20, 30 to the function arguments
cheese_and_crackers(20, 30)

# This prints a title for the third itteration of the function
print("OR, we can use variables from our script:")
# This assigns variable "amount_of_cheese" the value of 10
amount_of_cheese = 10
# This assigns the variable "amount_of_crackers" the value of 50
amount_of_crackers = 50

# This assigns two new variables to the function
# "amount_of_cheese", and "amount_of_crackers"
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# This prints a label for the next itteration of the script
print("We can even do math inside too:")
# This assigns the result of two math problems to each argument
# without expressly assigning the variables to specific arg names
cheese_and_crackers(10 + 20, 5 + 6)

# This prints a lable for the next itteration of the script
print("And we'can combine the two, variables and math:")
# This combines the value of specific argumemts with the values added
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

#...And that's all she wrote.
