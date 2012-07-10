'''
Created on 29/06/2012

@author: nightzpy
'''
from scene import Scene
from config import MATCH_SCENE
from sce_winner import Sce_Winner
from match import Match
import pygame

class Sce_Match(Scene):
    '''
    classdocs
    '''

    def __init__(self, director, background_match):
        '''
        Constructor
        '''
        Scene.__init__(self, director, background_match)        
        self.match = Match()
        self.scene_winner =  Sce_Winner(director, 'winner', MATCH_SCENE)
        self.c_fails = 0
        
        self.match.generate_table()
        for buttom in self.common_buttoms.itervalues():
            buttom.is_visible = True

    def on_update(self):
        self.time = self.director.time 
        
        if not self.is_failed:
            self.update()
            
            for key_function, function in self.match.functions.iteritems():
                if not function.is_correct:                                                      
                    if function.is_pressed:
                        function.is_mark = True 
                        function.line.point_end = pygame.mouse.get_pos()
                        break
                        
                    if function.is_mark:                
                        for key_element, element in self.match.elements.iteritems():
                            if element.is_pressed and not element.is_mark:
                                if key_function==key_element:
                                    print "key_function: "+key_function
                                    print "key_element: "+key_element
                                    point_end = element.rect.midleft
                                    function.line.point_end = point_end
                                    function.is_correct = True
                                    function.is_mark = False
                                    element.is_mark = True
                                    break
                                else:
                                    self.c_fails += 1
                                    if self.c_fails >= 4:
                                        self.c_fails = 0
                                        self.is_failed = True
                                        
                                    element.is_pressed = False
                        function.is_mark = False
                               
            self.is_complete = self.match.check_complete()

    def on_event(self, event):
        self.event(event)
        
        if event.type == pygame.MOUSEBUTTONDOWN: 
            mouse_pos = pygame.mouse.get_pos()            
            for function in self.match.functions.itervalues():
                function.pressed(mouse_pos)
                
        elif event.type == pygame.MOUSEBUTTONUP:            
            for function in self.match.functions.itervalues():
                if function.is_pressed and not function.is_correct:            
                    for element in self.match.elements.itervalues():
                        mouse_pos = pygame.mouse.get_pos()
                        element.pressed(mouse_pos)
                    function.release()
                    break
                    
                        

    def on_draw(self, screen):
        self.draw(screen)       
        self.match.draw(screen)
        for function in self.match.functions.itervalues(): 
            if function.is_pressed or function.is_correct:
                pygame.draw.line(screen,function.line.color,function.line.point_init, function.line.point_end,3)
        
        if self.is_failed:
            screen.blit(self.failed_img, self.failed_rect)          
        
        