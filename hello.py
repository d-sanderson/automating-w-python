# This program says hello and asks for your name

print('Hello world')
print('What is your name?') # ask for their name
myName = input() # the input function always returns a string value
print(f'it is good to meet you, {myName}')
print('The length of your name is:')
print(len(myName))
print('What is your age?')
myAge = input()
print(type(myAge))
# myAge is stroed as a string, it must be turned into an int to calculate age and
# then be turned back into a string to concat with the rest of the sentence.
print(f'you will be {str(int(myAge) + 1)} in a year')