'''
Created on 11/07/2012

@author: nightzpy
'''
from random import randint, randrange
from pygame.rect import Rect
import config
from char import Char
from graphics import string_to_image
from config import BLACK

VERT = 1
HORZ = 2
DIAGONAL_PRIMARY = 3
DIAGONAL_SECONDARY = 4

INVERSE = 1

MAX_ROWS = 20
MAX_COLS = 20
MAX_WORDS = 10

class Alphabet_Soup(object):
    '''
    classdocs
    '''
    def __init__(self):
        '''
        Constructor
        '''
        self.is_failed = False
        self.is_complete = False        
        self.soup  = []
        self.soup_chars = []
        self.words_char = {}
        self.valid_words = {}
        self.complete_words = []
        self.chars = {}
        
        self.all_words = [] 
        self.words = []
        self.words_dict = {}
                
        self.set_empty_soup()
        self.load_words_from_file('words.txt')
        self.load_random_words()
        self.preload_dict_words()        
        self.add_words_to_soup()         
        self.load_word_list()                         
        self.load_random_chars()
        self.load_chars()     
    
    '''def load_chars(self):
        for word, data in self.valid_words.iteritems():
            chars, rects = data[0], data[1]                        
            for i in range(len(data[0])):
                char = Char(chars[i], rects[i])
                self.words_char[word].append(char)''' 
    
    def load_word_list(self):
        words = []
        color = BLACK
        i = 0
        size = 30
        heigth = config.alphabet_soup_word_list_size[1]
        x_init, y_init = config.alphabet_soup_word_list_pos
        x, y = x_init, y_init
        for word in self.words:
            if i>0: y = y_init + (i * heigth)
            img = string_to_image(word, (x, y), color, size)
            words.append((word, img))
            i+=1
        self.words_dict = dict(words)
    
    def load_words_from_file(self, name):
        f = open(config.alphabet_soup_words+name, "r")
        self.all_words = f.readlines()
        for word in range(len(self.all_words)):
            self.all_words[word] = self.all_words[word].replace('\n', '')
        f.close()
    
    def load_random_words(self):
        i = 0
        while i < MAX_WORDS:
            word = self.all_words[randrange(len(self.all_words))].upper()
            while self.words.count(word)>0: word = self.all_words[randrange(len(self.all_words))].upper()
            self.words.append(word)
            i += 1     
    
    def load_chars(self):
        width, heigth = config.alphabet_soup_char_size                
        x_init, y_init = config.alphabet_soup_char_pos
        y = y_init        
        for row in range(MAX_ROWS):            
            if row > 0: y = y_init + (heigth * row)
            x = x_init
            for col in range(MAX_COLS):
                if col > 0: x = x_init + (width * col)
                char = self.soup[row][col]
                #print "Char: ", char, " - Pos: "+str((x, y))
                rect = Rect((x, y), (width, heigth))
                self.soup_chars[row][col] = Char(char, rect)     
    
    def check_collide_with_char(self, point):
        for row in self.soup_chars:
            for char in row:
                char.collide_point(point)
    
    def check_word(self):
        chars_marks = self.get_chars_marks()
        word_mark = ''
        for char in chars_marks: word_mark += char.char
        print "Marcada: "+word_mark
        c_marks = len(chars_marks)
        c_corrects = 0
        if c_marks>=min(self.get_list_words_sizes()):
            for word, data in self.valid_words.iteritems():
                print "A revisar: ", word
                c_chars = len(data[0])
                if c_marks == c_chars:
                    #print "Revisando..."
                    for i in range(c_chars):
                        c = data[0][i]
                        rect = data[1][i]
                        print "Comparando: Char->",c," | Rect->",str(rect)                                               
                        for char in chars_marks:
                            #print "::::con: Char->",char.char," | Rect->", str(char.rect)
                            if char.is_mark and char.char == c and char.collide_rect(rect):
                                print "::::con: Char->",char.char," | Rect->", str(char.rect)
                                if not char.is_correct: char.is_mark = False
                                else: char.is_mark = True 
                                c_corrects += 1
                                break
                    #print "Correctas: "+str(c_corrects)
                    if c_corrects == c_marks:
                        print "Encontrada: "+word
                        for char in chars_marks: char.is_correct = True
                        self.complete_words.append(word)
                        self.is_complete = len(self.words) <= len(self.complete_words)
                        self.is_failed = False
                        return word
                    c_corrects = 0
        print "..............No encontrada.................."
        for char in chars_marks: char.release()
        self.is_failed = True
        return False
    
    def get_chars_marks(self):
        marks = []
        for row in self.soup_chars:
            for char in row:
                if char.is_mark: marks.append(char)
        return marks
     
    def get_list_words_sizes(self):
        if len(self.words) > 0:
            sizes = []
            for word in self.words:
                sizes.append(len(word))
            return sizes
        return []
                
    def update(self):
        for row in self.soup_chars: 
            for char in row: 
                char.updater()
           
    def draw(self, screen):
        '''for chars in self.words_char.itervalues():
            for char in chars:
                char.draw(screen)'''
        for row in self.soup_chars:
            for char in row:
                char.draw(screen)
        #print "Word dict size: ", len(self.words_dict)
        for word, (img, rect) in self.words_dict.iteritems():
            #print "Drawning: ", word
            if self.complete_words.count(word) == 0:
                screen.blit(img, rect)
        
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
        self.valid_words[word][0].append(char)
        self.valid_words[word][1].append(Rect((x, y), (config.alphabet_soup_char_size)))
     
    def preload_dict_words(self):
        words = []
        words2 = []
        for word in self.words:
            words2.append((word, []))
            words.append((word, ([], [])))
        self.valid_words = dict(words)
        self.words_char = dict(words2)                            
        
    def set_empty_soup(self):
        for i in range(MAX_ROWS):
            self.soup.append([])
            self.soup_chars.append([])
            j = 0
            while j < MAX_COLS:
                self.soup[i].append('')
                self.soup_chars[i].append('')
                j += 1

    def add_words_to_soup(self):
        n_words = len(self.words)
        words_add = []
        i = 0
        while i < n_words:
            i += 1 
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
                self.valid_words[word] = [], []
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