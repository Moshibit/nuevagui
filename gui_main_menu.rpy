## Menú principal y menús del juego ############################################
##
## Controla la apariencia del menú principal y menús del juego

## Configuración Básica
## Imágenes del menú principal y menús del juego.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"

## [*] Logo del juego
define gui.main_menu_logo = "gui/game_logo.png"
# define gui.main_menu_logo_position = (0.5, 0.6) [X]
define gui.main_menu_logo_xaling = 0.5
define gui.main_menu_logo_ypos = 0.6

## [*] Navi
## Estilos de textos del menu principal
define gui.navi_button_text_size = 26
define gui.navi_button_text_xalign = 0.5

## Estilos de textos informativos
define gui.version_text_size = 18
define gui.version_text_outlines = [(1, "#000000aa", 0, 0)]

## Posiciones de texto informativo
define gui.main_menu_version_position = (-20, -20)
define gui.main_menu_copyright_position = (20, -20)

## Estilos de botones principales
define gui.main_menu_navi_orientation = "horizontal" 
# OPTIONS: "horizontal" o "vertical"

define gui.main_menu_navi_hposition = (0.5, 0.9) # (xalign, yalign)
define gui.navi_buttons_hspacing = 30

define gui.main_menu_navi_vposition = (0.05, 0.5) # (xalign, yalign)
define gui.navi_buttons_vspacing = 2

define gui.navi_button_text_size = 26 # [x]
define gui.navi_button_text_xalign = 0.5 # [x]

    ## NOTE: Ejemplos de ajustes recomendados 
    ##                                       position  / spacing
    ##                                 (xalign, yalign)
    ## Horizontal inferior centrado       -> (0.5, 0.9),  30
    ## Horizontal inferiro a la izquierda -> (0.1, 0.9),  30
    ## Horizontal inferiro a la derecha   -> (0.9, 0.9),  30
    ## Vertical centrado                  -> (0.5, 0.5),  30 Hor / 2 Ver
    ## Vertical a la izquierda            -> (0.1, 0.5),  2 
    ## Vertical a la derecha              -> (0.9, 0.5),  2 

## Textos al pie
define gui.footer_text_size = 20
# define gui.footer_text_outlines = [(1, "#000000aa", 0, 0)]

## Submenús
define gui.submenu_hspacing = 30
define gui.submenu_vspacing = 10
define gui.submenu_padding = (25, 25)
define gui.submenu_button_text_size = 24
define gui.submenu_button_text_xalign = 0.0