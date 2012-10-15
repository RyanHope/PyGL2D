#! /usr/bin/env python

#import pygame
import pygame
from pygame.locals import *

#import pygl2d and math
import sys; sys.path.insert(0, "..")
import pygl2d

from math import *

#Class for the lil' dude that looks like me
class Player(object):
    
    def __init__(self):
        self.angle = 0
        self.alpha = 255.0
        self.scale = 0.75
        self.image = pygl2d.image.Image("mike.png")
        self.rect = self.image.get_rect()
        self.rect.topleft = [100, 100]

    def draw(self):
        self.image.rotate(self.angle)
        self.image.colorize(255.0, 255.0, 255.0, self.alpha)
        self.image.scale(self.scale)
        self.image.draw(self.rect.topleft)

def main():
    
    #init pygl2d
    pygl2d.window.init([640, 480])
    
    #create starting objects
    clock = pygame.time.Clock()
    player = Player()
    
    #Create some text
    font = pygame.font.SysFont("Courier New", 32, bold=True)
    fps_display = pygl2d.font.RenderText("", [0, 0, 0], font)
    roto_text = pygl2d.font.RenderText("Rotated Text!", [255, 0, 255], font)
    roto_text.rotate(45)
    roto_text.scale(2.0)
    roto_text.colorize(255, 255, 255, 150)
    
    #Create a Rect for drawing
    rect = pygl2d.rect.Rect(20, 320, 132, 132)
    rect_speed = 50
    
    #Create some polygon lists
    poly1 = [[320, 240], [320-40, 320], [320+40, 280]]
    poly2 = [[400, 200], [300, 300], [450, 350], [420, 300]]
    
    while 1:
        
        #Tick the clock.
        dt = clock.tick(1000.0) / 1000.0
        
        #Always use change_text to, well, change text ;-)
        fps_display.change_text(str(int(clock.get_fps())) + " fps")
        
        #get input
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                return
            if e.type == KEYDOWN:
                if e.key == K_ESCAPE:
                    pygame.quit()
                    return
                
        #move the player
        key = pygame.key.get_pressed()
        if key[K_LEFT]:
            player.angle += 150 * dt
        if key[K_RIGHT]:
            player.angle -= 150 * dt
        if key[K_UP]:
            player.rect.x += -sin(radians(player.angle))*150.0 * dt
            player.rect.y += -cos(radians(player.angle))*150.0 * dt
        if key[K_DOWN]:
            player.rect.x += sin(radians(player.angle))*150.0 * dt
            player.rect.y += cos(radians(player.angle))*150.0 * dt
        
        #######################
        #### BEGIN DRAWING ####
        #######################
        pygl2d.window.begin_draw()
       
        #fill the background with a white rect
        pygl2d.draw.rect([0, 0, 640, 480], [255, 255, 255])
        
        ######################
        #### LINE DRAWING ####
        ######################
        
        #Draw a line
        pygl2d.draw.line([0, 0], [640, 240], [0, 255, 0], 14)
        
        #Draw some lists of lines
        pygl2d.draw.lines(poly1, [255, 0, 255], width=3, closed=1)
        pygl2d.draw.lines(poly2, [0, 0, 100], width=3, closed=1)

        ######################
        #### RECT DRAWING ####
        ######################
       
        #check for a rect collision, and change the color if there is one
        color = [0, 0, 255]
        if rect.colliderect(player.rect):
            color = [255, 0, 0]
            
        #move the rect
        rect.move_ip(0, rect_speed * dt)
        if rect.top <= 0:
            rect_speed = 50
        if rect.bottom >= 480:
            rect_speed = -50
            
        #draw the rect
        pygl2d.draw.rect(rect, color, width=4)
        
        #########################
        #### DRAW THE PLAYER ####
        #########################
        
        #call the player's draw function
        player.draw()
        
        ###############################
        #### DRAW AN ALPHA POLYGON ####
        ###############################
        pygl2d.draw.polygon([[320, 0], [250, 140], [390, 140]], [255, 200, 0], alpha=200)
        
        #####################
        #### RENDER TEXT ####
        #####################
        fps_display.draw([10, 10])
        roto_text.draw([190, 200])
        
        #####################
        #### END DRAWING ####
        #####################
        pygl2d.window.end_draw()

#run if executed
if __name__ == "__main__":
    main()
