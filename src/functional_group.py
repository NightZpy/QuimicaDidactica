'''
Created on 06/07/2012

@author: nightzpy
'''
from config import COTIDIAN_PAIRS, LTR, RTR, LBR, RBR, PNG_EXT
from pygame.rect import Rect
from random import randint, randrange
import config
from option import Option

class Functional_Group:
    '''
    classdocs
    '''

    def __init__(self):
        self.rect_grid = { 
                             LTR: Rect(19, 230, 157 - 19, 390 - 230),
                             RTR: Rect(167, 230, 442 - 167, 390 - 230),
                             LBR: Rect(19, 400, 157 - 19, 573 - 400),
                             RBR: Rect(167, 400, 442 - 167, 573 - 400)
                          }
        self.load_complete = False
        self.is_complete = False
        self.functions = {}
        self.types = {}
        self.current_type = {}
        self.current_type_key = ''
        self.current_function = {}
        self.current_function_key = ''
        self.options_types = {}
        self.options_functions = {}
        
        self.load_functions()
        self.load_types()
        self.generate_table()
           
    def generate_table(self):
        function = randrange(1, COTIDIAN_PAIRS)
        ctype = function
        while ctype == function:
            ctype = randrange(1, COTIDIAN_PAIRS)
        
        #print "Current function: ",str(function)
        #print "Current type: ",str(ctype)
        
        #print "Rando: "+str((function, ctype))
        
        self.current_function_key = str(function)
        self.current_function = self.functions[str(function)]
        self.current_function.rect.center = self.rect_grid[LTR].center       
        
        self.current_type_key = str(ctype)
        self.current_type = self.types[str(ctype)]
        self.current_type.rect.center = self.rect_grid[RBR].center     
        
        opt_function = function
        while opt_function == function or opt_function == ctype:
            opt_function = randrange(1, COTIDIAN_PAIRS)
            
        opt_type = ctype
        while opt_type == ctype or opt_type == opt_function or opt_type == function:
            opt_type = randrange(1, COTIDIAN_PAIRS)       
                        
        self.options_functions[str(opt_function)] = self.functions[str(opt_function)]
        self.options_types[str(opt_type)] = self.types[str(opt_type)]
        self.options_functions[str(ctype)] = self.functions[str(ctype)]
        self.options_types[str(function)] = self.types[str(function)]
        self.load_complete = True
        
        #print "Opt function: ",str(self.options_functions.keys())
        #print "Opt type: ",str(self.options_types.keys())          
        
        #=======================================================================
        # for key, option in self.options_functions.iteritems():
        #    self.options_functions[key] = option
        #    
        # for key, option in self.options_types.iteritems():
        #    self.options_types[key] = option        
        #=======================================================================
        
        self.options_functions[str(opt_function)].firts_pos(config.c_opt_pos)
        
        x = config.c_opt_pos[0]
        y = self.options_functions[str(opt_function)].rect.bottom
        self.options_types[str(opt_type)].firts_pos((x, y))
        
        y = self.options_types[str(opt_type)].rect.bottom
        self.options_functions[str(ctype)].firts_pos((x, y))
        
        y = self.options_functions[str(ctype)].rect.bottom
        self.options_types[str(function)].firts_pos((x, y))   
        
        #print "Nro Functions: ", str(len(self.options_functions))
        #print "Nro Types: ", str(len(self.options_types))               
        
    def load_functions(self):
        for i in range(1, COTIDIAN_PAIRS+1):
            option = Option(config.coditidian_functions+str(i)+PNG_EXT)
            self.functions[str(i)] = option 
        #print "Functions: "+str(self.functions.keys())  

    def load_types(self):
        for i in range(1, COTIDIAN_PAIRS+1):
            option = Option(config.coditidian_types+str(i)+PNG_EXT)
            self.types[str(i)] = option
        #print "Types: "+str(self.types.keys()) 
            
    def check_complete(self):
        if len(self.options_functions) > 0 and len(self.options_types) > 0:
            c_corrects = 0
            if self.load_complete:
                for functions in self.options_functions.itervalues():
                    if functions.is_correct: c_corrects += 1
                
                for types in self.options_types.itervalues():
                    if types.is_correct: c_corrects += 1
                    
            if c_corrects == 2: 
                self.is_complete = True
                            
        return self.is_complete

    def draw(self, screen):
        screen.blit(self.current_function.img, self.current_function.rect)
        screen.blit(self.current_type.img, self.current_type.rect)
        
        for option in self.options_functions.itervalues():
            option.draw(screen)
            
        for option in self.options_types.itervalues():
            option.draw(screen)
        
            
            
            
            