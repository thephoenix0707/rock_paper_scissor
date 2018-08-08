from random import randint

#List of choices
choices = ['rock', 'paper', 'scissor']
user_choice = ''
computer_choice = ''

#Accepting user input
user_input = raw_input('Choose from rock(r), paper(p), scissor(s): ')

#Assigning equivalent of r, p and s to user input
if user_input == 'r':
    user_choice = 'rock'
elif user_input == 'p':
    user_choice = 'paper'
elif user_input == 's':
    user_choice = 'scissor'
else:
    print 'Choose a valid option.'

#Generating a random int between 0 and 2
rand_int = randint(0, 2)

#Assigning the random int to predefined choices
if rand_int == 0:
    computer_choice = 'rock'
elif rand_int == 1:
    computer_choice = 'paper'
elif rand_int == 2:
    computer_choice = 'scissor'

#Print out user and computer choice
print 'Choices:\nYour: '+user_choice + '\nComputer: '+computer_choice


#Compare both the choices to evaluate the winner
if user_choice == computer_choice:
    print 'It\'s a draw!'
elif user_choice == 'rock' and computer_choice == 'paper':
    print 'Computer wins!'
elif user_choice == 'rock' and computer_choice == 'scissor':
    print 'User wins!'
elif user_choice == 'paper' and computer_choice == 'rock':
    print 'User wins!'
elif user_choice == 'paper' and computer_choice == 'scissor':
    print 'Computer wins!'
elif user_choice == 'scissor' and computer_choice == 'rock':
    print 'Computer wins!'
elif user_choice == 'scissor' and computer_choice == 'paper':
    print 'User wins!'
else:
    print 'Something went wrong, Try again!'
