'''
Created on 29/06/2012

@author: nightzpy
'''
import pygame
from scene import Scene
from functional_group import Functional_Group
from config import LBR, RTR, COTIDIAN_FUNCTION_SCENE
from sce_winner import Sce_Winner

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
        self.scene_winner =  Sce_Winner(director, 'winner', COTIDIAN_FUNCTION_SCENE)   
        
        for buttom in self.common_buttoms.itervalues():
            buttom.is_visible = True
        
        self.c_fails = 0

    def on_update(self):
        self.time = self.director.time 
        self.update()
        if not self.is_failed:
            for key, option in self.functional_group.options_functions.iteritems():
                if option.is_release:
                    if option.rect.colliderect(self.functional_group.rect_grid[LBR]):
                        if key == self.functional_group.current_type_key:
                            option.move(self.functional_group.rect_grid[LBR].center)
                            option.is_correct = True   
                        else:
                            self.c_fails += 1
                            if self.c_fails >= 2:
                                self.c_fails = 0
                                self.is_failed = True                        
                            option.move_to_firts_pos()  
                    else:
                        option.move_to_firts_pos()                                            
                    
                if option.is_pressed:
                    if not option.is_correct:
                        option.move(pygame.mouse.get_pos())
                    
        for key, option in self.functional_group.options_types.iteritems():
            if option.is_release:
                if option.rect.colliderect(self.functional_group.rect_grid[RTR]):
                    if key == self.functional_group.current_function_key:
                        option.move(self.functional_group.rect_grid[RTR].center)
                        option.is_correct = True   
                    else:
                        option.move_to_firts_pos()  
                else:
                    option.move_to_firts_pos()                                                     
                    
            if option.is_pressed:
                if not option.is_correct:
                    option.move(pygame.mouse.get_pos())
                   
        self.is_complete = self.functional_group.check_complete()
                    
    def on_event(self, event):
        self.event(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_pos = pygame.mouse.get_pos()
            
            for option in self.functional_group.options_functions.itervalues():
                option.pressed(mouse_pos)
               
            for option in self.functional_group.options_types.itervalues():
                option.pressed(mouse_pos)
                
        elif event.type == pygame.MOUSEBUTTONUP:            
            for option in self.functional_group.options_functions.itervalues():                
                option.release()
               
            for option in self.functional_group.options_types.itervalues():
                option.release()

    def on_draw(self, screen):
        self.draw(screen)
        self.functional_group.draw(screen)
        if self.is_failed:
            screen.blit(self.failed_img, self.failed_rect)                         
                        

        
                    
                        
        
