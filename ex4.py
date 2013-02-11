# The number of total cars available.
cars = 100
# The amount of seats in each car.
space_in_a_car = 4
# The number of available drivers for the day.
drivers = 30
# The number of passengers who need to be transported.
passengers = 90
# The total number of cars that cannot be driven because there aren't enough drivers.
cars_not_driven = cars - drivers
# The total number of cars that can be driven by the available drivers.
cars_driven = drivers
# The amount of seats multiplied by the driven cars.
carpool_capacity = cars_driven * space_in_a_car
# The amount of passengers divided by the amount of driven cars.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
