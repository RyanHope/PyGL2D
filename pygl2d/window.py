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

from OpenGL.GL import *
from OpenGL.GLU import *

import pygame

def begin_draw(surface_size):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    enable2D((0, surface_size[0], 0, surface_size[1]))

def end_draw():
    disable2D()
    pygame.display.flip()

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
