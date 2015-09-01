# Mini-project #6 - Blackjack

import simplegui
import random

# load card sprite - 936x384 - source: jfitz.com
CARD_SIZE = (72, 96)
CARD_CENTER = (36, 48)
card_images = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/cards_jfitz.png")

CARD_BACK_SIZE = (72, 96)
CARD_BACK_CENTER = (36, 48)
card_back = simplegui.load_image("http://storage.googleapis.com/codeskulptor-assets/card_jfitz_back.png")    

# initialize some useful global variables
in_play = False
outcome = ""
score = 0

# define globals for cards
SUITS = ('C', 'S', 'H', 'D')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K')
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


# define card class
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
        
# define hand class
class Hand:
    def __init__(self):
        self.cards=[]

    def __str__(self):
        # return a string representation of a hand
        cardlist=''
        for card in self.cards:
            cardlist+=str(card)+' '
        return 'Hand contains '+cardlist
    def add_card(self, card):
        self.cards.append(card)
        # add a card object to a hand

    def get_value(self):
        # count aces as 1, if the hand has an ace, then add 10 to hand value if it doesn't bust
        # compute the value of the hand, see Blackjack video
        total=0
        special=False
        for card in self.cards:
            if card.get_rank()=='A':
                special=True
            total+=VALUES[card.get_rank()]
        if total<=11 and special:
            total+=10
        return total
    def draw(self, canvas, pos):
        index=0
        newpos=[0,0]
        for card in self.cards:
            newpos[0]=pos[0]+CARD_SIZE[0]*index*1.2
            newpos[1]=pos[1]
            card.draw(canvas,newpos)
            index+=1
        
# define deck class 
class Deck:
    def __init__(self):
        self.cards=[]
        # create a Deck object
        for i in range(len(SUITS)):
            for j in range(len(RANKS)):
                self.cards.append(Card(SUITS[i],RANKS[j]))

    def shuffle(self):
        # shuffle the deck 
        random.shuffle(self.cards)

    def deal_card(self):
        # deal a card object from the deck
        return self.cards.pop()
    def __str__(self):
        # return a string representing the deck
        cardlist=''
        for card in self.cards:
            cardlist+=str(card)+' '
        return 'Deck contains '+cardlist   


#define event handlers for buttons
def deal():
    global outcome, in_play,newDeck,dealer,player,score
    if in_play:
        outcome='You give up!Lose!'
        score-=1
        in_play=False
    else:
        newDeck=Deck()
        newDeck.shuffle()
        dealer=Hand()
        player=Hand()
        player.add_card(newDeck.deal_card())
        dealer.add_card(newDeck.deal_card())
        player.add_card(newDeck.deal_card())
        dealer.add_card(newDeck.deal_card())
        outcome=''
        in_play = True

def hit():
    global outcome,in_play,score
    # replace with your code below
    
    if in_play:
        player.add_card(newDeck.deal_card())
        if player.get_value()>21:
            outcome="You went bust and lose!"
            score-=1
            in_play=False
    else:
        dealer.add_card(newDeck.deal_card())
        
    # if the hand is in play, hit the player
   
    # if busted, assign a message to outcome, update in_play and score
       
def stand():
    global outcome,in_play,score
    in_play=False
    if not in_play:
        while dealer.get_value()<17:
            hit()
        if dealer.get_value()>21:
            outcome="Dealer went bust!You win!"
            score+=1 
        elif player.get_value()>dealer.get_value():
            outcome='You win!'
            score+=1
        else:
            outcome='You lose!'
            score-=1

# draw handler    
def draw(canvas):
    global dealer,player,score,outcome
    # test to make sure that card.draw works, replace with your code below
    canvas.draw_text('Blackjack', (50, 100), 50, 'Aqua')
    canvas.draw_text('Score '+str(score), (300, 100), 35, 'Black')
    canvas.draw_text('Dealer        '+outcome, (80, 180), 30, 'Black')
    dealer.draw(canvas,[100,200])
    player.draw(canvas,[100,400])
    if in_play:
        canvas.draw_text('Player        Hit or stand?', (80, 380), 30, 'Black')
        canvas.draw_image(card_back, CARD_BACK_CENTER, CARD_BACK_SIZE, [100+CARD_BACK_CENTER[0],200+CARD_BACK_CENTER[1]], CARD_BACK_SIZE)
    else:
        canvas.draw_text('Player        New deal?', (80, 380), 30, 'Black')



# initialization frame
frame = simplegui.create_frame("Blackjack", 600, 600)
frame.set_canvas_background("Green")

#create buttons and canvas callback
frame.add_button("Deal", deal, 200)
frame.add_button("Hit",  hit, 200)
frame.add_button("Stand", stand, 200)
frame.set_draw_handler(draw)


# get things rolling
deal()
frame.start()


# remember to review the gradic rubric