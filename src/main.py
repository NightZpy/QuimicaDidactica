'''
Created on 26/06/2012

@author: nightzpy
'''
from director import Director
from sce_main import Sce_Main
import pygame
from config import EXIT, MAIN_SCENE

def main():   
    director = Director()
    sce_main = Sce_Main(director, MAIN_SCENE)       
    director.change_scene(sce_main) 
    go = sce_main
    while(go != EXIT):
        go = director.loop()
        if go != EXIT: director.change_scene(go)
        else:
            pygame.quit()
                

if __name__ == '__main__':
    pygame.init()
    main()    