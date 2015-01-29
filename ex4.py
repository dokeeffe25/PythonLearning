# initialise number of cars, space_in_a_car, drivers, passengers
# cars_not_driven, cars_driven
cars = 100
space_in_a_car = 4
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers

#calculate carpool_capacity using cars_driven and space_in_a_car
carpool_capacity = cars_driven * space_in_a_car
#calculate average passengers needed to be in a car by dividing the number
#of passengers by the number of cars driven.
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today"
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
