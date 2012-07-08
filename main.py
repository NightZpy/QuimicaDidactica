'''
Created on 26/06/2012

@author: nightzpy
'''
from director import Director
from sce_main_menu import Sce_Main_Menu
import pygame
from config import EXIT, MAIN_MENU_SCENE

def main():
    director = Director()
    sce_main_menu = Sce_Main_Menu(director, MAIN_MENU_SCENE)
      
    director.change_scene(sce_main_menu) 
    go = sce_main_menu
    while(go != EXIT):
        go = director.loop()
        if go != EXIT: director.change_scene(go)
        else:
            pygame.quit()
            exit()
                

if __name__ == '__main__':
    #f = open("archivo.txt", "r")
    #lineas = f.readlines()
    
    pygame.init()
    main()