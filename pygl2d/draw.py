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

def line(point1, point2, color, width=1, aa=True, alpha=255.0):
    glLineWidth(width)
    if aa:
        glEnable(GL_LINE_SMOOTH)
    glDisable(GL_TEXTURE_2D)
    glColor4f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0, alpha / 255.0)
    glBegin(GL_LINE_STRIP)
    glVertex3f(point1[0], point1[1], 0)
    glVertex3f(point2[0], point2[1], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glEnable(GL_TEXTURE_2D)
    
def lines(points, color, width=1, aa=True, closed=0, alpha=255.0):
    glLineWidth(width)
    if aa:
        glEnable(GL_LINE_SMOOTH)
    glDisable(GL_TEXTURE_2D)
    glBegin(GL_LINE_STRIP)
    glColor4f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0, alpha / 255.0)
    points = flip_points(points)
    for p in points:
        glVertex3f(p[0], p[1], 0)
    if closed:
        glVertex3f(points[0][0], points[0][1], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glDisable(GL_LINE_SMOOTH)
    glEnable(GL_TEXTURE_2D)
    
def point(point, color, size=1.0, alpha=255.0):
    glPointSize(size)
    glDisable(GL_TEXTURE_2D)
    glBegin(GL_POINTS)
    glColor4f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0, alpha / 255.0)
    glVertex3f(point[0], point[1], 0)
    glEnd()
    glEnable(GL_TEXTURE_2D)
    
def points(points, color, size=1.0, alpha=255.0):
    glPointSize(size)
    glDisable(GL_TEXTURE_2D)
    glColor4f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0, alpha / 255.0)
    glEnableClientState(GL_VERTEX_ARRAY)
    glVertexPointer(2, GL_FLOAT, 0, points)
    glDrawElementsui(GL_POINTS, range(len(points)))
    glDisableClientState(GL_VERTEX_ARRAY)
    glEnable(GL_TEXTURE_2D)

def polygon(points, color, aa=True, alpha=255.0):
    glDisable(GL_TEXTURE_2D)
    if aa:
        glEnable(GL_POLYGON_SMOOTH)
    glBegin(GL_POLYGON)
    glColor4f(color[0] / 255.0, color[1] / 255.0, color[2] / 255.0, alpha / 255.0)
    points = flip_points(points)
    for p in points:
        glVertex3f(p[0], p[1], 0)
    glEnd()
    glColor3f(1.0, 1.0, 1.0)
    glDisable(GL_POLYGON_SMOOTH)
    glEnable(GL_TEXTURE_2D)

def rect(rectstyle, color, width=0, alpha=255.0):
    x, y, w, h = rectstyle
    points = [[x, y], [x + w, y], [x + w, y + h], [x, y + h]]
    points = flip_points(points)
    if not width:
        polygon(points, color, aa=False, alpha=alpha)
    else:
        lines(points, color, width=width, aa=False, alpha=alpha, closed=1)

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
