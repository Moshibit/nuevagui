# ## Pantalla del menú del juego #################################################
# ##
# ## Esto distribuye la estructura de base del menú del juego. Es llamado con el
# ## título de la pantalla y presenta el fondo, el título y la navegación.
# ##
# ## El parámetro 'scroll' puede ser 'None', "viewport" o "vpgrid". Se usa esta
# ## pantalla con uno o más elementos, que son transcluídos (situados) en su

screen game_menu(title, scroll=None, yinitial=0.0, spacing=0, menu_type=None): #, tooltip=""

    style_prefix "game_menu"

    # --- Fondo del menú ---
    add "gui/gm.png"#TODO: DEBUG: Borrar 
    # TODO cambiar por #add gui.game_menu_background

    vbox:
        
        frame: # 1. Cabecera (Header) -----------------------------------------
            
            ysize int(config.screen_height * 0.1)
            xfill True
            
            background Transform(
                Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile),
                alpha=0.7) # TODO: DEBUG Borrar o cambiar el bg, temporal
            
            has hbox
            xfill True
            yalign 0.5
            

            label "★ " + title + " ★": # --- Título (esquina superior izquierda) # --> "★ [title] ★":
                xalign 0.0
                xoffset 40
            
            hbox: # --- Barra de menús principal (esquina superiror derecha)
                xalign 1.0
                spacing 20
                xoffset -40
                # style "game_menu_header_buttons"

                # --- Mostramos los botones según el tipo de menú ---
                if menu_type == "game":
                    textbutton _("Opciones") action ShowMenu("preferences")
                    textbutton _("Guardar") action ShowMenu("save")
                    textbutton _("Cargar") action ShowMenu("load")
                    
                    # textbutton _("Adultos") action ShowMenu("adult_options") # TODO: poner como submenu de preferences, TODO: controlar con persistente.
                    # graficos y video opciones con contro G y contro A
                
                elif menu_type == "extras": 
                    textbutton _("Sprites") action ShowMenu("sprites")
                    textbutton _("Galería") action ShowMenu("gallery")
                    textbutton _("Música") action ShowMenu("music_room")
                    textbutton _("Escenas") action ShowMenu("scenes")
                    # TODO: agregar mas
                
                elif menu_type == "in_game": 
                    textbutton _("Stats") action ShowMenu("stats")
                    textbutton _("Misiones") action ShowMenu("quests")
                    textbutton _("Codex") action ShowMenu("codex")
                    textbutton _("Guía") action ShowMenu("game_guide")
                    # TODO: agregar mas (opciones del gameplay)

                elif menu_type == "help":
                    textbutton _("Accesivilidad") action NullAction() #ShowMenu() # TODO: hacerfuncionar
                    textbutton _("Idioma") action NullAction() #ShowMenu() # TODO: hacerfuncionar
                    textbutton _("Acerca de") action ShowMenu("about")
                    textbutton _("Ayuda") action Help()


        frame: # 2. Área de contenido principal (Body) ------------------------
            ysize int(config.screen_height * 0.8)
            xfill True
            background Transform(
                Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile),
                alpha=0.7) # TODO: DEBUG Borrar o ccambiar el bg, temporal
            # style "game_menu_content_frame"
            
            # --- Elige el tipo de scroll ----
            if scroll == "viewport":
                viewport:
                    id "viewport"
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True

                    vbox:
                        spacing spacing
                        transclude

            elif scroll == "vpgrid":
                vpgrid:
                    cols 1
                    yinitial yinitial
                    scrollbars "vertical"
                    mousewheel True
                    draggable True
                    pagekeys True
                    side_yfill True

                    spacing spacing
                    transclude

            else:
                transclude


        # 3. Pie de página (Footer) -------------------------------------------
        frame:
            ysize int(config.screen_height * 0.1)
            xfill True
            background Transform(
                Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile),
                alpha=0.7) # TODO DEBUG: Borrar este background


            has hbox
            xfill True
            yalign 0.5

            hbox: # --- Tooltip (esquina inferior izquierda)
                xalign 0.0
                xoffset 40
                spacing 5

                text _("Ayuda: ")
                text "demo de tooltip" # TODO: eliminar la linea y poner el tooltip de abajo
                # text tooltip #: # TODO: agregar tooltips y remplazar por la linea de arriba
                    # style "game_menu_tooltip"
                    
            
            hbox: # --- Botones de acción (esquina inferior derecha)
                xalign 1.0
                xoffset -40
                spacing 40
                # style "game_menu_footer_buttons"
                
                textbutton _("Salir") action Quit(confirm=not main_menu)
                if not main_menu:
                    textbutton _("Menú Principal") action MainMenu()
                textbutton _("Volver") action Return()


    # Atajo de teclado para el menú principal
    if main_menu:
        key "game_menu" action ShowMenu("main_menu")
        # TODO: else reggresar o cerrar ventana (parece que  ya está)

## Estilos para la nueva estructura ############################################

# Estilos para la cabecera
style game_menu_title:
    size 36
    color gui.accent_color
    bold True
    outlines [(2, "#0008", 0, 0)]

style game_menu_header_buttons:
    spacing 30

style game_menu_header_buttons_text:
    size 22

# Estilos para el contenido
style game_menu_content_frame:
    #background "#0003"  # Fondo semi-transparente para el área de contenido
    padding (25, 15)
    #margin (50, 0, 50, 0)

# Estilos para el pie de página
style game_menu_tooltip:
    size 16
    color "#CCC"
    italic True

style game_menu_footer_buttons:
    spacing 20

style game_menu_footer_buttons_text:
    size 18
    hover_color gui.hover_color
    selected_color gui.selected_color

# Estilos generales
# style game_menu_viewport:
#     #xsize 1380

style game_menu_vscrollbar:
    unscrollable gui.unscrollable