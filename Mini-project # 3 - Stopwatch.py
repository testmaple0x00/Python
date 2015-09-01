# template for "Stopwatch: The Game"

# define global variables
import simplegui
import random
time_count=0
time_work=False
clicks_hit=0
clicks_stop=0
# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    sec=str(t%600)
    if len(sec)==3:
        B=sec[0]
        C=sec[1]
        D=sec[2]
    elif len(sec)==2:
        B="0"
        C=sec[0]
        D=sec[1]
    else:
        B="0"
        C="0"
        D=sec[0]
    A=str(t/600)
    return A+":"+B+C+"."+D
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def Start():
    global time_work
    time_work=True
def Stop():
    global time_work,clicks_hit,clicks_stop
    if time_work:
        time_work=False
        if time_count%10==0:
            clicks_hit+=1
        clicks_stop+=1
def Reset():
    global time_work,time_count,clicks_hit,clicks_stop
    time_work=False
    time_count=0
    clicks_hit=0
    clicks_stop=0
# define event handler for timer with 0.1 sec interval
def tick():
    global time_count
    if time_work:
        time_count+=1
# define draw handler
def draw(canvas):
    canvas.draw_text(format(time_count), [50,90], 36, "White")
    score=str(clicks_hit)+"/"+str(clicks_stop)
    canvas.draw_text(score, [150,25], 25, "Green")
# Create a frame 
frame = simplegui.create_frame("Stopwatch", 200, 150)

# Register event handlers
frame.add_button("Start", Start, 100)
frame.add_button("Stop", Stop, 100)
frame.add_button("Reset", Reset, 100)
frame.set_draw_handler(draw)
timer = simplegui.create_timer(100, tick)

# Start the frame animation
frame.start()
timer.start()