# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

## Main Menu Configuration ####################################################
##
## Controla la apariencia de Mwnú Principals

## Configuración Básica
define gui.main_menu_logo = "gui/game_logo.png"
define gui.main_menu_logo_position = (0.5, 0.6) 


## Posiciones de texto informativo
define gui.main_menu_version_position = (-20, -20)
define gui.main_menu_copyright_position = (20, -20)

## Estilos de botones principales
define gui.main_menu_orientation = "horizontal" #OPTIONS: "horizontal" o "vertical"
define gui.main_menu_hposition = (0.5, 0.9) # (xalign, yalign)
define gui.main_menu_buttons_hspacing = 30 # 2
define gui.main_menu_vposition = (0.05, 0.5) # (xalign, yalign)
define gui.main_menu_buttons_vspacing = 2 #
## NOTE: Ejemplos de ajustes recomendados 
## Horizontal centrado inferiro -> position (0.5, 0.9), spacing 30
## Horizontal abajo a la izquierda -> position (0.1, 0.9), spacing 30
## Vertical centrado a la izquierda -> position (0.1, 0.5), spacing 2 
## Centrado -> position (0.5, 0.5) spacing 30 Hor / 2 Ver

## Estilos de textos del menu principal
define gui.main_menu_text_color = "#ffffff"
define gui.main_menu_text_outlines = [(2, "#000000cc", 0, 0)]
define gui.main_menu_button_size = 20

## Estilos de textos informativos
define gui.main_menu_info_size = 16
define gui.main_menu_info_outlines = [(1, "#000000aa", 0, 0)]

## Configuración de submenús
define gui.submenu_bg = Frame("gui/overlay/submenu.png", 12, 12)  # TODO: Crear este asset
define gui.submenu_button_hover_bg = Frame("gui/button/hover.png", 6, 6)
define gui.submenu_spacing = 10
define gui.submenu_button_width = 250
define gui.submenu_button_height = 45
define gui.submenu_padding = (25, 25)
define gui.submenu_button_text_size = 18

## Variables de build (TEMPORAL - mover a build.rpy) ##
define gui.year = 2025
define gui.developer = "Developer"
define gui.edition = "Estandar" # OPTIONS: [Estandar, Trial, Demo, Premium, Regular, Complete, First Press, Press, Desarrollo]
define gui.rated = "All"  # OPTIONS: Censored, 18+, 15+, All ages
# market # OPTIONS:  Steam, itch.io, None
# platform # OPTIONS: PC, Linux, Macintosh, Windows

# TODO: esta sección deberia ser creada en un rpy al momento de hacer build de juego. 
# esta información quizas deberia estar en un documento build.rpy en un storage build.variable en lugar del storage gui.variable


