"""
author: Tarkan
date: 05/21/2024
Pygame development (goated)
"""


# Weirdly reminds me of web development with onclick functions and addEvenListeners('click', function(){}) lol 

import time
import pgzrun

alien = Actor('alien') # type: ignore
alien.pos = 100, 56

WIDTH = 500
HEIGHT = alien.height + 20

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0
        
"""
const button = document.getElementById("btn");

button.addEventListener('click', function() {
    console.log('Eek!');  
})
"""

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt() 

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)
    
def set_alien_normal():
    alien.image = 'alien'

def draw():
    screen.clear() # type: ignore
    alien.draw()
pgzrun.go()  # Must be the last line of code