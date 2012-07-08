# -*- encoding: utf-8 -*-


""" Configuracion general del proyecto """
from glob import glob

# Nombre
NAME = "Química Didáctica"
EXIT = -1
GAME_OVER = 0
STARTING = 1
NEXT_SCENE = 2
PAUSE = 3

#Scenes constant
MAIN_MENU_SCENE = 'main_menu'
HANGMAN_SCENE = 'main_ahorcado'
MATCH_SCENE = 'main_match'
NAME_SCENE = 'main_name'
CRUCIGRAMA_SCENE = 'main_crucigrama'
SOPA_LETRAS_SCENE = 'main_sopa'
COTIDIAN_FUNCTION_SCENE = 'main_cotidian_function'
DEFINITIONS_SCENE = 'main_definition'
WINNER_SCENE = 'winner'

# Rect dict constant for grid in cotidian function game
LTR = 'left_top_rect'
RTR = 'right_top_rect'
LBR = 'left_bottom_rect'
RBR = 'right_bottom_rect'

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

# Resolution
width = 800
height = 600

# main menu button size
b_size = (270, 140)

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
c_opt_size = (160, 80)

#init pos for cotidian options
c_opt_pos = (515, 130)

# names exercise size
name_exercise_size = (300, 300)

# names exercise pos
name_exercise_pos = ((width / 2) - 170, 260)

# Size name text fiel
name_text_field_size = (400, 80)

# Name text field default pos
name_text_field_pos = (name_exercise_pos[0], name_exercise_pos[1] + (name_exercise_pos[1] / 2) + 80)

# names option size
name_opt_size = (300, 80)

# names option pos
name_opt_pos = (name_text_field_pos[0] + (name_text_field_pos[0] / 2) + 85, name_exercise_pos[1]-(name_exercise_size[1] / 2)+10)

# exit button pos
exit_btn_pos = (width - (exit_btn_size[0] * 2.2), height - 50)
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
fuentes = "resources/fuentes/"
audios = "resources/audios/"

# Number of cotidian pairs
COTIDIAN_PAIRS = len(glob(coditidian_functions+'*'+PNG_EXT))

# Number of name pairs
NAME_PAIRS = len(glob(name_exercises+'*'+PNG_EXT))