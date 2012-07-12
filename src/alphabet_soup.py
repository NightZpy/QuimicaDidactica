'''
Created on 11/07/2012

@author: nightzpy
'''
from random import randint
from pygame import rect
import config
from char import Char

VERT = 1
HORZ = 2
DIAGONAL_PRIMARY = 3
DIAGONAL_SECONDARY = 4

INVERSE = 1

MAX_ROWS = 20
MAX_COLS = 20

class Alphabet_Soup(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.soup  = []
        self.words_char = {}
        self.words_chars_rect = {}
        self.chars = {}
        
        self.words = [ 'avion', 'auto', 'persona', 'animal', "caratula", "espejo", "tecnico", "escuela", "barco", "caballo",
                      "cepillo", "ballena", "tiburon", "estocolmo", "libreta", "sellador", "parabrisas", "comida", "cantimplora"]
                
        self.set_empty_soup()
        self.preload_dict_words()        
        self.add_words_to_soup()
        self.load_chars()
        #for word, chars in self.words_chars_rect.iteritems():
            #print "Word: {0} | Size: {1} - Char Size: {2} | Chars: {3}".format(word, len(word), len(chars[1]), chars)
            
                
        self.load_random_chars()
        for i in range(MAX_ROWS):
                print str(self.soup[i])      
    
    def load_chars(self):
        for word, data in self.words_chars_rect.iteritems():
            chars, rects = data[0], data[1]                        
            for i in range(len(data[0])):
                char = Char(chars[i], rects[i])
                self.words_char[word].append(char) 
            
    def draw(self, screen):
        for chars in self.words_char.itervalues():
            for char in chars:
                char.draw(screen)
        
    def create_words_chars_rect(self, word, char, (x , y)):
        if x==0 and y==0:            
            x, y = config.alphabet_soup_char_pos
        elif x==0 and y>0:
            x, y = config.alphabet_soup_char_pos[0] + ((y) * config.alphabet_soup_char_size[0]), config.alphabet_soup_char_pos[1]
        elif x!=0 and y==0:
            x, y = config.alphabet_soup_char_pos[0], config.alphabet_soup_char_pos[1] + ((x) * config.alphabet_soup_char_size[1])
        elif x!=0 and y!=0:  
            x, y = config.alphabet_soup_char_pos[0] + ((y) * config.alphabet_soup_char_size[0]), config.alphabet_soup_char_pos[1] + ((x) * config.alphabet_soup_char_size[1])
        #print "Word: ",word,"Char: ",char,"Pos en: ", (x, y) 
        self.words_chars_rect[word][0].append(char)
        self.words_chars_rect[word][1].append(rect.Rect((x, y), (config.alphabet_soup_char_size)))
     
    def preload_dict_words(self):
        words = []
        words2 = []
        for word in self.words:
            words2.append((word, []))
            words.append((word, ([], [])))
        self.words_chars_rect = dict(words)
        self.words_char = dict(words2)                            
        
    def set_empty_soup(self):
        for i in range(MAX_ROWS):
            #row = []
            self.soup.append([])
            for j in range(MAX_COLS):
                self.soup[i].append('')

    def add_words_to_soup(self):
        n_words = len(self.words)
        words_add = []
        for i in range(n_words):
            word = randint(0, n_words-1)
            word = self.words[word]
            while words_add.count(word) > 0:
                word = randint(0, n_words-1)
                word = self.words[word]                
            #print "Palabra a agregar: "+str(i+1)+" -> "+word
            x , y = randint(0, MAX_ROWS-1), randint(0, MAX_COLS-1)
            sense = randint(1, 2)
            direction = randint(1, 4)                
            while not self.load_word(word, sense, direction, (x, y)):
                self.words_chars_rect[word] = [], []
                x , y = randint(0, MAX_ROWS-1), randint(0, MAX_COLS-1)
                sense = randint(1, 4)
                direction =randint(1, 2)       
            words_add.append(word)                            
    
    def load_random_chars(self):
        for x in range(MAX_ROWS):
            for y in range(MAX_COLS):
                c_chars = randint(0, len(config.chars)-1) 
                if self.soup[x][y] == '': self.soup[x][y] = config.chars[c_chars]           
        
    def load_word(self, word, sense, direction, (x, y)):                      
        word_size = len(word)
        char = 0
        char_add = []
        if sense==VERT:
            #print "Vertical"
            if direction == INVERSE: 
                if (x - word_size) > 0:                    
                    for x in range(x, x-word_size, -1):
                        if self.soup[x][y] == '' or self.soup[x][y] == word[char]:
                            if self.soup[x][y] == '': char_add.append((x, y))
                            #if (self.soup[x][y] == word[char]): print "Iguales: "+str((x, y))+" -> "+str(self.soup[x][y])+"="+str(word[char])
                            self.soup[x][y] = word[char]   
                            self.create_words_chars_rect(word, word[char],  (x, y))                                                                                           
                            char += 1
                        else:
                            if len(char_add)>0:
                                #print "Eliminando ocupadas erroneamente: "+str(len(char_add))
                                for x, y in char_add:
                                    #print "Char: "+str((x, y))+" -> "+self.soup[x][y] 
                                    self.soup[x][y] = ''                                                             
                            return False
                else: return False
            elif (x + word_size) < MAX_ROWS:
                for x in range(x, x+word_size):
                    if self.soup[x][y] == '' or self.soup[x][y] == word[char]:
                        if self.soup[x][y] == '': char_add.append((x, y))
                        #if (self.soup[x][y] == word[char]): print "Iguales: "+str((x, y))+" -> "+str(self.soup[x][y])+"="+str(word[char])
                        self.soup[x][y] = word[char]
                        self.create_words_chars_rect(word, word[char],  (x, y))                            
                        char += 1
                    else:
                        if len(char_add)>0:
                            #print "Eliminando ocupadas erroneamente: "+str(len(char_add))
                            for x, y in char_add:
                                #print "Char: "+str((x, y))+" -> "+self.soup[x][y] 
                                self.soup[x][y] = ''                             
                        return False
            else: return False 
        elif sense==HORZ:
            #print "Horizontal"
            if direction == INVERSE: 
                if (y - word_size) > 0:           
                    for y in range(y, y-word_size, -1):
                        if self.soup[x][y] == '' or self.soup[x][y] == word[char]:
                            if self.soup[x][y] == '': char_add.append((x, y))
                            #if (self.soup[x][y] == word[char]): print "Iguales: "+str((x, y))+" -> "+str(self.soup[x][y])+"="+str(word[char])
                            self.soup[x][y] = word[char] 
                            self.create_words_chars_rect(word, word[char],  (x, y))                                
                            char += 1
                        else:
                            if len(char_add)>0:
                                #print "Eliminando ocupadas erroneamente: "+str(len(char_add))
                                for x, y in char_add:
                                    #print "Char: "+str((x, y))+" -> "+self.soup[x][y] 
                                    self.soup[x][y] = ''                          
                            return False
                else: return False
            elif (y + word_size) < MAX_ROWS:                       
                for y in range(y, y+word_size):
                    if self.soup[x][y] == '' or self.soup[x][y] == word[char]:
                        if self.soup[x][y] == '': char_add.append((x, y))
                        #if (self.soup[x][y] == word[char]): print "Iguales: "+str((x, y))+" -> "+str(self.soup[x][y])+"="+str(word[char])
                        self.soup[x][y] = word[char]  
                        self.create_words_chars_rect(word, word[char],  (x, y))                           
                        char += 1
                    else:                        
                        if len(char_add)>0:
                            #print "Eliminando ocupadas erroneamente: "+str(len(char_add))
                            for x, y in char_add:
                                #print "Char: "+str((x, y))+" -> "+self.soup[x][y] 
                                self.soup[x][y] = ''                             
                        return False
            else: return False
        elif sense==DIAGONAL_PRIMARY:
            #print "DIAGONAL_PRIMARY"
            if direction == INVERSE:
                if (y - word_size) > 0 and (x - word_size) > 0:
                    for y in range(y, y-word_size, -1):
                        if self.soup[x][y] == '':
                            if self.soup[x][y] == '': char_add.append((x, y))
                            #if (self.soup[x][y] == word[char]): print "Iguales: "+str((x, y))+" -> "+str(self.soup[x][y])+"="+str(word[char])
                            self.soup[x][y] = word[char] 
                            self.create_words_chars_rect(word, word[char],  (x, y))                                
                            x-=1
                            char += 1
                        else:
                            if len(char_add)>0:
                                #print "Eliminando ocupadas erroneamente: "+str(len(char_add))
                                for x, y in char_add:
                                    #print "Char: "+str((x, y))+" -> "+self.soup[x][y] 
                                    self.soup[x][y] = ''                             
                            return False
                return False
            elif (y + word_size) < MAX_COLS and (x + word_size) < MAX_ROWS:
                for y in range(y, y+word_size):
                    if self.soup[x][y] == '' or self.soup[x][y] == word[char]:
                        if self.soup[x][y] == '': char_add.append((x, y))
                        #if (self.soup[x][y] == word[char]): print "Iguales: "+str((x, y))+" -> "+str(self.soup[x][y])+"="+str(word[char])
                        self.soup[x][y] = word[char] 
                        self.create_words_chars_rect(word, word[char],  (x, y))                            
                        x+=1
                        char += 1
                    else:
                        if len(char_add)>0:
                            #print "Eliminando ocupadas erroneamente: "+str(len(char_add))
                            for x, y in char_add:
                                #print "Char: "+str((x, y))+" -> "+self.soup[x][y] 
                                self.soup[x][y] = ''                             
                        return False
            else: return False
        elif sense==DIAGONAL_SECONDARY:
            #print "DIAGONAL_SECONDARY"
            if direction == INVERSE:
                if (y - word_size) > 0 and (x + word_size) < MAX_ROWS:                       
                    for y in range(y, y-word_size, -1):
                        if self.soup[x][y] == '' or self.soup[x][y] == word[char]:
                            if self.soup[x][y] == '': char_add.append((x, y))
                            #if (self.soup[x][y] == word[char]): print "Iguales: "+str((x, y))+" -> "+str(self.soup[x][y])+"="+str(word[char])
                            self.soup[x][y] = word[char]    
                            self.create_words_chars_rect(word, word[char],  (x, y))                             
                            x+=1
                            char += 1
                        else:
                            if len(char_add)>0:
                                #print "Eliminando ocupadas erroneamente: "+str(len(char_add))
                                for x, y in char_add:
                                    #print "Char: "+str((x, y))+" -> "+self.soup[x][y] 
                                    self.soup[x][y] = ''                             
                            return False
                return False
            elif (y + word_size) < MAX_COLS and (x - word_size) > 0:
                for y in range(y, y+word_size):
                    if self.soup[x][y] == '' or self.soup[x][y] == word[char]:
                        if self.soup[x][y] == '': char_add.append((x, y))
                        #if (self.soup[x][y] == word[char]): print "Iguales: "+str((x, y))+" -> "+str(self.soup[x][y])+"="+str(word[char])
                        self.soup[x][y] = word[char] 
                        self.create_words_chars_rect(word, word[char],  (x, y))                            
                        x-=1
                        char += 1
                    else:
                        if len(char_add)>0:
                            #print "Eliminando ocupadas erroneamente: "+str(len(char_add))
                            for x, y in char_add:
                                #print "Char: "+str((x, y))+" -> "+self.soup[x][y] 
                                self.soup[x][y] = ''                             
                        return False
            else: return False
        #print "Pos: "+str((x, y)) 
        return True
    
#Alphabet_Soup()        