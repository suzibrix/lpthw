# This line assigns 100 to the variable "cars"
cars = 100
# This statement assigns the number "4.0" to the variable "space_in_car"
space_in_a_car = 4.0

# Assigns the number 30 to the variable "drivers"
drivers = 30

# Assigns the number 90 to the variable "passengers"
passengers = 90

# Assigns the difference of variable "cars" and "drivers" to "cars_not_driven"
cars_not_driven = cars - drivers

# Assigns the number stored in "drivers" to the variable "cars_driven"
cars_driven = drivers

# Assigns the multiple of "cars_driven" and "space_in_car" to "carpool_capacity"
carpool_capacity = cars_driven * space_in_a_car

# Assigns the dividend of the total of "passengers" and "cars_driven" 
average_passengers_per_car = passengers / cars_driven

#
# Let's show our work
#

# Insert variable $cars into printable string revealing # of cars
print("There are", cars, "cars available.")

# Insert the variable $drivers into printable string displaying number of drivers
print("There are only", drivers, "drivers available.")

# Insert $cars_not_driven into printable string demonstrating number of unused vehicles
print("There will be", cars_not_driven, "empty cars today.")

# Insert variable $carpool_capacity into the number of people that can be driven today
print("We can transport", carpool_capacity, "people today.")

# Insert variable $passengers into the string printing how many passengers are in need of transportation
print("We have", passengers, "to carpool today.")

# Insert the variable of $average_passengers_per_car into a string printing the number of people per car
print("We need to put about", average_passengers_per_car, "in each car.")
