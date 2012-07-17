'''
Created on 29/06/2012

@author: nightzpy
'''
from scene import Scene
from config import HANGMAN_SCENE
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
        if not self.is_failed:
            self.update()            
            if not self.hangman.lose:
                word = ''
                self.is_complete = word.join(self.hangman.exposed) == self.hangman.word
                self.is_failed = self.hangman.lose = self.hangman.intent == self.hangman.intents
            else:
                self.hangman.paused = True                

    def on_event(self, event):        
        self.event(event) 
        if not self.is_failed: 
            if not self.hangman.lose:                      
                if event.type == pygame.KEYDOWN:            
                    if not self.hangman.paused and ((event.unicode.lower() in ("abcdefghijklmnopqrstuvwxyz")) or (event.key == pygame.K_SPACE and ' ' in self.hangman.word)):
                        key = event.unicode.lower()
                        if (key in self.hangman.word.lower()) and (key not in self.hangman.typeds):
                            self.hangman.put_char(key)
                        else:
                            self.hangman.intent += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:                        
                self.hangman.intent = 0
                self.hangman.choose_word()
                self.hangman.typeds = []
                self.hangman.lose = False           
                                      

    def on_draw(self, screen):
        self.draw(screen)
        self.hangman.draw(screen)
        
        