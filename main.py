'''
Created on 26/06/2012

@author: nightzpy
'''
from director import Director
from sce_main_menu import Sce_Main_Menu
import pygame
from sce_functional_group import Sce_Functional_Group
from sce_nombrar import Sce_Nombrar
from sce_ahorcado import Sce_Ahorcado
from config import EXIT, STARTING, COTIDIAN_FUNCTION_SCENE, NOMBRAR_SCENE,\
    MAIN_MENU_SCENE


def main():
    director = Director()
    sce_main_menu = Sce_Main_Menu(director, MAIN_MENU_SCENE)
    sce_functional_group = Sce_Functional_Group(director, COTIDIAN_FUNCTION_SCENE)
    sce_nombrar = Sce_Nombrar(director, NOMBRAR_SCENE)
    #sce_nombrar = Sce_Ahorcado(director, "main_ahorcado")  
    scenes = {
              MAIN_MENU_SCENE: sce_main_menu,
              COTIDIAN_FUNCTION_SCENE: sce_functional_group,
              NOMBRAR_SCENE: sce_nombrar 
             }
      
    director.change_scene(sce_main_menu) 
    go = STARTING
    while(go != EXIT):
        go = director.loop()
        if go != EXIT:
            director.change_scene(scenes[go])

if __name__ == '__main__':
   pygame.init()
   main()