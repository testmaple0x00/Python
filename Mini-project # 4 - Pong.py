# Implementation of classic arcade game Pong

import simplegui
import random

# initialize globals - pos and vel encode vertical info for paddles
WIDTH,HEIGHT = 600,400
BALL_RADIUS = 20
PAD_WIDTH,PAD_HEIGHT = 8,80
HALF_PAD_WIDTH,HALF_PAD_HEIGHT=PAD_WIDTH/2,PAD_HEIGHT/2
LEFT,RIGHT=False,True
paddle1_vel, paddle2_vel=0,0
score1,score2=0,0
paddle1_pos,paddle2_pos=HEIGHT/2,HEIGHT/2
ball_pos = [WIDTH / 2, HEIGHT / 2]
ball_vel = [0,0]
key_w,key_s,key_up,key_down=False,False,False,False
# initialize ball_pos and ball_vel for new bal in middle of table
# if direction is RIGHT, the ball's velocity is upper right, else upper left
def spawn_ball(direction):
    global ball_pos, ball_vel # these are vectors stored as lists
    ball_pos=[WIDTH / 2, HEIGHT / 2]
    ball_vel= [direction*random.randrange(120,240)/60,-random.randrange(60,180)/60]
# define event handlers
def new_game():
    global paddle1_pos, paddle2_pos, paddle1_vel, paddle2_vel  # these are numbers
    global score1, score2,LEFT,RIGHT
    score1,score2=0,0
    paddle1_pos,paddle2_pos=HEIGHT/2,HEIGHT/2
    paddle1_vel,paddle2_vel=0,0
    LEFT,RIGHT=False,True
    if LEFT:
        x=-1
    elif RIGHT:
        x=1
    spawn_ball(x)
def draw(canvas):
    global score1, score2, paddle1_pos, paddle2_pos, ball_pos, ball_vel,paddle1_vel,paddle2_vel
    # draw mid line and gutters
    hitL=False
    hitR=False
    canvas.draw_line([WIDTH / 2, 0],[WIDTH / 2, HEIGHT], 1, "White")
    canvas.draw_line([PAD_WIDTH, 0],[PAD_WIDTH, HEIGHT], 1, "White")
    canvas.draw_line([WIDTH - PAD_WIDTH, 0],[WIDTH - PAD_WIDTH, HEIGHT], 1, "White")
    # update ball
    ball_pos[0] += ball_vel[0]
    ball_pos[1] += ball_vel[1]
    
    # collide and reflect off of left hand side of canvas
    if ball_pos[0] <= BALL_RADIUS+PAD_WIDTH:
        ball_vel[0] = - ball_vel[0]
        hitL=True
        ball_vel[0]*=1.1
        ball_vel[1]*=1.1
    if ball_pos[0] >= WIDTH-BALL_RADIUS-PAD_WIDTH-1:
        ball_vel[0] = - ball_vel[0]
        hitR=True
        ball_vel[0]*=1.1
        ball_vel[1]*=1.1
    if ball_pos[1] <= BALL_RADIUS:
        ball_vel[1] = - ball_vel[1]
    if ball_pos[1] >= HEIGHT-BALL_RADIUS-1:
        ball_vel[1] = - ball_vel[1]       
    # draw ball
    canvas.draw_circle(ball_pos, BALL_RADIUS, 2, "White", "Yellow")
    # update paddle's vertical position, keep paddle on the screen
    paddle1_pos+=paddle1_vel
    paddle2_pos+=paddle2_vel
    if paddle1_pos<=HALF_PAD_HEIGHT:
        paddle1_pos=HALF_PAD_HEIGHT
        paddle1_vel=0
    elif paddle1_pos>HEIGHT-HALF_PAD_HEIGHT:
        paddle1_pos=HEIGHT-HALF_PAD_HEIGHT
        paddle1_vel=0
    if paddle2_pos<=HALF_PAD_HEIGHT:
        paddle2_pos=HALF_PAD_HEIGHT
        paddle2_vel=0
    elif paddle2_pos>HEIGHT-HALF_PAD_HEIGHT:
        paddle2_pos=HEIGHT-HALF_PAD_HEIGHT
        paddle2_vel=0
    # draw paddles
    canvas.draw_polygon([[0, paddle1_pos-HALF_PAD_HEIGHT], [PAD_WIDTH, paddle1_pos-HALF_PAD_HEIGHT],[PAD_WIDTH, paddle1_pos+HALF_PAD_HEIGHT],[0, paddle1_pos+HALF_PAD_HEIGHT]], 1, 'Blue', 'White')
    canvas.draw_polygon([[WIDTH-PAD_WIDTH, paddle2_pos-HALF_PAD_HEIGHT], [WIDTH, paddle2_pos-HALF_PAD_HEIGHT],[WIDTH, paddle2_pos+HALF_PAD_HEIGHT],[WIDTH-PAD_WIDTH, paddle2_pos+HALF_PAD_HEIGHT]], 1, 'Blue', 'White')
    # determine whether paddle and ball collide
    if hitL==True:
        if abs(ball_pos[1]-paddle1_pos)>HALF_PAD_HEIGHT:
            score2+=1
            spawn_ball(1)
    if hitR==True:
        if abs(ball_pos[1]-paddle2_pos)>HALF_PAD_HEIGHT:
            score1+=1
            spawn_ball(-1)
    # draw scores
    canvas.draw_text(str(score1), (WIDTH/4-15, 100), 50, 'White')
    canvas.draw_text(str(score2), (WIDTH/4*3-15, 100), 50, 'White')
    canvas.draw_text('1P', (WIDTH/4-15, 50), 50, 'Purple')
    canvas.draw_text('2P', (WIDTH/4*3-15, 50), 50, 'Purple')   
def keydown(key):
    global paddle1_vel, paddle2_vel,key_w,key_s,key_up,key_down
    vel=4
    if key == simplegui.KEY_MAP["down"]:
        key_down=True
        paddle2_vel = vel
    elif key == simplegui.KEY_MAP["up"]:
        key_up=True
        paddle2_vel = -vel
    if key == simplegui.KEY_MAP["s"]:
        key_s=True
        paddle1_vel = vel
    elif key == simplegui.KEY_MAP["w"]:
        key_w=True
        paddle1_vel = -vel
def keyup(key):
    global paddle1_vel, paddle2_vel,key_w,key_s,key_up,key_down
    vel=4
    if key == simplegui.KEY_MAP["down"]:
        key_down=False
        if key_up:
            paddle2_vel= -vel
        else:
            paddle2_vel = 0
    elif key == simplegui.KEY_MAP["up"]:
        key_up=False
        paddle2_vel = 0
        if key_down:
            paddle2_vel= vel
        else:
            paddle2_vel = 0
    if key == simplegui.KEY_MAP["s"]:
        key_s=False
        if key_w:
            paddle1_vel= -vel
        else:
            paddle1_vel = 0
    elif key == simplegui.KEY_MAP["w"]:
        key_w=False
        if key_s:
            paddle1_vel= vel
        else:
            paddle1_vel = 0
def restart():
    new_game()
# create frame
frame = simplegui.create_frame("Pong", WIDTH, HEIGHT)
frame.set_draw_handler(draw)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.add_button("Restart", restart, 100)
frame.add_label('control', 200)
frame.add_label('1P: W/S', 300)
frame.add_label('2P: UP/DOWN', 300)

# start frame
new_game()
frame.start()
