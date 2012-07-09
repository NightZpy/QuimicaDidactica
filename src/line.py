'''
Created on 08/07/2012

@author: nightzpy
'''
import pygame
from config import WHITE

class Line:
    '''
    classdocs
    '''


    def __init__(self, point_init, point_end = (0, 0)):
        '''
        Constructor
        '''
        self.points = []
        self.point_init = point_init
        self.point_end = point_end
        self.color = WHITE
        self.points = [self.point_init, point_end]
        