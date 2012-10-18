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

from contextlib import contextmanager

def set_mode(resolution=(0,0), flags=0, depth=0):
    flags |= pygame.OPENGL
    screen = pygame.display.set_mode(resolution, flags, depth)
    init_gl()
    return screen

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

def begin_draw(surface_size):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    enable2D(surface_size)

def end_draw():
    disable2D()
    pygame.display.flip()
    
def enable2D((width, height)):
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    glOrtho(0, width, height, 0, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

def disable2D():
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)
    glPopMatrix()

@contextmanager   
def scissor_box(rect):
    glEnable(GL_SCISSOR_TEST)
    glScissor(rect.left, int(glGetIntegerv(GL_VIEWPORT)[3]) - rect.bottom, rect.width, rect.height)
    yield
    glDisable(GL_SCISSOR_TEST)

@contextmanager
def subspace(rect):
    glPushMatrix()
    glTranslatef(rect.left, rect.top, 0)
    with scissor_box(rect):
        yield
    glPopMatrix()