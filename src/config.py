# -*- encoding: utf-8 -*-


""" Configuracion general del proyecto """
from glob import glob

# Nombre
NAME = "Jugando con los Grupos Funcionales Por: Rosa Duque & Lenny Contreras"
EXIT = -1
GAME_OVER = 0
STARTING = 1
NEXT_SCENE = 2
PAUSE = 3

# Color constant
WHITE = (255, 255, 255)
BLACK = (000, 000, 000)


#Scenes constant
MAIN_MENU_SCENE = 'main_menu'
MAIN_SCENE = 'main'
HANGMAN_SCENE = 'main_hangman'
MATCH_SCENE = 'main_match'
NAME_SCENE = 'main_name'
CRUCIGRAMA_SCENE = 'main_crucigrama'
ALPHABET_SOUP_SCENE = 'main_alphabet_soup'
COTIDIAN_FUNCTION_SCENE = 'main_cotidian_function'
DEFINITIONS_SCENE = 'main_definitions'
WINNER_SCENE = 'winner'

# Rect dict constant for grid in cotidian function game
LTR = 'left_top_rect'
RTR = 'right_top_rect'
LBR = 'left_bottom_rect'
RBR = 'right_bottom_rect'

# page buttoms
NEXT_BTN = 'next'
PREV_BTN = 'previous'
GO_SCHEME = 'go_scheme'

# Items
TEXT_FIELD = 'text_field'

# Number of problems in every cotidian game
NUMBER_COTIDIAN_OPTIONS = 2

# Number of problems in every name game
NUMBER_NAME_OPTIONS = 3

SMALL = '_small'
BIG = '_big'
PNG_EXT = '.png'
JPG_EXT = '.jpg'
END = '_end'
INIT = '_init'

#String of chars
chars = 'abcdefghijklmnopqrstuvwxyz'

# Resolution
width = 800
height = 600

# main menu button size
b_size = (270, 100)

# title correct size 
correct_title_size = (300, 130)

# title winner size 
winner_title_size = (550, 200)

# title winner pos
winner_title_pos = (width / 2, (height / 2) - 100) 

# size main buttons
main_menu_btn_size = (120, 60)
exit_btn_size = (120, 60)

# cotidian option size
c_opt_size = (250, 105)

#init pos for cotidian options
c_opt_pos = (515, 130)

# names exercise size
name_exercise_size = (400, 260)

# names exercise pos
name_exercise_pos = ((width / 2) - 140, 260)

# Size name text fiel
name_text_field_size = (500, 100)

# Name text field default pos
name_text_field_pos = (name_exercise_pos[0]+50, name_exercise_pos[1] + (name_exercise_pos[1] / 2) + 80)

# names option size
name_opt_size = (300, 25)

# names option pos
name_opt_pos = (name_text_field_pos[0] + (name_text_field_pos[0] / 2) + 20, name_exercise_pos[1]-(name_exercise_size[1] / 2)+10)

# match function size
match_function_size = (200, 65)

# match function size
match_element_size = (200, 65)

# match function size
match_function_pos = (50, 90)

# match element pos
match_element_pos = (width - 250, 90)

# hangman text field pos
hangman_text_field_pos = (width / 2, 113)

# Size hangman text fiel
hangman_text_field_size = (600, 60)

# hangman text exposed pos
hangman_text_exposed_pos = ((hangman_text_field_pos[0] - (hangman_text_field_size[0] / 2)) + 35, hangman_text_field_pos[1]-11)

# hangman text msg pos
hangman_text_msg_pos = (width / 2, height - 200)

# hangman track msg pos
hangman_track_msg_pos = (width / 2, height - 200)

# pages buttoms size:
page_btn_size = (200, 60)

page_btn_next_pos = ((width / 2) + 170, (height-20))

page_btn_prev_pos = ((width / 2) - 170, (height-20))

page_btn_go_scheme_pos = ((width / 2), (height-20))

# Crucigrama button size
crux_b_size = (14, 25)

# Failed img size
failed_size = (400, 200)

# Failed img pos
failed_pos = (width / 2, height / 2)

#alphabet soup chars size
alphabet_soup_char_size = (30, 30)

#alphabet soup space between chars
alphabet_soup_char_space = (5, 5)

#alphabet soup chars init pos
alphabet_soup_char_pos = (0, 0)

#alphabet soup words to search pos
alphabet_soup_word_list_pos = (width - 100, 80)

#alphabet soup words to search size
alphabet_soup_word_list_size = (150, 35)

#alphabet soup words to search space
alphabet_soup_word_list_space = (width - 150, 150)

#alphabet soup btn pos
alphabet_soup_btn_correct_pos = (width - 100, height - 150)

#alphabet soup btn size
alphabet_soup_btn_correct_size = (180, 90)

# exit button pos
exit_btn_pos = (width - (exit_btn_size[0] * 2.2), height - 30)
main_menu_btn_pos = ((exit_btn_pos[0] + exit_btn_size[0] + 20), exit_btn_pos[1])

# Directories
sprites = "resources/images/sprites/"
backgrounds = "resources/images/backgrounds/"
buttoms_png = "resources/images/buttoms/png/"
titles = "resources/images/titles/"
menus = "resources/images/menus/"
coditidian_functions = "resources/images/cotidian/function/"
coditidian_types = "resources/images/cotidian/type/"
name_items = "resources/images/name/"
name_names = "resources/images/name/names/"
name_exercises = "resources/images/name/exercises/"
match_functions = "resources/images/matching/function/"
match_elements = "resources/images/matching/element/"
hangman = "resources/images/hangman/"
definition_pages = "resources/images/definitions/"
crux_words_imgs = "resources/images/crucigrama/"
alphabet_soup_words = "resources/images/alphabet_soup/words/"
#alphabet_soup_word_list = "resources/images/alphabet_soup/words/"
alphabet_soup_char_list = "resources/images/alphabet_soup/chars/"
fonts = "resources/fonts/"
audios = "resources/audios/"

# Number of cotidian pairs
COTIDIAN_PAIRS = len(glob(coditidian_functions+'*'+PNG_EXT))

# Number of name pairs
NAME_PAIRS = len(glob(name_exercises+'*'+PNG_EXT))

# Number of match pairs
MATCH_PAIRS = len(glob(match_functions+'*'+PNG_EXT))   
    
        
        
        
        
    
    