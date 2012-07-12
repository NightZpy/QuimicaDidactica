import os
PNG_EXT = '.png'
def change_file_name():
    path = '.'
    chars = 'abcdefghijklmnopqrstuvwxyz'.upper()
    n_chars = len(chars)
    print "Lista: ".format(os.listdir(path))
    for fn in os.listdir(path):
        for i in range(n_chars):
            file = 'Letra '+chars[i]+' 2'+PNG_EXT
            print "File: "+file
            if fn == file:
                name=chars[i].lower()+'_pressed'+PNG_EXT
                os.rename(fn,name)
                break
            
change_file_name()
