# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

## Main Menu ##################################################################
##
## Controla la apariencia de Mwnú Principals

## Configuración de menu princial
define gui.main_menu_logo = "gui/game_logo.png"
define gui.main_menu_logo_position = (0.5, 0.6) 
define gui.main_menu_buttons_spacing = 50 # override del definido en el archivo gui.rpy
define gui.main_menu_version_position = (-20, -20)
define gui.main_menu_copyright_position = (20, -20)

## Estilos de los botones del menu principal
define gui.main_menu_button_font = gui.interface_text_font
define gui.main_menu_button_size = 20
define gui.main_menu_button_color = "#ffffff"
define gui.main_menu_button_outlines = [(2, "#000000cc", 0, 0)]

# Estilos de los textos informativos
define gui.main_menu_info_font = gui.interface_text_font
define gui.main_menu_info_size = 16
define gui.main_menu_info_color = "#ffffff"
define gui.main_menu_info_outlines = [(1, "#000000aa", 0, 0)]

## Configurón de submenus
define gui.submenu_bg = Frame(Solid("#000000B2"),12 ,12) # TODO sustituir Solid por "gui/overlaysubmenu.png"
#define gui.submenu_bg = Frame("gui/overlay/submenu.png", 12, 12)
define gui.submenu_border = "#FFFFFF"
define gui.submenu_buttons = 5
define gui.submenu_spacing = 10
define gui.submenu_button_width = 250
define gui.submenu_button_height = 45
define gui.submenu_padding = (25, 25)
define gui.submenu_yalign = 0.0
define gui.submenu_xoffset = 0

# ?????????
define gui.main_menu_button_hover_color = "#ffd700"


# Configuración de desarrollo
define gui.year = 2025
define gui.developer = "Developer"
define gui.edition = "Estandar" # OPTIONS: [Estandar, Trial, Demo, Premium, Regular, Complete, First Press, Press]
define gui.rated = "All" # OPTIONS: Censored, 18+, 15+, All ages
# TODO: deberia salir del momento de hacer build de juego.
# market # OPTIONS:  Steam, itch.io, None
# platform # OPTIONS: PC, Linux, Macintosh, Windows