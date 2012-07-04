'''
Created on 29/06/2012

@author: nightzpy
'''
import pygame
import random

from pygame.rect import Rect
from random import random, Random, randint

from config import LTR, LBR, RBR, RTR, PNG_EXT, COTIDIAN_PAIRS, NUMBER_COTIDIAN_OPTIONS
from scene import Scene
from graphics import load_image
import config
from pygame.sprite import Sprite


'''

Idea general del algoritmo:

Un arreglo de 4 posiciones.
cada espacio representa un cuadro de la cuadricula del juego.
se generara un algoritmo aleatorio donde la cuadricula escojida 
sera en la que se mostrara la imagen:
    -Si el espacio es de Grupo Funcional (columna 0):
        -Se se agrega una imagen (Seleccionada aleatoriamente) de grupo funcional al espacio correspondiente y su tipo al espacio de opciones disponibles.
    -Si el espacio es de tipo:
        -Se agrega una imagen (Seleccionada aleatoriamente) de tipo al espacio correspondiente y su grupo funcional al espacio de opciones  disponibles.

si se presiona la imagen y se suelta en el area correcta (columna 1):
    -se verifica click presionado (mantenido) sobre imagen
    -si es verdad la imagen se actualiza con las coordenadas del mouse:
        -se verifica si al soltar el click las coordenadas del mouse estan dentro de un area valida
        -si es asi:
            -se verifica que esa imagen corresponde a esa area
            -si es asi: 
                -la imagen pasa a posicionarse dentro de esa area
            -no es asi:
                -la imagen regresa a su posicion inicial
            
cuando no quedan imagenes en las opciones disponibles, el juego termina.
            

'''

class Sce_Functional_Group(Scene):
    '''
    classdocs
    '''

    def __init__(self, director, background_name):
        '''
        Constructor
        '''
        Scene.__init__(self, director, background_name)
        self.functional_group = Functional_Group()
        self.element_collide = False

    def on_update(self):
        self.time = self.director.time 
        
        lbr = self.functional_group.rect_grid[LBR]
        
        key_lbr = self.functional_group.current_function_key
        for key, option in self.functional_group.options_functions.iteritems():
            option.updater(lbr)
            if option.rect.center == lbr.center and key == key_lbr:
                print "Keys: "+str((key_lbr, key))
                option.is_correct = True                
        
        rtr = self.functional_group.rect_grid[RTR]
        key_rtr = self.functional_group.current_type_key        
        for key, option in self.functional_group.options_types.iteritems():
            option.updater(rtr)   
            if option.rect.center == lbr.center and key == key_rtr:
                option.is_correct = True            
        
        


    def on_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN: 
            #print "MOUSEBUTTONUP"
            #mouse_pressed = pygame.mouse.get_pressed()
            mouse_pos = pygame.mouse.get_pos()
            
            for key, option in self.functional_group.options_functions.iteritems():
                option.pressed(mouse_pos)
               
            for key, option in self.functional_group.options_types.iteritems():
                option.pressed(mouse_pos)
                
        elif event.type == pygame.MOUSEBUTTONUP: 
            for key, option in self.functional_group.options_functions.iteritems():
                option.release()
               
            for key, option in self.functional_group.options_types.iteritems():
                option.release()


    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
        screen.blit(self.functional_group.current_function.img, self.functional_group.current_function.rect)
        screen.blit(self.functional_group.current_type.img, self.functional_group.current_type.rect)
        
        for option in self.functional_group.options_functions.itervalues():
            screen.blit(option.img, option.rect)
            
        for option in self.functional_group.options_types.itervalues():
            screen.blit(option.img, option.rect)            

        
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
        #print str(self.rect_grid)
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
        self.generate_grid()
           
    def generate_grid(self):
        function = randint(1, COTIDIAN_PAIRS)
        ctype = randint(1, COTIDIAN_PAIRS)
        
        self.current_function_key = str(function)
        self.current_function = self.functions[str(function)]
        self.current_function.rect.centerx = self.rect_grid[LTR].centerx
        self.current_function.rect.centery = self.rect_grid[LTR].centery
        
        self.current_type_key = [str(ctype)]
        self.current_type = self.types[str(ctype)]
        self.current_type.rect.centerx = self.rect_grid[RBR].centerx
        self.current_type.rect.centery = self.rect_grid[RBR].centery
        
        opt_function = function
        while opt_function == function:
            opt_function = randint(1, COTIDIAN_PAIRS)
            
        opt_type = ctype
        while opt_type == ctype:
            opt_type = randint(1, COTIDIAN_PAIRS)
        
        self.options_functions[str(opt_function)] = self.functions[str(opt_function)]
        self.options_types[str(opt_type)] = self.types[str(opt_type)]
        self.options_functions[str(ctype)] = self.functions[str(ctype)]
        self.options_types[str(function)] = self.types[str(function)]
        
        for key, option in self.options_functions.iteritems():
            option.resize(config.c_opt_size)
            self.options_functions[key] = option
            
        for key, option in self.options_types.iteritems():
            option.resize(config.c_opt_size)
            self.options_types[key] = option        
        
        self.options_functions[str(opt_function)].firts_pos(config.c_opt_pos)
        
        x = config.c_opt_pos[0]
        y = self.options_functions[str(opt_function)].rect.bottom + 10
        self.options_types[str(opt_type)].firts_pos((x, y))
        
        y = self.options_types[str(opt_type)].rect.bottom + 10
        self.options_functions[str(ctype)].firts_pos((x, y))
        
        y = self.options_functions[str(ctype)].rect.bottom + 10
        self.options_types[str(function)].firts_pos((x, y))                  
        
    def load_functions(self):
        for i in range(1, COTIDIAN_PAIRS+1):
            option = Option(config.coditidian_functions+str(i)+PNG_EXT, self.rect_grid[LTR].size)
            self.functions[str(i)] = option   

    def load_types(self):
        for i in range(1, COTIDIAN_PAIRS+1):
            option = Option(config.coditidian_types+str(i)+PNG_EXT, self.rect_grid[RTR].size)
            self.types[str(i)] = option                     
                        
        
class Option(Sprite):   
   
    def __init__(self, path, size):
        self.img = load_image(path, True)
        self.img = pygame.transform.scale(self.img, (size[0] - 20, size[1] - 20))
        self.init_pos = (0, 0)
        self.rect = self.img.get_rect()
        
        self.is_pressed = False
        self.is_correct = False
    
    def pressed(self, mouse_pos):
        if self.rect.collidepoint(mouse_pos): self.is_pressed = True
        else: self.is_pressed = False
        
    def release(self):
        self.is_pressed = False
        
    def updater(self, grid_rect):
        if self.is_pressed:
            mouse_pos = pygame.mouse.get_pos()
            self.move(mouse_pos)
        else:
            if self.rect.colliderect(grid_rect): 
                self.move(grid_rect.center)
            else:
                if not self.is_correct: 
                    self.move_to_firts_pos()
    
    def resize(self, size): 
        self.img = pygame.transform.scale(self.img, size)
        self.rect = self.img.get_rect()
    
    def move(self, (x, y)):
        self.rect.centerx = x
        self.rect.centery = y
        
    def firts_pos(self, (x, y)):
        self.rect.left = x
        self.rect.top = y
        self.init_pos = self.rect.topleft
        
    def move_to_firts_pos(self):
        self.rect.left = self.init_pos[0]
        self.rect.top = self.init_pos[1]        