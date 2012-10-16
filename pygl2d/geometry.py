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

import math

def rotate_point(point, center_point, angle):
    """Rotate a point <- return list (new point)
    """
    
    p = [point[0] - center_point[0], point[1] - center_point[1]]
    print p, center_point
    x = int(p[0] * math.cos(math.radians(-angle)) - p[1] * math.sin(math.radians(-angle)))
    y = int(p[0] * math.sin(math.radians(-angle)) + p[1] * math.cos(math.radians(-angle)))
    x += center_point[0]
    y += center_point[1]
    return [x, y]

def rotate_points(points, center_point, angle):
    """Rotate a series of points <- return points list
    """
    
    new = []
    for p in points:
        new.append(rotate_point(p, center_point, angle))
    return new

def center_of_poly(poly):
    """Get the center of a polygon <- return tuple
    """
    
    bx, by = 0, 0
    sx, sy = 0, 0
    for p in poly:
        if p[0] > bx:
            bx = p[0]
        if p[0] < sx:
            sx = p[0]
        if p[1] > by:
            by = p[1]
        if p[1] < sy:
            sy = p[1]
    return ((bx - sx) / 2, (by - sy) / 2)

def line_collision(a, b):
    """Detects a collision between two lines <- return bool
    """
    
    s1 = a[0]
    s2 = b[0]
    e1 = a[1]
    e2 = b[1]
    
    a1 = e1[0] - s1[0]
    b1 = e1[1] - s1[1]
    c1 = e1[0] * s1[1] - s1[0] * e1[1]

    a2 = e2[0] - s2[0]
    b2 = e2[1] - s2[1]
    c2 = e2[0] * s2[1] - s2[0] * e2[1]
    
    denom = a1 * b2 - a2 * b1
    
    if denom <= 0.0001:
        return False
    
    numA = (e2[0] - s2[0]) * (s1[1] - s2[1]) - (e2[1] - s2[1]) * (s1[0] - s2[0])
    numB = (e1[0] - s1[0]) * (s1[1] - s2[1]) - (e1[1] - s1[1]) * (s1[0] - s2[0])
    
    result = [(a2 * c1 - a1 * c2) / denom, -(b1 * c2 - b2 * c1 / denom)]
    Ta = numA / float(denom)
    Tb = numB / float(denom)
    if (Ta >= 0 and Ta <= 1) and (Tb >= 0 and Tb <= 1):
        return result
    
    return False

def circle_collision(p1, p2, r1, r2):
    """Detects a collision between two circles <- return bool
    """
    
    if ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) <= (r1 + r2):
        return True
    return False

def poly_collision(poly1, poly2):
    """Detect a collision between two polygons <- return bool
    """
    
    collisions = []
    lines1 = []
    lines2 = []
    for n in xrange(len(poly1)):
        lines1.append([poly1[n - 1], poly1[n]])
    for n in xrange(len(poly2)):
        lines2.append([poly2[n - 1], poly2[n]])
    for l1 in lines1:
        for l2 in lines2:
            c = line_collision(l1, l2)
            if c:
                return True
                #collisions.append(c)
    return False
