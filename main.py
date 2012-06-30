'''
Created on 26/06/2012

@author: nightzpy
'''
from director import Director
from sce_main_menu import Sce_Main_Menu
import pygame


def main():
    director = Director()
    sce_main_menu = Sce_Main_Menu(director)
    director.change_scene(sce_main_menu) 
    go = director.loop()

if __name__ == '__main__':
   pygame.init()
   main()