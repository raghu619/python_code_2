# -*- coding: utf-8 -*-
"""
Created on Mon Aug 14 23:20:35 2017

@author: koduri Raghvendra ra
"""

import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def __sub__(self, no):
        x = self.x - no.x
        y = self.y - no.y
        z = self.z - no.z
        return Points(x, y, z)

    def dot(self, no):
        x = self.x * no.x
        y = self.y * no.y
        z = self.z * no.z
        return x + y + z

    def cross(self, no):
        x = self.y * no.z - self.z * no.y
        y = self.z * no.x - self.x * no.z
        z = self.x * no.y - self.y * no.x
        return Points(x, y, z)

    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


points = list()
for i in range(4):
    a = map(float, raw_input().split())
    points.append(a)

A, B, C, D = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
X = (B - A).cross(C - B)
Y = (C - B).cross(D - C)
angle = math.acos(X.dot(Y) / (X.absolute() * Y.absolute()))

print "%.2f" % math.degrees(angle)