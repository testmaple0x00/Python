def name_to_number(name):
    if name == "rock":
        return 0
    elif name == "Spock":
        return 1
    elif name == "paper":
        return 2
    elif name == "lizard":
        return 3
    elif name == "scissors":
        return 4
def number_to_name(number):
    if number == 0:
        return "rock"
    elif number == 1:
        return "Spock"
    elif number == 2:
        return "paper"
    elif number == 3:
        return "lizard"
    elif number == 4:
        return "scissors"
import random
def rpsls(player_choice): 
    print ""
    print "Player chooses "+player_choice
    player_choice_number=name_to_number(player_choice)
    computer_choice_number=random.randrange(0,5)
    print "Computer chooses "+number_to_name(computer_choice_number)
    status=(player_choice_number-computer_choice_number)%5
    if status==1 or status==2:
        print "Player wins!"
    elif status==3 or status==4:
        print "Computer wins!"
    else:
        print "Player and computer tie!"
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
