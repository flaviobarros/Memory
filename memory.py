# By Flavio Barros
# implementation of card game - Memory

import simplegui
import random

# Global variables
numbers = []
exposed = [False]*16
state = 0  
card1 = ""
card2 = ""
turn_counter = 0 

# helper function to initialize globals
def new_game():
    
    ''' Initialize new game and set variables'''
    
    global numbers, exposed, state, turn_counter, card1, card2
    numbers = range(8) + range(8)
    random.shuffle(numbers)
    exposed = [False]*16
    turn_counter = 0
    state = 0
    card1 = ""
    card2 = ""
    frame.start()
    

     
# define event handlers
def mouseclick(pos):
    # add game state logic here
    global exposed, state, card1, card2, turn_counter
   
    card = pos[0] // 50
    
    if state == 0:
        exposed[card] = True
        card1 = card
        state = 1
        
    elif state == 1:
        
        if exposed[card] == False:
            turn_counter += 1
            exposed[card] = True
            card2 = card
            state = 2
        
    else:
        if exposed[card] == False:
            state = 1
            exposed[card] = True
            if numbers[card1] != numbers[card2]:
                exposed[card1] = False
                exposed[card2] = False
                card2 = ""
            card1 = card

                        
# cards are logically 50x100 pixels in size    
def draw(canvas):
    
    ''' Print numbers and cards '''
    
    position = 0
    for num, key in zip(numbers, exposed):
        
        if key:
            
            # Draw the numbers
            canvas.draw_text(str(num), [position,85], 100, "white")
        else:
            
            # Draw the cards
            canvas.draw_polygon([[position, 0], 
                                 [position + 50, 0], 
                                 [position + 50, 100], 
                                 [position, 100]], 
                                1, 'Yellow', 'Green')
        position += 50
    label.set_text("Turns = " + str(turn_counter))


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
