from distutils.core import setup  
import py2exe  
  
setup(name="Quimica Didactica",  
      version="0.1",  
      description="Quimica Didactica mini-juegos",  
      author="Lenyn Alcantara",  
      author_email="lenin@gmail.com",  
      url="https://github.com/NightZpy/QuimicaDidactica",  
      license="GPL",  
      scripts=["main.py"],  
      windows=["main.py"],
	  #packages = ["buttom", "config", "director", "functional_group", "graphics", "hangman", "line", 
       #     "match", "name", "option", "sce_crucigrama", "sce_functional_group", "sce_hangman", 
        #    "sce_main_menu", "sce_match", "sce_name", "sce_sopa_letras", "sce_winner", "scene", "sce_definitions", "definitions", "page"],
	  includes = ['glob', 'pygame', 'random', 'time', "buttom", "config", "director", "functional_group", "graphics", "hangman", "line", 
            "match", "name", "option", "sce_crucigrama", "sce_functional_group", "sce_hangman", 
            "sce_main_menu", "sce_match", "sce_name", "sce_sopa_letras", "sce_winner", "scene", "sce_crucigrama", "sce_main", "alphabet_soup", "alphabet_soup", "char"]
)