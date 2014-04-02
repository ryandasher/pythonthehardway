# Define our function and print some strings.
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes of crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"
    
# Print a string and then call our function.
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

# Print a string, then set some variables.
print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

# Run our function with the previous variables.
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Print a string and call our function with some operators for arguments.
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

# Print a string and call our function using variables and operators.
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers +1000)

# Study drill 3:

def best_game_ever(best_game):
    print "What is the best game ever?"
    print "%s" % best_game
    
best_game_ever("Grand Theft Auto")