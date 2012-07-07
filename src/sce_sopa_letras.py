'''
Created on 29/06/2012

@author: nightzpy
'''
from scene import Scene

class Sce_Sopa_Letras(Scene):
    '''
    classdocs
    '''

    def __init__(self, director, background_name):
        '''
        Constructor
        '''
        Scene.__init__(self, director, background_name)

    def on_update(self):
        self.time = self.director.time 


    def on_event(self, event):
        pass


    def on_draw(self, screen):
        screen.blit(self.background, (0, 0))
        