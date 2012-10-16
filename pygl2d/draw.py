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

import numpy

from OpenGL.GL import *
from OpenGL.GLU import *

def flip_points(points):
    lowest = 0
    highest = 0
    for p in points:
        if p[1] <= lowest:
            lowest = p[1]
        elif p[1] >= highest:
            highest = p[1]
    height = highest - lowest
    new = []
    for p in points:
        new.append([p[0], (highest + p[1]) - height])
    return new

def line(surface_size, point1, point2, color, width=1, aa=True, alpha=255.0):
    glLineWidth(width)
    if aa:
        glEnable(GL_LINE_SMOOTH)
    glDisable(GL_TEXTURE_2D)
    glColor4f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0, alpha / 255.0)
    glBegin(GL_LINE_STRIP)
    offset = surface_size[1]
    glVertex3f(point1[0], offset - point1[1], 0)
    glVertex3f(point2[0], offset - point2[1], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glEnable(GL_TEXTURE_2D)
    
def lines(surface_size, points, color, width=1, aa=True, closed=0, alpha=255.0):
    glLineWidth(width)
    if aa:
        glEnable(GL_LINE_SMOOTH)
    glDisable(GL_TEXTURE_2D)
    glBegin(GL_LINE_STRIP)
    glColor4f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0, alpha / 255.0)
    offset = surface_size[1]
    points = flip_points(points)
    for p in points:
        glVertex3f(p[0], offset - p[1], 0)
    if closed:
        glVertex3f(points[0][0], offset - points[0][1], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glDisable(GL_LINE_SMOOTH)
    glEnable(GL_TEXTURE_2D)
    
def point(surface_size, point, color, size=1.0, alpha=255.0):
    glDisable(GL_TEXTURE_2D)
    offset = surface_size[1]
    glPointSize(size)
    glBegin(GL_POINTS);
    glColor4f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0, alpha / 255.0)
    glVertex3f(point[0], offset - point[1], 0)
    glEnd()
    glEnable(GL_TEXTURE_2D)
    
def points(surface_size, points, color, size=1.0, alpha=255.0):
    glDisable(GL_TEXTURE_2D)
    offset = surface_size[1]
    points = numpy.array(zip(*points))
    points[1] = offset - points[1]
    points = zip(*points)
    glPointSize(size)
    glColor4f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0, alpha / 255.0)
    glEnableClientState(GL_VERTEX_ARRAY);
    glVertexPointer(2, GL_FLOAT, 0, points)
    glDrawElementsui(GL_POINTS, numpy.arange(len(points), dtype="i"))
    glEnable(GL_TEXTURE_2D)

def polygon(surface_size, points, color, aa=True, alpha=255.0):
    glDisable(GL_TEXTURE_2D)
    if aa:
        glEnable(GL_POLYGON_SMOOTH)
    glBegin(GL_POLYGON)
    glColor4f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0, alpha / 255.0)
    offset = surface_size[1]
    points = flip_points(points)
    for p in points:
        glVertex3f(p[0], offset - p[1], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glDisable(GL_POLYGON_SMOOTH)
    glEnable(GL_TEXTURE_2D)

def rect(surface_size, rectstyle, color, width=0, alpha=255.0):
    x, y, w, h = rectstyle
    points = [[x, y], [x + w, y], [x + w, y + h], [x, y + h]]
    points = flip_points(points)
    if not width:
        polygon(surface_size, points, color, aa=False, alpha=alpha)
    else:
        lines(surface_size, points, color, width=width, aa=False, alpha=alpha, closed=1)

def circle(pos, radius, color, alpha=255.0):
    w, x, y = color
    w = w / 255.0 if w else 0
    x = x / 255.0 if x else 0
    y = y / 255.0 if y else 0
    z = alpha / 255.0 if alpha else 0
    glDisable(GL_TEXTURE_2D)
    c = gluNewQuadric()
    glColor4f(w, x, y, z)
    glPushMatrix()
    glTranslatef(pos[0], pos[1], 0)
    gluDisk(c, 0, radius, 100, 100)
    glPopMatrix()
    glEnable(GL_TEXTURE_2D)
