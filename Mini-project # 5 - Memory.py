# implementation of card game - Memory

import simplegui
import random

# helper function to initialize globals
def new_game():
    global open,card,count,openList,label
    open=[False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
    card=[0,1,2,3,4,5,6,7,0,1,2,3,4,5,6,7]
    count=0
    openList=[]
    random.shuffle(card)
    label.set_text("Turns = "+str(count))
    
    
# define event handlers
def mouseclick(pos):
    global open,openList,card,count,label
    # add game state logic here
    find=pos[0]/50
    if not open[find]:
        if len(openList)==2:
            if card[openList[0]]!=card[openList[1]]:
                for back in openList:
                    open[back]=False
            openList=[]
        open[find]=True
        openList.append(find)
        if len(openList)==1:
            count+=1
    label.set_text("Turns = "+str(count))

    
# cards are logically 50x100 pixels in size    
def draw(canvas):
    global open
    for index in range(len(open)):
        if open[index]:
            canvas.draw_text(str(card[index]), (index*50,90), 100, 'White')
        else:
            canvas.draw_polygon([[index*50, 0], [(index+1)*50, 0], [(index+1)*50, 100], [index*50, 100]],1,'Black','Green')
            

# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")

# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()


# Always remember to review the grading rubric