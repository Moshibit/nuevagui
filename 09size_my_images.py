# -*- coding: utf-8 -*-
# Autor: Erik Juárez Guerrero

from PIL import Image
import os

def get_file_list():
    path = os.getcwd()
    f_list = [ ]
    for dir_name, sub_dir, file_list in os.walk(path):
        #print("directorio encontrado: %s" % dir_name)
        
        for file_name in file_list:
            name, ext = os.path.splitext(file_name)
            if ext == ".png":
                f_list.append(file_name)
            
    return f_list

def loadImg(fn):
    im = None
    try:
        
        im = Image.open(fn)
    except FileNotFoundError:
        print("No se pudo abrir la imagen:", fn)
    finally:
        return im

def generate_name(fn):
    s = fn.split('.')
    ext = "." + s.pop()
    s = ".".join(s)
    s = "modified_" + s + ext
    return s


def main():
    fl = get_file_list()
    SIZE = (600, 600)
    
    for fn in fl:
        print(fn)
        im = loadImg(fn)
        im.thumbnail(SIZE)
        #s = generate_name(fn)
        im.save(fn)

if __name__ == "__main__":
    main()