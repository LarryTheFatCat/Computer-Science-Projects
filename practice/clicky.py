import pgzrun
import random
import os


WIDTH = 400
HEIGHT = 300

# Create an Actor with the circle image
image = Actor('circle.png', pos=(200,150))

os.environ['SDL_VIDEO_CENTERED'] = '1'

def draw():
    screen.clear()
    image.draw()
    

def on_mouse_down(pos):
    # Check if the mouse click is within the bounds of the circle
    current_pos = [] # im just doing this cuz i wanna iterate through each and append to a list
    if image.collidepoint(pos):
        # Randomize the position of the circle
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        image.pos = (x, y)
        for numbers in image.pos:
            if numbers == "":
                return None
            else:
                current_pos.append(numbers)
    for i in range(len(current_pos)):
        if current_pos[i] >= 200:
            image.pos = (x - 60, y - 40) # this was just guessing random things till it worked lol
        elif current_pos[i] <= HEIGHT and current_pos[i] <= WIDTH:
            image.pos = (x + 60, y + 40) # this kinda solved the issue lol, very garbo code but it works :shrug:
        
        
pgzrun.go()
