'''
Created on 29/06/2012

@author: nightzpy
'''
from scene import Scene
from config import HANGMAN_SCENE, END
from sce_winner import Sce_Winner
from hangman import Hangman
import pygame

class Sce_Hangman(Scene):
    '''
    classdocs
    '''

    def __init__(self, director, background_hangman):
        '''
        Constructor
        '''
        Scene.__init__(self, director, background_hangman)        
        self.hangman = Hangman()
        self.scene_winner =  Sce_Winner(director, background_hangman+END, HANGMAN_SCENE)
        
        self.hangman.generate_table()
        for buttom in self.common_buttoms.itervalues():
            buttom.is_visible = True

    def on_update(self):
        self.time = self.director.time 
        self.update()


    def on_event(self, event):
        self.event(event)

                    
                        

    def on_draw(self, screen):
        self.draw(screen)
        self.hangman.draw(screen)
        
        