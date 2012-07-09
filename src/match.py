'''
Created on 06/07/2012

@author: nightzpy
'''
from config import PNG_EXT, TEXT_FIELD, MATCH_PAIRS
from random import randint
import config
from option import Option
from graphics import load_image, resize

class Match:
    '''
    classdocs
    '''

    def __init__(self):
        self.text_field_img = resize(load_image(config.name_items+TEXT_FIELD+PNG_EXT, True), config.name_text_field_size)
        self.text_field_rect = self.text_field_img.get_rect()
        self.text_field_rect.center = config.name_text_field_pos
        
        self.is_complete = False
        self.functions = {}
        self.elements = {}
        
        self.load_elements()
        self.load_functions()
        print "Elements keys: "+str(self.elements.keys())
        self.generate_table()
           
    def generate_table(self):
        all_functions = []
        for i in range(1, MATCH_PAIRS + 1):
            function = str(randint(1, MATCH_PAIRS))
            while all_functions.count(function) > 0:
                function = str(randint(1, MATCH_PAIRS))
            all_functions.append(function)
            
        all_elements = []
        for i in range(1, MATCH_PAIRS + 1):
            element = str(randint(1, MATCH_PAIRS))
            while all_elements.count(element) > 0:
                element = str(randint(1, MATCH_PAIRS))
            all_elements.append(element)

        
        x_function = config.match_function_pos[0]
        x_element = config.match_element_pos[0]
        previous = ''      
        first = True
        for i in all_functions:
            function = self.functions[i]
            if first:
                function.firts_pos(config.match_function_pos)
                first = False
            else:
                y_function = previous.rect.bottom + 10
                function.firts_pos((x_function, y_function))                
            previous = function
         
        first = True           
        for i in all_elements:
            element = self.elements[i]
            if first:
                element.firts_pos(config.match_element_pos)
                first = False
            else:
                y_element = previous.rect.bottom + 10
                element.firts_pos((x_element, y_element))                
            previous = element          
        
    def load_functions(self):
        for i in range(1, MATCH_PAIRS + 1):
            option = Option(config.match_functions+str(i)+PNG_EXT, config.match_function_size)
            self.functions[str(i)] = option   

    def load_elements(self):
        for i in range(1, MATCH_PAIRS + 1):
            option = Option(config.match_elements+str(i)+PNG_EXT, config.match_element_size)
            self.elements[str(i)] = option 
            
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
            
        for element in self.elements.itervalues():            
            element.draw(screen)
        
            
            
            
            