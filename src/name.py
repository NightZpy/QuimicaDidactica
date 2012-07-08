'''
Created on 06/07/2012

@author: nightzpy
'''
from config import COTIDIAN_PAIRS, LTR, RTR, LBR, RBR, PNG_EXT, TEXT_FIELD,\
    NAME_PAIRS, NUMBER_NAME_OPTIONS
from pygame.rect import Rect
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
        self.exercises = {}
        self.names = {}
        self.current_exercise = {}
        self.current_exercise_key = ''
        self.options_names = {}
        
        self.load_names()
        self.load_exercises()
        self.generate_table()
           
    def generate_table(self):
        exercise = randint(1, NAME_PAIRS)        
        
        self.current_exercise_key = str(exercise)
        self.current_exercise = self.exercises[self.current_exercise_key]
        self.current_exercise.rect.center = config.name_exercise_pos     
        
        print "Exercise: "+str(exercise)
        self.options_names[str(exercise)] = self.names[str(exercise)]
        
        
        for i in range(1, NUMBER_NAME_OPTIONS + 1):
            name = exercise
            while name == exercise:
                name = randint(1, NAME_PAIRS)                
            self.options_names[str(name)] = self.names[str(name)]
            
        x = config.name_opt_pos[0]
        previous = ''
        first = False
        for option in self.options_names.itervalues():            
            if not first:                 
                option.firts_pos(config.name_opt_pos)
                first = True
                previous = option
            else:
                y = previous.rect.bottom + 10  
                option.firts_pos((x, y))
                previous = option         
        
        
        '''
        print "Names: "+str(self.options_names.keys())
        all_opt = []   
        x = config.name_opt_pos[0]
        for i in range(1, NUMBER_NAME_OPTIONS + 1):
            current_opt = str(randint(1, NAME_PAIRS))
            
            print "Current: "+current_opt             
            while self.options_names.has_key(current_opt) == False: 
                #print "antes bucles"
                current_opt = randint(1, NAME_PAIRS)
            print "Names has key: "+str(self.options_names.has_key(current_opt))
            
            all_opt.append(current_opt)
            if i == 1:                 
                self.options_names[current_opt].firts_pos(config.name_opt_pos)
            else:
                last = len(all_opt) - 1
                y = self.options_names[str(all_opt[last])].rect.bottom + 10  
                self.options_names[str(current_opt)].firts_pos((x, y)) 
        '''
        
    def load_exercises(self):
        for i in range(1, NAME_PAIRS+1):
            option = Option(config.name_exercises+str(i)+PNG_EXT, config.name_exercise_size)
            self.exercises[str(i)] = option   

    def load_names(self):
        for i in range(1, NAME_PAIRS+1):
            option = Option(config.name_names+str(i)+PNG_EXT, config.name_opt_size)
            self.names[str(i)] = option 
            
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
        
            
            
            
            