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

class _rect:
    def __init__(self, x, y, w, h):
        self.x = float(x)
        self.y = float(y)
        self.w = w
        self.h = h

class Rect(object):
    
    def __init__(self, x, y, w, h):
        """Create a rect object <- return None
        """
        
        self._r = _rect(x, y, w, h)
   
    def __getattr__(self, name):
        if name in ('top', 'y'):
            return self._r.y
        elif name in ('left', 'x'):
            return self._r.x
        elif name == 'bottom':
            return self._r.y + self._r.h
        elif name == 'right':
            return self._r.x + self._r.w
        elif name == 'topleft':
            return self._r.x, self._r.y
        elif name == 'bottomleft':
            return self._r.x, self._r.y + self._r.h
        elif name == 'topright':
            return self._r.x + self._r.w, self._r.y
        elif name == 'bottomright':
            return self._r.x + self._r.w, self._r.y + self._r.h
        elif name == 'midtop':
            return self._r.x + self._r.w / 2, self._r.y
        elif name == 'midleft':
            return self._r.x, self._r.y + self._r.h / 2
        elif name == 'midbottom':
            return self._r.x + self._r.w / 2, self._r.y + self._r.h
        elif name == 'midright':
            return self._r.x + self._r.w, self._r.y + self._r.h / 2
        elif name == 'center':
            return self._r.x + self._r.w / 2, self._r.y + self._r.h / 2
        elif name == 'centerx':
            return self._r.x + self._r.w / 2
        elif name == 'centery':
            return self._r.y + self._r.h / 2
        elif name == 'size':
            return self._r.w, self._r.h
        elif name == 'width' or name == "w":
            return self._r.w
        elif name == 'height' or name == "h":
            return self._r.h
        else:
            raise AttributeError, name

    def __setattr__(self, name, value):
        if name == 'top' or name == 'y':
            self._r.y = value
        elif name == 'left' or name == 'x':
            self._r.x = value
        elif name == 'bottom':
            self._r.y = value - self._r.h
        elif name == 'right':
            self._r.x = value - self._r.w
        elif name == 'topleft':
            self._r.x, self._r.y = value[0], value[1]
        elif name == 'bottomleft':
            self._r.x = value[0]
            self._r.y = value[1] - self._r.h
        elif name == 'topright':
            self._r.x = value[0] - self._r.w
            self._r.y = value[1]
        elif name == 'bottomright':
            self._r.x = value[0] - self._r.w
            self._r.y = value[1] - self._r.h
        elif name == 'midtop':
            self._r.x = value[0] - self._r.w / 2
            self._r.y = value[1]
        elif name == 'midleft':
            self._r.x = value[0]
            self._r.y = value[1] - self._r.h / 2
        elif name == 'midbottom':
            self._r.x = value[0] - self._r.w / 2
            self._r.y = value[1] - self._r.h
        elif name == 'midright':
            self._r.x = value[0] - self._r.w
            self._r.y = value[1] - self._r.h / 2
        elif name == 'center':
            self._r.x = value[0] - self._r.w / 2
            self._r.y = value[1] - self._r.h / 2
        elif name == 'centerx':
            self._r.x = value - self._r.w / 2
        elif name == 'centery':
            self._r.y = value - self._r.h / 2
        elif name == 'size':
            if value[0] < 0 or value[1] < 0:
                self._ensure_proxy()
            self._r.w, self._r.h = value
        elif name == 'width':
            if value < 0:
                self._ensure_proxy()
            self._r.w = value
        elif name == 'height':
            if value < 0:
                self._ensure_proxy()
            self._r.h = value
        elif name == "_r":
            self.__dict__["_r"] = value
        else:
            raise AttributeError, name

    def __len__(self):
        return 4

    def __getitem__(self, key):
        return (self._r.x, self._r.y, self._r.w, self._r.h)[key]

    def __setitem__(self, key, value):
        r = [self._r.x, self._r.y, self._r.w, self._r.h]
        r[key] = value
        self._r.x, self._r.y, self._r.w, self._r.h = r
        
    def move(self, dx, dy):
        """Create a new rect moved the amount of dx and dy. <- return Rect
        """
         
        return Rect(self._r.x + dx, self._r.y + dy, self._r.h, self._r.w)
        
    def move_ip(self, dx, dy):
        """Move the rect the amount of dx and dy. <- return None
        """
        
        self._r.x += dx
        self._r.y += dy
        
    def colliderect(self, rect):
        """Check for a collision between another rect. <- return bool
        """
        
        return _rect_collide(self, rect)
        
    def collidepoint(self, rect):
        """Check for a collision between the rect and a point <- return bool
        """
        
        return rect._r.x >= self._r.x and \
               rect._r.y >= self._r.y and \
               rect._r.x < self._r.x + self._r.w and \
               rect._r.y < self._r.y + self._r.h
        
def _rect_collide(a, b):
    return a.x + a.w > b.x and b.x + b.w > a.x and \
           a.y + a.h > b.y and b.y + b.h > a.y
