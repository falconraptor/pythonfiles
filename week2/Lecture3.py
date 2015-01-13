#print abs(-5)
print 'Please think of a number between 0 and 100!'
low=0
high=100
guess=(low+high)/2
while True:
    print 'Is your secret number '+str(guess)+"?"
    answer=str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly."))
    if answer=='h':
        high=guess
    elif answer=='l':
        low=guess
    elif answer=='c':
        break
    else:
        print "Sorry, I did not understand your input."
    guess=(low+high)/2
print "Game over. Your secret number was: "+str(guess)