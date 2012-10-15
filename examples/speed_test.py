#! /usr/bin/env python

#Please send me the results of this speed test on the
#googlecode wiki page: http://code.google.com/p/pygl2d/wiki/SpeedTests

#import pygame
import pygame
from pygame.locals import *

#import pygl2d
import sys; sys.path.insert(0, "..")
import pygl2d

#init pygl2d
pygl2d.window.init([640, 480])

#create starting objects
clock = pygame.time.Clock()

#load image
image = pygl2d.image.Image("mike.png")

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
    pygl2d.window.begin_draw()
    for i in range(1000):
        image.draw([0, 0])
    pygl2d.window.end_draw()

pygame.quit()
