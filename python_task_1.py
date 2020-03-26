# -*- coding: utf-8 -*-
"""
Created on Thur Mar 26 20:14:13 2020

@author: Bayo
"""
def cal_circle_area (radius):
    area = 3.142*(radius**2)
    return area
radius = float(input("Please enter the radius of the circle here: "))

print (cal_circle_area(radius))