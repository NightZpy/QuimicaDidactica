# -*- encoding: utf-8 -*-


""" Configuracion general del proyecto """

# Nombre
NAME = "Química Didáctica"
EXIT = -1
GAME_OVER = 0
STARTING = 1
NEXT_SCENE = 2
PAUSE = 3

#Scenes constant
MAIN_MENU_SCENE = 'main_menu'
AHORCADO_SCENE = 'main_ahorcado'
PAREO_SCENE = 'main_pareo'
NOMBRAR_SCENE = 'main_nombrar'
CRUCIGRAMA_SCENE = 'main_crucigrama'
SOPA_LETRAS_SCENE = 'main_sopa'
COTIDIAN_FUNCTION_SCENE = 'main_cotidian_function'
DEFINITIONS_SCENE = 'main_definition'

# Rect dict constant for grid in cotidian function game
LTR = 'left_top_rect'
RTR = 'right_top_rect'
LBR = 'left_bottom_rect'
RBR = 'right_bottom_rect'

# Number of cotidian pairs
COTIDIAN_PAIRS = 6

# Number of problems in every cotidian game
NUMBER_COTIDIAN_OPTIONS = 2

SMALL = '_small'
BIG = '_big'
PNG_EXT = '.png'
JPG_EXT = '.jpg'

# Resolution
width = 800
hight = 600

# main menu button size
b_width = 270
b_heigth = 140 

# cotidian option size
c_opt_size = (200, 100)

#init pos for cotidian options
c_opt_pos = (515, 130)

# Directories
sprites = "resources/images/sprites/"
backgrounds = "resources/images/backgrounds/"
buttoms_png = "resources/images/buttoms/png/"
titles = "resources/images/titles/"
menus = "resources/images/menus/"
coditidian_functions = "resources/images/cotidian/function/"
coditidian_types = "resources/images/cotidian/type/"
fuentes = "resources/fuentes/"
audios = "resources/audios/"