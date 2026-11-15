from PIL import Image
import os

def get_file_list():
    path = os.getcwd()
    f_list = [ ]
    for dir_name, sub_dir, file_list in os.walk(path):
        print("directorio encontrado: %s" % dir_name)
        
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
        
    # para mostrar la imgen
    # img.show()
    
    # para imprimir en pantalla información
    #print("formato:", img.format)
    #print("tamanio:", img.size)
    #print("tipo:", img.mode)

def generate_name(fn):
    s = fn.split('.')
    ext = "." + s.pop()
    s = ".".join(s)
    s = "modified_" + s + ext
    return s
    
def max_crop(f_list):
    left_list = [ ]
    up_list = [ ]
    right_list = [ ]
    down_list = [ ]
    for fn in f_list:
        im = loadImg(fn)
        bb = im.getbbox()
        left_list.append(bb[0])
        up_list.append(bb[1])
        right_list.append(bb[2])
        down_list.append(bb[3])
    return min(left_list), min(up_list), max(right_list), max(down_list)

#def crop(im, region):
#    # tupla pixeles: izquierda, arriba, derecha, abajo
#    return im.crop(region)

#def resize(im, size):
#    # tupla pixeles: ancho, alto
#    return im.thumbnail(size)

#def save(im, fn):
#    im.save(fn)
    
#def get_bounding_box(im):
#    return im.getbbox()

def main():
    fl = get_file_list()
    mi_crop = max_crop(fl)
    for fn in fl:
        im = loadImg(fn)
        im = im.crop(mi_crop)
        #s = generate_name(fn)
        im.save(fn)
        
if __name__ == "__main__":
    main()