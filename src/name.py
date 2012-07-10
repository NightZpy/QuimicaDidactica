'''
Created on 06/07/2012

@author: nightzpy
'''
from config import PNG_EXT, TEXT_FIELD, NAME_PAIRS, NUMBER_NAME_OPTIONS
from random import randint
import config
from option import Option
from graphics import load_image, resize

class Name:
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
        self.current_exercise = {}
        self.current_exercise_key = ''
        self.options_names = {}
        
        self.load_elements()
        self.load_functions()
        self.generate_table()
           
    def generate_table(self):
        exercise = randint(1, NAME_PAIRS)        
        
        self.current_exercise_key = str(exercise)
        self.current_exercise = self.functions[self.current_exercise_key]
        self.current_exercise.rect.center = config.name_exercise_pos     
        
        #print "Exercise: "+str(exercise)
        self.options_names[str(exercise)] = self.elements[str(exercise)]
        
        
        for i in range(1, NUMBER_NAME_OPTIONS + 1):
            name = exercise
            while name == exercise:
                name = randint(1, NAME_PAIRS)                
            self.options_names[str(name)] = self.elements[str(name)]
            
        x = config.name_opt_pos[0]
        previous = ''
        first = False
        for option in self.options_names.itervalues():            
            if not first:                 
                option.firts_pos(config.name_opt_pos)
                first = True
                previous = option
            else:
                y = previous.rect.centery + 20  
                option.firts_pos((x, y))
                previous = option         
        
        
    def load_functions(self):
        for i in range(1, NAME_PAIRS+1):
            option = Option(config.name_exercises+str(i)+PNG_EXT, config.name_exercise_size)
            self.functions[str(i)] = option   

    def load_elements(self):
        for i in range(1, NAME_PAIRS+1):
            option = Option(config.name_names+str(i)+PNG_EXT, config.name_opt_size)
            self.elements[str(i)] = option 
            
    def check_complete(self):
        if len(self.options_names) > 0: 
            c_corrects = 0
            for name in self.options_names.itervalues():
                if name.is_correct: c_corrects += 1
                if c_corrects == 1: 
                    self.is_complete = True
                    break
            
        return self.is_complete

    def draw(self, screen):
        screen.blit(self.current_exercise.img, self.current_exercise.rect)
        screen.blit(self.text_field_img, self.text_field_rect)
        
        for option in self.options_names.itervalues():
            option.draw(screen)   
        
            
            
            
            