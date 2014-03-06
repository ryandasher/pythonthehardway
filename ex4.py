# Set cars to an integer of 100.
cars = 100
# Set space_in_a_car to a floating point number. 
space_in_a_car = 4.0
# Set drivers to an integer of 30.
drivers = 30
# Set passengers to an integer of 90.
passengers = 90
# Subtract the amount of cars from drivers to get the number of cars not being driven.
cars_not_driven = cars - drivers
# Set the variable cars_driven to the amount of drivers.
cars_driven = drivers
# Multiply the cars_driven from the space_in_a_car to find your carpool_capacity.
carpool_capacity = cars_driven * space_in_a_car
# Divide the amount of passengers from the amount of cars being driven.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Zed received the NameError because he incorrectly referenced the carpool_capacity variable, which is defined on line 6. He had referred to it as car_pool_capacity.

# Study drill 1: Using a floating point number in this case is not necessary. you get the same result if you use a simple integer.

# Study drill 2: Floating point numbers use scientific notation, so they're more precise than integers.

# Study drill