'''
Created on 06/07/2012

@author: nightzpy
'''
from config import PNG_EXT, TEXT_FIELD, MATCH_PAIRS
from random import randint
import config
from option import Option
from graphics import load_image, resize
from pygame.rect import Rect
from page import Page
from glob import glob

ALIFATICOS = '2'
ALCANOS  = '3'
ALQUENOS = '4'
ALQUINOS = '5'
CICLICOS = '6'
AROMATICOS = '7'
ALCOHOLES = '8'
FENOLES = '9'
ALDEHIDOS = '10'
CETONAS = '11'
ETERES = '12'
ACIDOS = '13'
AMINAS = '14'
AMIDAS = '16'
NITRILOS = '17'

class Definitions:
    '''
    classdocs
    '''

    def __init__(self):    
        self.rect_options = {}   
        self.options = {} 
        self.load_options()
        self.current_page = ''
        self.list_current_pages = []
        self.pages_listed = False

           
    def generate_table(self):
        pass  
        
    def load_options(self):
        self.rect_options = {
                     ALIFATICOS: Rect((132, 370), (246-132, 398-370)),
                     ALCANOS: Rect((70, 449), (133-70, 475-449)),
                     ALQUENOS: Rect((142, 449), (217-142, 475-449)),
                     ALQUINOS: Rect((225, 449), (298-225, 475-449)),
                     CICLICOS: Rect((140, 540), (298-225, 475-449)),
                     AROMATICOS: Rect((210, 370), (246-132, 398-370)),
                     ALCOHOLES: Rect((345, 349), (490-345, 376-349)),
                     FENOLES: Rect((345, 382), (490-345, 376-349)),
                     ALDEHIDOS: Rect((345, 414), (490-345, 376-349)),
                     CETONAS: Rect((345, 446), (490-345, 376-349)),
                     ETERES: Rect((345, 480), (490-345, 376-349)),
                     ACIDOS: Rect((345, 512), (490-345, 376-349)),
                     AMINAS: Rect((511, 363), (597-511, 390-363)),
                     AMIDAS: Rect((626, 362), (597-511, 390-363)),
                     NITRILOS: Rect((567, 413), (597-511, 390-363))
                     }
        for key, rect in self.rect_options.iteritems():
            self.options[key] = Option()
            self.options[key].set_rect(rect)

    def load_pages(self, number, director):
        n_pages = len(glob(config.definition_pages+number+'/'+'*'+PNG_EXT))
        for i in range(1, n_pages+1):
            directorie = number+'/'+str(i)
            print "Dir: "+directorie
            self.list_current_pages.append(Page(director, directorie))
        self.pages_listed = True
        
        print "Len: "+str(len(self.list_current_pages))   
        
        size = len(self.list_current_pages)
        last = len(self.list_current_pages)-1
        for i in range(size):
            if size > 1:
                if i==0:
                    self.list_current_pages[i].follow = self.list_current_pages[i+1]
                elif i==last:
                    self.list_current_pages[i].previous = self.list_current_pages[i-1]
                else:
                    self.list_current_pages[i].follow = self.list_current_pages[i+1]
                    self.list_current_pages[i].previous = self.list_current_pages[0]
                self.list_current_pages[i].check_buttoms()
             
        self.current_page = self.list_current_pages[0]
            
    def check_complete(self):
        if len(self.functions) > 0 and len(self.elements) > 0: 
            c_corrects = 0
            for function in self.functions.itervalues():
                if function.is_correct: c_corrects += 1
                if c_corrects == MATCH_PAIRS: 
                    self.is_complete = True
                    break
            
        return self.is_complete

    def draw(self, screen):
        for function in self.functions.itervalues():
            function.draw(screen)   

        
            
            
            
            