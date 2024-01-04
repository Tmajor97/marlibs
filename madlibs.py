#string cocantenation (aka how to put string together)
#suppose we want to create a string that says "unsubsricbe to ______"
#youtuber = "oluwatobi solomon" # some string variable

# a few ways to do this
#print("subscibe to " + youtuber)
#print("subscribe to {}".format(youtuber))
#print(f"subscribe to {youtuber}")

adj = input("Adjective:")
verb1 = input("Verb1:")
verb2 = input ("verb2:")
famous_person = input("Famous person:")

madlib = f"Computer programming is so {adj}! It makes me so excicted all the time because \
I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!."

print(madlib) 
    