from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# Study drill 1: If you don't pass in the required amount of arguments, you will receive an error stating that you need to pass in more arguments.

# Study drill 2:

# script, best_game, worst_game = argv
# 
# print "This is the best game I've played:", best_game
# print "This is the worst game I've played:", worst_game

# script, food, movie, book, hobby = argv
# 
# print "This is my favorite food:", food
# print "This is my favorite movie:", movie
# print "This is my favorite book:", book
# print "This is my favorite hobby:", hobby

# Study drill 3:

# script, person = argv
# 
# print "Ok, so you're %s? Tell me about yourself." % person
# print "What is your favorite programming language?",
# language = raw_input()
# print "How many years have you been programming?",
# length = raw_input()
# print "What do you want to do with programming?",
# goal = raw_input()
# 
# print """Ok, so your favorite language is %s, you've been programming for %s 
# years, and you hope to use programming to %s. That is neat.""" % (
#     language, length, goal)