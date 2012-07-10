'''
Created on 06/07/2012

@author: nightzpy
'''
from config import PNG_EXT, TEXT_FIELD, MATCH_PAIRS, WHITE, BLACK
from random import randint
import config
from option import Option
from graphics import load_image, resize, string_to_image
import pygame

class Hangman:
    '''
    classdocs
    '''

    def __init__(self):
        self.text_field_img = resize(load_image(config.name_items+TEXT_FIELD+PNG_EXT, True), config.hangman_text_field_size)
        self.text_field_rect = self.text_field_img.get_rect()
        self.text_field_rect.center = config.hangman_text_field_pos
        
        self.changed = False
        self.intents = 8
        self.paused = False
        self.is_complete = False
        self.tracks = []
        self.words = []
        self.typeds = []
        self.intent = 0
        self.lose = False
        self.word = ''
        self.track = ''
        self.exposed = ''
        
        self.load_words()            
        self.choose_word()
                 
    
    def choose_word(self):
        word_num = randint(0, len(self.words) - 1)
        self.word = self.words[word_num].replace('\n', '').lower()
        #print "Word: "+self.word
        self.track = self.tracks[word_num].replace('\n', '')
        self.split_track()
        self.exposed = ("_ "*len(self.word)).split()
    
    def put_char(self, char):
        for i in range(len(self.word)):
            if self.word[i]==char:
                self.exposed[i]=self.word[i]
                self.changed=True
        self.typeds.append(char)        
    
    def split_track(self):
        tracks = self.track.split(' ')
        c_words = len(tracks)
        #print "C_words: "+str(c_words)
        #print "Track: "+str(tracks)
        n_splits = 0
        new_track = []
        
        if c_words > 4:
            n_splits = c_words / 4            
            cut_track = ''
            init = 0
            for i in range(n_splits):
                for j in range(init, init+4):
                    cut_track += tracks[j]+' '
                    if j>=init+3: init = init+4               
                new_track.append(cut_track)
                cut_track = ''
            if (c_words % 4) > 0:  
                for i in range(init, c_words):
                    cut_track += tracks[i]+' '
                new_track.append(cut_track)
        else:
            new_track.append(self.track)
            
        self.track = new_track  
        #print "Track: "+str(self.track)      
       
    def load_words(self):
        f = open(config.hangman+'words.txt', "r")
        lines = f.readlines()
        t_lines = len(lines)
        c_lines = 0
        while c_lines < t_lines:
            self.tracks.append(lines[c_lines])
            self.words.append(lines[c_lines+1])
            c_lines += 2            

    def draw_hangman(self, screen):
        for i in range(self.intent):
            if i==0:#DIBUJANDO CABEZA
                pygame.draw.circle(screen,(0,0,255),(config.width/2,config.height/3),30,2)
            elif i==1:#DIBUJANDO COLUMNA
                pygame.draw.line(screen,(0,0,255),(config.width/2,config.height/3+30),(config.width/2,config.height/3+110),5)
            elif i==2:#DIBUJANDO MANOS
                pygame.draw.line(screen,(0,0,255),(config.width/2,config.height/3+30),(config.width/2+55,config.height/3+55),3)
                pygame.draw.line(screen,(0,0,255),(config.width/2,config.height/3+30),(config.width/2-55,config.height/3+55),3)
            elif i==3:#DIBUJANDO PIES
                    pygame.draw.line(screen,(0,0,255),(config.width/2,config.height/3+110),(config.width/2+55,config.height/3+110+55),3)
                    pygame.draw.line(screen,(0,0,255),(config.width/2,config.height/3+110),(config.width/2-55,config.height/3+110+55),3)
            elif i==4:#CARA NORMAL
                pygame.draw.circle(screen,(0,0,255),(config.width/2-10,config.height/3-5),6)
                pygame.draw.circle(screen,(0,0,255),(config.width/2+10,config.height/3-5),6)
                    
                pygame.draw.line(screen,(0,0,255),(config.width/2-10,config.height/3+10),(config.width/2+10,config.height/3+10),3)
        
            elif i==5:#DIBUJANDO EL OBJETO SUICIDA
                #BASE
                pygame.draw.polygon(screen,(250,150,0),((config.width/2+100,config.height/3+110+55),
                                                                 (config.width/2+200,config.height/3+110+55),
                                                                 (config.width/2+170,config.height/3+120),
                                                                 (config.width/2+120,config.height/3+120)),4)
                #VIGA
                pygame.draw.line(screen,(250,150,0),(config.width/2+140,config.height/3+120),(config.width/2+140,config.height/5),8)
            elif i==6:#DIBUJANDO EL OBJETO SUICIDA
                    
                #BASE SUICIDA
                pygame.draw.line(screen,(250,150,0),(config.width/2+140,config.height/5),(config.width/2,config.height/5),10)
            elif i==7:
        
                pygame.draw.circle(screen,(0,0,0),(config.width/2,config.height/3),30)#BORRAMOS LA CABEZA ANTERIOR
                    
                pygame.draw.line(screen,(250,10,20),(config.width/2+50,config.height/5),(config.width/2,config.height/3+30),2)#CUERDA
                pygame.draw.circle(screen,(0,0,255),(config.width/2,config.height/3),30,2)#CREAMOS UNA CABEZA DE NUEVO
                #CARA SUICIDA
                pygame.draw.circle(screen,(255,0,0),(config.width/2-10,config.height/3-5),5)
                pygame.draw.circle(screen,(255,0,0),(config.width/2+10,config.height/3-5),5)
                    
                pygame.draw.line(screen,(255,0,0),(config.width/2-10,config.height/3+10),(config.width/2+10,config.height/3+10),2)#BOCA        

    def draw_text_exposed(self, screen):        
        first = True        
        x = 0
        for i in self.exposed:
            char = string_to_image(i, config.hangman_text_exposed_pos, BLACK, 28)
            if first:                    
                screen.blit(char[0], char[1])
                x = char[1].left
                first = False
            else:
                x += 18
                char[1].left = x
                screen.blit(char[0], char[1])
                    
    def draw_you_lose(self, screen):            
        if self.lose: 
            text = string_to_image('Perdiste. La palabra era: '+self.word, config.hangman_text_msg_pos, BLACK, 30)
            screen.blit(text[0], text[1]) 
            
    def draw_track(self, screen):
        if not self.lose and not self.is_complete:
            first = True
            y = 0
            for text in self.track:
                text = string_to_image(text, config.hangman_track_msg_pos, BLACK, 25)
                if first:                     
                    y = text[1].centery
                    first = False
                else:
                    y += 25
                    text[1].centery = y                                            
                screen.blit(text[0], text[1]) 

    def draw(self, screen):
        screen.blit(self.text_field_img, self.text_field_rect)
        self.draw_hangman(screen)
        self.draw_text_exposed(screen)
        self.draw_you_lose(screen)
        self.draw_track(screen)
            
            
            
            