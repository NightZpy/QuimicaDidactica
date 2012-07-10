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
        self.scene_winner =  Sce_Winner(director, 'winner', HANGMAN_SCENE)
        
        for buttom in self.common_buttoms.itervalues():
            buttom.is_visible = True

    def on_update(self):
        self.time = self.director.time 
        self.update()
        
        if not self.hangman.lose:
            word = ''
            self.is_complete = word.join(self.hangman.exposed) == self.hangman.word
            self.hangman.lose = self.hangman.intent == self.hangman.intents
        else:
            self.hangman.paused = True
                


    def on_event(self, event):
        self.event(event)
        if event.type == pygame.KEYDOWN:            
            if not self.hangman.paused and ((event.unicode.lower() in ("abcdefghijklmnopqrstuvwxyz")) or (event.key == pygame.K_SPACE and ' ' in self.hangman.word)):
                key = event.unicode.lower()
                #print "Tecla: "+key
                if (key in self.hangman.word.lower()) and (key not in self.hangman.typeds):
                    self.hangman.put_char(key)
                else:
                    self.hangman.intent += 1        
                                      

    def on_draw(self, screen):
        self.draw(screen)
        self.hangman.draw(screen)
        
        