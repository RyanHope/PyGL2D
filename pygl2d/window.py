#===============================================================================
# This file is part of PyGL2D.
# Copyright (C) 2008 PyMike <pymike93@gmail.com>
# Copyright (C) 2012 Ryan Hope <rmh3093@gmail.com>
#
# PyGL2D is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyGL2D is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyGL2D.  If not, see <http://www.gnu.org/licenses/>.
#===============================================================================

import sys, os

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame
from pygame.locals import *

SCREEN_SIZE = [800, 600]

def init(size, caption="PyGL2D App", flags=DOUBLEBUF):
    """Initialise pygame and pyopengl <- return None
    """
    
    global SCREEN_SIZE
    SCREEN_SIZE = size
    
    flags |= OPENGL
    
    os.environ["SDL_VIDEO_CENTERED"] = "1"
    pygame.init()
    
    pygame.display.set_caption(caption)
    screen = pygame.display.set_mode(SCREEN_SIZE, flags)
    
    init_gl()

def begin_draw():
    """Begin drawing <- return None
    """
    
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    enable2D((0, SCREEN_SIZE[0], 0, SCREEN_SIZE[1]))

def end_draw():
    """End drawing <- return None
    """
    
    disable2D()
    pygame.display.flip()

def get_size():
    """Get the size of the window <- return tuple
    """
    
    return pygame.display.get_surface().get_size()


######################################################
###################### INTERNAL ######################
######################################################

def init_gl():
    glEnable(GL_BLEND)
    glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)
    glTexEnvi(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_MODULATE)
    glEnable(GL_TEXTURE_2D)
    glShadeModel(GL_SMOOTH)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    glClearDepth(1.0)
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_ALPHA_TEST)
    glDepthFunc(GL_LEQUAL)
    glHint(GL_PERSPECTIVE_CORRECTION_HINT, GL_NICEST)
    glAlphaFunc(GL_NOTEQUAL, 0.0)
    
def enable2D(rect):
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(rect[0], rect[0] + rect[1], rect[2], rect[2] + rect[3], -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

def disable2D():
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()
