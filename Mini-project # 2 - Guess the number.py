# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import simplegui
import random
import math
secret_number=9999
remain_guesses=7
game_type=100
# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    if game_type==100:
        range100()
    elif game_type==1000:
        range1000()
        
# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    print "New game. Range is from 0 to 100"
    global secret_number,remain_guesses,game_type
    game_type=100
    remain_guesses=7
    secret_number=random.randrange(0,101)
    print "Number of remaining guesses is",remain_guesses
    print 

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    print "New game. Range is from 0 to 1000"
    global secret_number,remain_guesses,game_type
    game_type=1000
    remain_guesses=10
    secret_number=random.randrange(0,1001)
    print "Number of remaining guesses is",remain_guesses
    print
    
def input_guess(guess):
    # main game logic goes here
    int_guess=int(guess)
    print "Guess was",int_guess
    global secret_number,remain_guesses
    remain_guesses-=1
    print "Number of remaining guesses is",remain_guesses
    if int_guess==secret_number:
        print "Correct!"
        print
        new_game()
    elif remain_guesses==0:
        print "You ran out of guesses.  The number was",secret_number
        print
        new_game()
    elif int_guess<secret_number:
        print "Higher!"
    elif int_guess>secret_number:
        print "Lower!" 
    print
    
# create frame
frame = simplegui.create_frame("Guess the number",200,200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100]", range100, 200)
frame.add_button("Range is [0, 1000]", range1000, 200)
frame.add_input("Enter a guess", input_guess, 100)

# call new_game 
new_game()
frame.start()
