#! /usr/bin/env python

#Please send me the results of this speed test on the
#googlecode wiki page: http://code.google.com/p/pygl2d/wiki/SpeedTests

import os
import pygame
from pygame.locals import *

#import pygl2d
import sys; sys.path.insert(0, "..")
import pygl2d

#init pygl2d
screen_size = (640, 480)
os.environ['SDL_VIDEO_WINDOW_POS'] = 'center'
pygame.init()
pygame.display.set_mode(screen_size, pygame.DOUBLEBUF | pygame.OPENGL)
pygl2d.window.init_gl()

#create starting objects
clock = pygame.time.Clock()

#load image
image = pygl2d.image.Image(screen_size, "mike.png")

running = 1
while running:
    
    clock.tick(1000.0)
   
    for e in pygame.event.get():
        if e.type == QUIT:
            running = 0
        if e.type == KEYDOWN:
            if e.key == K_ESCAPE:
                running = 0
   
    print "Drawing 1000 images at",int(clock.get_fps()),"fps"
    pygl2d.window.begin_draw(screen_size)
    for i in range(1000):
        image.draw([0, 0])
    pygl2d.window.end_draw()

pygame.quit()
