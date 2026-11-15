################################################################################
## Inicialización
################################################################################

init offset = -1


################################################################################
## Estilos
################################################################################

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize gui.bar_size
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)

################################################################################
## [*] Estilos propios
################################################################################ 

# style emoji:
#     emoji_font "EmojiTwoCOLRv0.ttf"


################################################################################
## Pantallas internas del juego
################################################################################


## Pantalla de diálogo #########################################################
##
## La pantalla de diálogo muestra el diálogo al jugador. Acepta dos parámetros,
## 'who' y 'what', es decir, el nombre del personaje que habla y el texto que ha
## de ser mostrado respectivamente. (El parámetro 'who' puede ser 'None' si no
## se da ningún nombre.)
##
## Esta pantalla debe crear un texto 'displayable' con id "what" que Ren'Py usa
## para gestionar la visualización del texto. Puede crear también 'displayables'
## con id "who" y id "window" para aplicar propiedades de estilo.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"


    ## Si hay una imagen lateral, se muéstra encima del texto. No la muestra en
    ## la variante de teléfono - no hay espacio.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Permite que el 'namebox' pueda ser estilizado en el objeto 'Character'.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")

    xpos gui.dialogue_xpos
    xsize gui.dialogue_width
    ypos gui.dialogue_ypos

    adjust_spacing False

## Pantalla de introducción de texto ###########################################
##
## Pantalla usada para visualizar 'renpy.input'. El parámetro 'prompt' se usa
## para pasar el texto presentado.
##
## Esta pantalla debe crear un 'displayable' 'input' con id "input" para aceptar
## diversos parámetros de entrada.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xanchor gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Pantalla de decisiones ######################################################
##
## Esta pantalla presenta las decisiones dentro del juego de la sentencia
## 'menu'. El parámetro único, 'items', es una lista de objetos, cada uno con
## los campos 'caption' y 'action'.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox:
        for i in items:
            textbutton i.caption action i.action


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    ypos 405
    yanchor 0.5

    spacing gui.choice_spacing

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.text_properties("choice_button")


## Pantalla de menú rápido #####################################################
##
## El menú rápido se muestra en el juego para ofrecer fácil acceso a los menús
## externos al juego.

screen quick_menu():

    ## Asegura que esto aparezca en la parte superior de otras pantallas.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            style "quick_menu"

            textbutton _("Atrás") action Rollback()
            textbutton _("Historial") action ShowMenu('history')
            textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Guardar") action ShowMenu('save')
            textbutton _("Guardar R.") action QuickSave()
            textbutton _("Cargar R.") action QuickLoad()
            textbutton _("Ajustes") action ShowMenu('preferences')


## Este código asegura que la pantalla 'quick_menu' se muestra en el juego,
## mientras el jugador no haya escondido explícitamente la interfaz.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_menu is hbox
style quick_button is default
style quick_button_text is button_text

style quick_menu:
    xalign 0.5
    yalign 1.0

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.text_properties("quick_button")


################################################################################
## Pantallas del menú principal y del menú del juego
################################################################################

## Pantalla de navegación ######################################################
##
## Esta pantalla está incluida en el menú principal y los menús del juego y
## ofrece navegación a los otros menús y al inicio del juego.

screen navigation():

    vbox:
        style_prefix "navigation"

        xpos gui.navigation_xpos
        yalign 0.5

        spacing gui.navigation_spacing

        if main_menu:

            textbutton _("Comenzar") action Start()

        else:

            textbutton _("Historial") action ShowMenu("history")

            textbutton _("Guardar") action ShowMenu("save")

        textbutton _("Cargar") action ShowMenu("load")

        textbutton _("Ajustes") action ShowMenu("preferences")

        if _in_replay:

            textbutton _("Finaliza repetición") action EndReplay(confirm=True)

        elif not main_menu:

            textbutton _("Menú principal") action MainMenu()

        textbutton _("Acerca de") action ShowMenu("about")

        if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

            ## La ayuda no es necesaria ni relevante en dispositivos móviles.
            textbutton _("Ayuda") action ShowMenu("help")

        if renpy.variant("pc"):

            ## El botón de salida está prohibido en iOS y no es necesario en
            ## Android y Web.
            textbutton _("Salir") action Quit(confirm=not main_menu)


style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")

style navigation_button_text:
    properties gui.text_properties("navigation_button")


## Pantalla del menú principal #################################################
##
## Usado para mostrar el menú principal cuando Ren'Py arranca.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

# screen main_menu():

#     ## Esto asegura que cualquier otra pantalla de menu es remplazada.
#     tag menu

#     add gui.main_menu_background

#     ## Este marco vacío oscurece el menu principal.
#     frame:
#         style "main_menu_frame"

#     ## La sentencia 'use' incluye otra pantalla dentro de esta. El contenido
#     ## real del menú principal está en la pantalla de navegación.
#     use navigation

#     if gui.show_name:

#         vbox:
#             style "main_menu_vbox"

#             text "[config.name!t]":
#                 style "main_menu_title"

#             text "[config.version]":
#                 style "main_menu_version"


# style main_menu_frame is empty
# style main_menu_vbox is vbox
# style main_menu_text is gui_text
# style main_menu_title is main_menu_text
# style main_menu_version is main_menu_text

# style main_menu_frame:
#     xsize 420
#     yfill True

#     background "gui/overlay/main_menu.png"

# style main_menu_vbox:
#     xalign 1.0
#     xoffset -30
#     xmaximum 1200
#     yalign 1.0
#     yoffset -30

# style main_menu_text:
#     properties gui.text_properties("main_menu", accent=True)

# style main_menu_title:
#     properties gui.text_properties("title")

# style main_menu_version:
#     properties gui.text_properties("version")


screen main_menu():
    style_prefix "main_menu" # [*]

    ## TODO: hacer que el main menu muestre algo si permanece idle

    ## Esto asegura que cualquier otra pantalla de menu es remplazada.
    tag menu

    ## Fondo del menú [*]
    add gui.main_menu_background
    # TODO cambiar de momento sera un place holder
    # TODO: hacer un image button que mande a una web

    ## [*] Logo del juego
    add gui.main_menu_logo:
        xalign gui.main_menu_logo_xaling
        ypos gui.main_menu_logo_ypos

    ## Este marco vacío oscurece el menu principal.
    # frame:
    #     style "main_menu_frame"

    ## La sentencia 'use' incluye otra pantalla dentro de esta. El contenido
    ## real del menú principal está en la pantalla de navegación.
    # use navigation

    ## [*] Botones principales del menú
    if gui.main_menu_navi_orientation == "horizontal":
        hbox:
            style_prefix "navi"
            style "navi_horizontal"
            use navi_content

    else: # Si el menú es vertical
        ## Este marco vacío oscurece el menu principal.
        frame:
            style "main_menu_frame"
        
        vbox:
            style_prefix "navi"
            style "navi_vertical"
            use navi_content


    # Botones superiores [*]
    hbox:
        style_prefix "top_buttons"

        imagebutton:
            auto "gui/button/mmabout_%s.png"
            action ShowMenu("about")

        imagebutton:
            auto "gui/button/mmlanguage_%s.png"
            action NullAction() #ShowMenu("language") # TODO: hacer funcionar

        imagebutton:
            auto "gui/button/mmaccesibility_%s.png"
            action NullAction() # ShowMenu("accesibility") # TODO: hacer funcionar

    # if gui.show_name:

    #     vbox:
    #         style "main_menu_vbox"

    #         text "[config.name!t]":
    #             style "main_menu_title"

    #         text "[config.version]":
    #             style "main_menu_version"

    ## Información del juego [*] 
    if gui.show_name:
        frame:  # Copyright (inferior izquierda)
            style_prefix "main_menu_copyfooter"
            
            hbox: 
                style_prefix "main_menu_footer"
                # text "© ":
                #     style "main_menu_footer_emoji"
                text _("© [build.developer] [build.year]. Todos los derechos reservados.")

        frame: # Versión (inferior derecha)
            style_prefix "main_menu_versionfooter"

            vbox: 
                style_prefix "main_menu_footer"

                if gui.show_name:
                    text "[config.name!t]"
                    text _("versión: [config.version]")
                    ## Muestra información si es relevante
                    if build.edition != "standar":
                        text _("edición: [build.edition]")
                    if build.rated != "all":
                        text _("clasificación: [build.rated]")
                    if build.platform != "multiplataform":
                        text _("plataforma: [build.platform]")
                    if build.market != "general":
                        text _("distribución: [build.market]")
                    if build.developer:
                        text _("Modo desarrollor"):
                            color "#ff0000"

    ## Información del juego [*] 


## Estilos del menú princiapal [*]
style main_menu_frame is empty
# style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
# style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 420
    yfill True

    background "gui/overlay/main_menu.png"

# style main_menu_vbox:
#     xalign 1.0
#     xoffset -30
#     xmaximum 1200
#     yalign 1.0
#     yoffset -30

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

# style main_menu_version:
#     properties gui.text_properties("version")

## [*] Estilos añadidos
# --- Información del juego

style main_menu_copyfooter_frame:
    background Solid("#333a")
    xalign 0.0
    xoffset 20
    yalign 1.0
    yoffset -20

style main_menu_versionfooter_frame:
    background Solid("#333a")
    xalign 1.0
    xoffset -20
    yalign 1.0
    yoffset -20

style main_menu_footer_text is main_menu_text:
    properties gui.text_properties("footer")

style main_menu_footer_emoji is emoji:
    take main_menu_footer_text
    # outlines [ ]
    
style main_menu_footer_vbox is vbox:
    box_align 1.0


style main_menu_footer_hbox is hbox

## --- Botones superiores
style top_buttons_hbox:
    xalign 1.0
    xoffset -20
    ypos 20 
    spacing 10

## --- Navegación principal ---
style navi_button is gui_button
style navi_button_text is gui_button_text

style navi_button:
    size_group "navi"
    properties gui.button_properties("navi_button")

style navi_button_text:
    properties gui.text_properties("navi_button")


style navi_horizontal is hbox:
    xalign gui.main_menu_navi_hposition[0]
    yalign gui.main_menu_navi_hposition[1]
    spacing gui.navi_buttons_hspacing

style navi_vertical is vbox:
    xalign gui.main_menu_navi_vposition[0]
    yalign gui.main_menu_navi_vposition[1]
    spacing gui.navi_buttons_vspacing

style navi_vbox is vbox:
    xalign 0.5
    spacing 5

style navi_text is main_menu_text:
    properties gui.text_properties("navi_button")
    xalign 0.5


# === Pantallas Auxiliares ===
screen navi_content(): # --- Contenido del navi ---
    vbox: # Iniciar
        # imagebutton:
        #     auto "gui/button/mmplay_%s.png"
        #     action If(persistent.first_run, Start(), Show("submenu_screen"))
        textbutton "⭐ " + _("Jugar"):
            background "#00ff00"
            action If(persistent.first_run, Start(), Show("submenu_screen"))
    vbox: # Opciones
        # imagebutton:
        #     auto "gui/button/mmoptions_%s.png"
        #     action ShowMenu("preferences")
        
        textbutton _("⚙️ Ajustes") action ShowMenu("preferences") background "#00ff00"
    vbox: # Extras
        # imagebutton:
        #     auto "gui/button/mmextras_%s.png"
        #     action ShowMenu("extras")
        textbutton _("🎁 Extras") action ShowMenu("extras") background "#00ff00"
    #vbox: # Salir
        # imagebutton:
        #     auto "gui/button/mmexit_%s.png"
        #     action Quit()
    textbutton _("🚪 Salir") action Quit() background "#00ff00"
    
    
    
    # frame:
    #     background Solid("#00f")
    # button:
    #     idle_background Solid("#f00")
    #     hover_background Solid("#0f0")
    #     action Notify("text completado")
    #     vbox:
    #         add "gui/button/mmexit_idle.png"
    #         text "Hola"



#       ## TODO agregar un boton para sideStories. oculto[debe ser oculto y no desvanecido]  solos al finalizar el juegon
#       ##      o cambiar el comportamiento de del boton para mostrar un selector de historias.


### temporal
style mybutton_textbutton:
    background "#00ff00"


screen submenu_screen: # --- Submenús ---
    # TODO: hacer que sea una pantalla completa y no una ventana flotante.
    #       poner boton de return para regresar al mine menu. 
    #       eliminar el zorder y añadir tag menu, quitar el close layer
    # NOTE: persistene.end_game, persistent.unlocked_routes y 
    #       persistent.after_story_unlocked deben definirse = True 
    #       en algun lugar del script de juego

    zorder 100

    button:
        style "close_layer"
        action Hide()

    frame:
        modal True
        style_prefix "submenu"

        hbox:
            vbox: # Inicio
                label _("Menú de inicio")
                textbutton "▶ " + _("Nueva partida") action Start()
                if persistent.end_game:
                    textbutton "➕ " + _("Nueva partida +") action Start("new_game_plus")
                if persistent.unlocked_routes:
                    textbutton "🔀 " + _("Selector de Rutas") action [ShowMenu("route_selector"), Hide("submenu_screen")]
                if persistent.after_story_unlocked:
                    textbutton "💞 " + _("After Stories") action [ShowMenu("after_selector"), Hide("submenu_screen")]
                    
            vbox: # Carga
                label _("Menú de carga")
                if renpy.can_load("quitsave"):
                    textbutton "💾 " + _("Reanudar") action FileLoad("quitsave", slot=True) #reanuda desde el punto en que se salio
                textbutton "📌 " + _("Continuar") action Continue(regexp=r'\d',confirm=False) #[r'\d+',]       aparte # reanuda desde el ultimo archivo salvado(o eso se supone que hace)
                textbutton "➡️ " + _("Cargar partida") action [ShowMenu("load"), Hide("submenu_screen")]

    key "game_menu" action Hide("submenu_screen")

## --- capa de cierre ---
style close_layer:
    area (0, 0, config.screen_width, config.screen_height)
    background "#000000aa"

## --- Submenus ---
style submenu_frame is frame:
    
    xalign 0.5
    yalign 0.5
    padding gui.submenu_padding
    
style submenu_hbox is hbox:
    spacing gui.submenu_hspacing

style submenu_vbox is vbox:
    #box_align 10.0
    spacing gui.submenu_vspacing

style submenu_text is gui_text:
    size gui.submenu_button_text_size

style submenu_button is gui_button

style submenu_button_text is gui_button_text:
    properties gui.text_properties("submenu_button")


# [*] experimental
# screen my_iconbutton(icon, caption=None): #, **properties
#     #$ icon_properties, text_properties, button_properties = renpy.split_properties(properties, "icon_", "text_", "")

#     button:
#         #style "iconbutton"
#         #properties button_properties

#         if caption:
#             text caption #style "iconbutton_text" properties text_properties

#         #icon icon style "iconbutton_icon" properties icon_properties
#         add icon 

# TODO: ver como mandar a la pantalla de opciones de video que se accdeder por SHIFT + G
# TODO: mandar el boton de accecibilidad top button a la pantallas de accecibilidad SHIFT + A.
# TODO: o acrear esa pantalla basandose en la de shift + A

# ========================================================================
# Contenido de la Historia y Galería

#     Galería de Imágenes (CG Gallery): Esta es casi un must-have. Permite a los jugadores revisar todas las imágenes y escenas especiales (CGs) que han desbloqueado durante el juego. Es ideal que se puedan ver en pantalla completa.
#     Galería de Sprites/Personajes: Muestra los diferentes sprites (ilustraciones de los personajes) con sus variaciones de expresiones y atuendos. Puede incluir biografías o perfiles cortos de cada personaje.
#     Revisor de Escenas (Scene Replay/Memories): Permite a los jugadores revivir escenas específicas de la historia que ya hayan desbloqueado, especialmente útil para ver las ramificaciones de la trama o momentos favoritos.
#     Diccionario/Glosario: Si tu VN tiene terminología compleja, nombres de lugares o conceptos únicos, un glosario es invaluable para que los jugadores puedan consultarlos.
#     Árbol de Rutas/Progreso (Route Map/Flowchart): Muy útil para VN con múltiples rutas y finales. Muestra visualmente las decisiones tomadas y las rutas desbloqueadas, ayudando a los jugadores a encontrar los finales que les faltan.
#     Finales Desbloqueados (Endings List): Una lista sencilla de todos los finales que el jugador ha conseguido, y quizás pistas sutiles sobre los que faltan.

# Multimedia y Sonido

#     Jukebox/Galería de Música (Music Gallery): Permite escuchar todas las pistas de la banda sonora del juego. Ideal si se pueden ver los nombres de las canciones y del compositor.
#     Galería de Voces (Voice Gallery): Si tu VN tiene voces, esta opción permite escuchar las líneas de diálogo de los personajes, a menudo organizadas por personaje o por escena.
#     Videos/Cortos Animados ( si aplica): Si tu VN tiene secuencias animadas o videos promocionales, este es el lugar para que los jugadores los revisen.

# Material Adicional y Coleccionables

#     Concept Art/Bocetos: Muestra arte conceptual, diseños tempranos de personajes o escenarios, y notas de los desarrolladores.
#     Material de Desarrollo/Comentarios del Equipo: Un apartado donde los desarrolladores pueden compartir anécdotas, decisiones de diseño o curiosidades sobre la creación del juego.
#     Logros/Premios: Si tienes un sistema de logros internos o integrados con plataformas como Steam, un menú para verlos es una buena adición.
#     Mini-juegos (si aplica): Si incluiste pequeños juegos o rompecabezas dentro de la VN, puedes dar la opción de jugarlos por separado.
#     Arte de Fans/Fan Art (si planeas curarlo): Si tienes una comunidad activa, podrías considerar una galería de arte de fans (con su permiso, claro).

# Recomendaciones para la implementación:

#     Claridad: Asegúrate de que los nombres de las opciones sean claros y descriptivos.
#     Organización: Agrupa las opciones de forma lógica, como en las categorías que te he presentado.
#     Accesibilidad: Que sea fácil navegar por el submenú y acceder a cada sección.
#     Progreso: Muchas opciones, como la galería de CGs o la jukebox, solo deben mostrar contenido que el jugador ya haya "desbloqueado" al avanzar en la historia.
#     Estilo: Mantén la estética de tu VN en el diseño del submenú.

# Al elegir qué incluir, piensa en lo que tus jugadores disfrutarían más después de terminar la historia principal o mientras exploran diferentes rutas. Un buen apartado de "Extras" puede prolongar la vida útil de tu VN y aumentar la satisfacción del jugador.







## Pantalla del menú del juego #################################################
##
## Esto distribuye la estructura básica común de la pantalla de menú del juego.
## Se llama con el título de la pantalla y muestra el fondo, el título y la
## navegación.
##
## El parámetro 'scroll' puede ser 'None', 'viewport' o 'vpgrid'. Se usa esta
## pantalla con uno o más elementos, que son transcluidos (situados) en su
## interior.

# screen game_menu(title, scroll=None, yinitial=0.0, spacing=0):

#     style_prefix "game_menu"

#     if main_menu:
#         add gui.main_menu_background
#     else:
#         add gui.game_menu_background

#     frame:
#         style "game_menu_outer_frame"

#         hbox:

#             ## Reservar espacio para la sección de navegación.
#             frame:
#                 style "game_menu_navigation_frame"

#             frame:
#                 style "game_menu_content_frame"

#                 if scroll == "viewport":

#                     viewport:
#                         yinitial yinitial
#                         scrollbars "vertical"
#                         mousewheel True
#                         draggable True
#                         pagekeys True

#                         side_yfill True

#                         vbox:
#                             spacing spacing

#                             transclude

#                 elif scroll == "vpgrid":

#                     vpgrid:
#                         cols 1
#                         yinitial yinitial

#                         scrollbars "vertical"
#                         mousewheel True
#                         draggable True
#                         pagekeys True

#                         side_yfill True

#                         spacing spacing

#                         transclude

#                 else:

#                     transclude

#     use navigation

#     textbutton _("Volver"):
#         style "return_button"

#         action Return()

#     label title

#     if main_menu:
#         key "game_menu" action ShowMenu("main_menu")


# style game_menu_outer_frame is empty
# style game_menu_navigation_frame is empty
# style game_menu_content_frame is empty
# style game_menu_viewport is gui_viewport
# style game_menu_side is gui_side
# style game_menu_scrollbar is gui_vscrollbar

# style game_menu_label is gui_label
# style game_menu_label_text is gui_label_text

# style return_button is navigation_button
# style return_button_text is navigation_button_text

# style game_menu_outer_frame:
#     bottom_padding 45
#     top_padding 180

#     background "gui/overlay/game_menu.png"

# style game_menu_navigation_frame:
#     xsize 420
#     yfill True

# style game_menu_content_frame:
#     left_margin 60
#     right_margin 30
#     top_margin 15

# style game_menu_viewport:
#     xsize 1380

# style game_menu_vscrollbar:
#     unscrollable gui.unscrollable

# style game_menu_side:
#     spacing 15

# style game_menu_label:
#     xpos 75
#     ysize 180

# style game_menu_label_text:
#     size 75 # gui.title_text_size
#     color gui.accent_color
#     yalign 0.5

# style return_button:
#     xpos gui.navigation_xpos
#     yalign 1.0
#     yoffset -45


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


## Pantalla 'acerca de' ########################################################
##
## Esta pantalla da información sobre los créditos y el copyright del juego y de
## Ren'Py.
##
## No hay nada especial en esta pantalla y por tanto sirve también como ejemplo
## de cómo hacer una pantalla personalizada.

# screen about():

#     tag menu

#     ## Esta sentencia 'use' incluye la pantalla 'game_menu' dentro de esta. El
#     ## elemento 'vbox' se incluye entonces dentro del 'viewport' dentro de la
#     ## pantalla 'game_menu'.
#     use game_menu(_("Acerca de"), scroll="viewport"):

#         style_prefix "about"

#         vbox:

#             label "[config.name!t]"
#             text _("Versión [config.version!t]\n")

#             ## 'gui.about' se ajusta habitualmente en 'options.rpy'.
#             if gui.about:
#                 text "[gui.about!t]\n"

#             text _("Hecho con {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")

screen about():

    tag menu

    ## Esta sentencia 'use' incluye la pantalla 'game_menu' dentro de esta. El
    ## elemento 'vbox' se incluye entonces dentro del 'viewport' al interno de
    ## la pantalla 'game_menu'.
    use game_menu(_("Acerca de"), scroll="viewport", menu_type="help"):

        style_prefix "about"

        vbox:

            label "[config.name!t]"
            text _("Versión [config.version!t]\n")
            text _("Edición [gui.edition] [gui.rated]")
            text _("[gui.platform] [gui.market]\n")

            # TODO: hacer funcionar
            ## DLC instalados
            if gui.dlc:
                text "[gui.dlc]"

            ## 'gui.about' se ajusta habitualmente en 'options.rpy'.
            if gui.about:
                text "[gui.about!t]\n"

            text _("Hecho con {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only].\n\n[renpy.license!t]")




# style about_label is gui_label
# style about_label_text is gui_label_text
# style about_text is gui_text

# style about_label_text:
#     size gui.label_text_size

style about_label is gui_label
style about_label_text is gui_label_text
style about_text is gui_text

style about_label_text:
    size gui.label_text_size

## Pantallas de carga y guardado ###############################################
##
## Estas pantallas permiten al jugador guardar el juego y cargarlo de nuevo.
## Como comparten casi todos los elementos, ambas están implementadas en una
## tercera pantalla: 'file_slots'.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

# screen save():

#     tag menu

#     use file_slots(_("Guardar"))


# screen load():

#     tag menu

#     use file_slots(_("Cargar"))


# screen file_slots(title):

#     default page_name_value = FilePageNameInputValue(pattern=_("Página {}"), auto=_("Guardado automático"), quick=_("Guardado rápido"))

#     use game_menu(title):

#         fixed:

#             ## Esto asegura que 'input' reciba el evento 'enter' antes que
#             ## cualquier botón.
#             order_reverse True

#             ## El nombre de la página se puede editar haciendo clic en un botón.
#             button:
#                 style "page_label"

#                 key_events True
#                 xalign 0.5
#                 action page_name_value.Toggle()

#                 input:
#                     style "page_label_text"
#                     value page_name_value

#             ## La cuadrícula de huecos de guardado.
#             grid gui.file_slot_cols gui.file_slot_rows:
#                 style_prefix "slot"

#                 xalign 0.5
#                 yalign 0.5

#                 spacing gui.slot_spacing

#                 for i in range(gui.file_slot_cols * gui.file_slot_rows):

#                     $ slot = i + 1

#                     button:
#                         action FileAction(slot)

#                         has vbox

#                         add FileScreenshot(slot) xalign 0.5

#                         text FileTime(slot, format=_("{#file_time}%A, %d de %B %Y, %H:%M"), empty=_("ranura vacía")):
#                             style "slot_time_text"

#                         text FileSaveName(slot):
#                             style "slot_name_text"

#                         key "save_delete" action FileDelete(slot)

#             ## Botones de acceso a otras páginas
#             vbox:
#                 style_prefix "page"

#                 xalign 0.5
#                 yalign 1.0

#                 hbox:
#                     xalign 0.5

#                     spacing gui.page_spacing

#                     textbutton _("<") action FilePagePrevious()
#                     key "save_page_prev" action FilePagePrevious()

#                     if config.has_autosave:
#                         textbutton _("{#auto_page}A") action FilePage("auto")

#                     if config.has_quicksave:
#                         textbutton _("{#quick_page}R") action FilePage("quick")

#                     ## range(1, 10) da los números del 1 al 9.
#                     for page in range(1, 10):
#                         textbutton "[page]" action FilePage(page)

#                     textbutton _(">") action FilePageNext()
#                     key "save_page_next" action FilePageNext()

#                 if config.has_sync:
#                     if CurrentScreenName() == "save":
#                         textbutton _("Subir sincronización"):
#                             action UploadSync()
#                             xalign 0.5
#                     else:
#                         textbutton _("Descargar sincronización"):
#                             action DownloadSync()
#                             xalign 0.5


# style page_label is gui_label
# style page_label_text is gui_label_text
# style page_button is gui_button
# style page_button_text is gui_button_text

# style slot_button is gui_button
# style slot_button_text is gui_button_text
# style slot_time_text is slot_button_text
# style slot_name_text is slot_button_text

# style page_label:
#     xpadding 75
#     ypadding 5

# style page_label_text:
#     textalign 0.5
#     layout "subtitle"
#     hover_color gui.hover_color

# style page_button:
#     properties gui.button_properties("page_button")

# style page_button_text:
#     properties gui.text_properties("page_button")

# style slot_button:
#     properties gui.button_properties("slot_button")

# style slot_button_text:
#     properties gui.text_properties("slot_button")


screen save():

    tag menu

    use file_slots(_("Guardar"))


screen load():

    tag menu

    use file_slots(_("Cargar"))


screen file_slots(title):

    default page_name_value = FilePageNameInputValue(pattern=_("Página {}"), auto=_("Grabación automática"), quick=_("Grabación rápida"))

    use game_menu(title, menu_type="game"):

        fixed:

            ## Esto asegura que 'input' recibe el evento 'enter' antes que otros
            ## botones.
            order_reverse True

            ## El nombre de la pagina, se puede editar haciendo clic en el
            ## botón.
            button:
                style "page_label"

                key_events True
                xalign 0.5
                action page_name_value.Toggle()

                input:
                    style "page_label_text"
                    value page_name_value

            ## La cuadrícula de huecos de guardado.
            grid gui.file_slot_cols gui.file_slot_rows:
                style_prefix "slot"

                xalign 0.5
                yalign 0.5

                spacing gui.slot_spacing

                for i in range(gui.file_slot_cols * gui.file_slot_rows):

                    $ slot = i + 1

                    button:
                        action FileAction(slot)

                        has vbox

                        add FileScreenshot(slot) xalign 0.5

                        text FileTime(slot, format=_("{#file_time}%A, %d de %B %Y, %H:%M"), empty=_("vacío")):
                            style "slot_time_text"

                        text FileSaveName(slot):
                            style "slot_name_text"

                        key "save_delete" action FileDelete(slot)

            ## Botones de acceso a otras páginas
            vbox:
                style_prefix "page"

                xalign 0.5
                yalign 1.0

                hbox:
                    xalign 0.5

                    spacing gui.page_spacing

                    textbutton _("<") action FilePagePrevious()
                    key "save_page_prev" action FilePagePrevious()

                    if config.has_autosave:
                        textbutton _("{#auto_page}A") action FilePage("auto")

                    if config.has_quicksave:
                        textbutton _("{#quick_page}R") action FilePage("quick")

                    ## range(1, 10) da los números del 1 al 9.
                    for page in range(1, 10):
                        textbutton "[page]" action FilePage(page)

                    textbutton _(">") action FilePageNext()
                    key "save_page_next" action FilePageNext()

                if config.has_sync:
                    if CurrentScreenName() == "save":
                        textbutton _("Subir Sync"):
                            action UploadSync()
                            xalign 0.5
                    else:
                        textbutton _("Descargar Sync"):
                            action DownloadSync()
                            xalign 0.5


style page_label is gui_label
style page_label_text is gui_label_text
style page_button is gui_button
style page_button_text is gui_button_text

style slot_button is gui_button
style slot_button_text is gui_button_text
style slot_time_text is slot_button_text
style slot_name_text is slot_button_text

style page_label:
    xpadding 75
    ypadding 5
    xalign 0.5

style page_label_text:
    textalign 0.5
    layout "subtitle"
    hover_color gui.hover_color

style page_button:
    properties gui.button_properties("page_button")

style page_button_text:
    properties gui.text_properties("page_button")

style slot_button:
    properties gui.button_properties("slot_button")

style slot_button_text:
    properties gui.text_properties("slot_button")




## Pantalla de preferencias ####################################################
##
## La pantalla de ajustes permite al jugador configurar el juego a su
## gusto.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

# screen preferences():

#     tag menu

#     use game_menu(_("Ajustes"), scroll="viewport"):

#         vbox:

#             hbox:
#                 box_wrap True

#                 if renpy.variant("pc") or renpy.variant("web"):

#                     vbox:
#                         style_prefix "radio"
#                         label _("Pantalla")
#                         textbutton _("Ventana") action Preference("display", "window")
#                         textbutton _("Pantalla completa") action Preference("display", "fullscreen")

#                 vbox:
#                     style_prefix "check"
#                     label _("Saltar")
#                     textbutton _("Texto no visto") action Preference("skip", "toggle")
#                     textbutton _("Después de decisiones") action Preference("after choices", "toggle")
#                     textbutton _("Transiciones") action InvertSelected(Preference("transitions", "toggle"))

#                 ## Aquí se pueden añadir 'vboxes' adicionales del tipo
#                 ## "radio_pref" o "check_pref" para nuevos ajustes.

#             null height (4 * gui.pref_spacing)

#             hbox:
#                 style_prefix "slider"
#                 box_wrap True

#                 vbox:

#                     label _("Velocidad de texto")

#                     bar value Preference("text speed")

#                     label _("Tiempo de avance automático")

#                     bar value Preference("auto-forward time")

#                 vbox:

#                     if config.has_music:
#                         label _("Volumen música")

#                         hbox:
#                             bar value Preference("music volume")

#                     if config.has_sound:

#                         label _("Volumen sonido")

#                         hbox:
#                             bar value Preference("sound volume")

#                             if config.sample_sound:
#                                 textbutton _("Prueba") action Play("sound", config.sample_sound)


#                     if config.has_voice:
#                         label _("Volumen voz")

#                         hbox:
#                             bar value Preference("voice volume")

#                             if config.sample_voice:
#                                 textbutton _("Prueba") action Play("voice", config.sample_voice)

#                     if config.has_music or config.has_sound or config.has_voice:
#                         null height gui.pref_spacing

#                         textbutton _("Silenciar todo"):
#                             action Preference("all mute", "toggle")
#                             style "mute_all_button"


# style pref_label is gui_label
# style pref_label_text is gui_label_text
# style pref_vbox is vbox

# style radio_label is pref_label
# style radio_label_text is pref_label_text
# style radio_button is gui_button
# style radio_button_text is gui_button_text
# style radio_vbox is pref_vbox

# style check_label is pref_label
# style check_label_text is pref_label_text
# style check_button is gui_button
# style check_button_text is gui_button_text
# style check_vbox is pref_vbox

# style slider_label is pref_label
# style slider_label_text is pref_label_text
# style slider_slider is gui_slider
# style slider_button is gui_button
# style slider_button_text is gui_button_text
# style slider_pref_vbox is pref_vbox

# style mute_all_button is check_button
# style mute_all_button_text is check_button_text

# style pref_label:
#     top_margin gui.pref_spacing
#     bottom_margin 3

# style pref_label_text:
#     yalign 1.0

# style pref_vbox:
#     xsize 338

# style radio_vbox:
#     spacing gui.pref_button_spacing

# style radio_button:
#     properties gui.button_properties("radio_button")
#     foreground "gui/button/radio_[prefix_]foreground.png"

# style radio_button_text:
#     properties gui.text_properties("radio_button")

# style check_vbox:
#     spacing gui.pref_button_spacing

# style check_button:
#     properties gui.button_properties("check_button")
#     foreground "gui/button/check_[prefix_]foreground.png"

# style check_button_text:
#     properties gui.text_properties("check_button")

# style slider_slider:
#     xsize 525

# style slider_button:
#     properties gui.button_properties("slider_button")
#     yalign 0.5
#     left_margin 15

# style slider_button_text:
#     properties gui.text_properties("slider_button")

# style slider_vbox:
#     xsize 675



screen preferences():

    tag menu

    default tab = "text"

    use game_menu(_("Opciones"), scroll="viewport", menu_type="game"):

        vbox:
            xpos 50
            ypos 5
            spacing 15
        
            hbox:
                spacing 50


                textbutton _("Gráficos") action SetScreenVariable("tab", "grafics")
                textbutton _("Texto") action SetScreenVariable("tab", "text")
                textbutton _("Audio") action SetScreenVariable("tab", "audio")
                textbutton _("Voces") action SetScreenVariable("tab", "voice")
                textbutton _("Salvar/Cargar") action SetScreenVariable("tab", "save_load")
                # if GamepadExists(): # TODO añadir las variables persistent del dlc adult
                #     textbutton _("Adulto") action SetScreenVariable("device", "adult")

                # TODO: tabs y subtabas que se haran en otro lado del script.
                # graficos, texto, audio, voces, guardado/cargado, dlc18plues
                # en otro lado accesivilidad, / idioma / about , contactos , creditos, licencias / controles, atajos, ayuds y consejos de visual novels 
                # extras etc etc etc etc
                # enotro otro lado opciones sobre el gameplay y no sobre modo vn

            hbox:
                
                if tab == "grafics":
                    use grafics_opt
                elif tab == "text":
                    use text_opt
                elif tab == "audio":
                    use audio_opt
                elif tab == "voice":
                    use voice_opt
                elif tab == "save_load":
                    use save_load_opt
                # elif tab == "adult": # TODO activar esta parte
                #     use adult_opt


# TODO: botones--> on/off, on/neutra/off, radio, check, combo_box, sliders

screen grafics_opt():
        # TODO: feats:
        # * pantalla tamaños ?
        # * Activar / Desactivar particulas
        # * BG del main menu
        # * skin de interface
        # * Anti-aliasing ??
        # * Vsync ??
        # * fps limite  ??
        # * lived2
        # * efectos
        # * flasheos o cambios de colores rapidos (accesibilidad)
        # * temblores (accesibilidad)

    vbox:
        box_wrap True

        if renpy.variant("pc") or renpy.variant("web"):

            vbox:
                style_prefix "radio"
                label _("Pantalla")
                textbutton _("Ventana") action Preference("display", "window")
                textbutton _("Pantalla completa") action Preference("display", "fullscreen")
    
    null width (4 * gui.pref_button_spacing)

    vbox:
        box_wrap True

        text "algo va aquí _G_"
        

screen text_opt():
    # TODO: feats:
    # * tamaño (accesibilidad)
    # * fuentes (accesibilidad)
    # * velocidad
    # * color  -- visto, ya visto, otros? --
    # * opasidad del la ventana de texto
    # * subtitulos(cinematicas) / accesibilidad
    # * saltos y omisiones
    # * saltos de eleccione
    # * saltos de esccenas

    
    vbox:
        box_wrap True

        vbox:
            style_prefix "slider"
            
            
            label _("Veloc. texto")

            bar value Preference("text speed")

            label _("Veloc. autoavance")

            bar value Preference("auto-forward time")

    null width (4 * gui.pref_spacing)


    vbox:
        box_wrap True

        vbox:
            style_prefix "check"
            label _("Saltar")
            textbutton _("Texto no visto") action Preference("skip", "toggle")
            textbutton _("Tras elecciones") action Preference("after choices", "toggle")
            textbutton _("Transiciones") action InvertSelected(Preference("transitions", "toggle"))

        ## Aquí se pueden añadir 'vboxes' adicionales del tipo
        ## "radio_pref" o "check_pref" para nuevas preferencias.






screen audio_opt():
    # TODO: feats:
        # * volume maestro
        # * volumen musica
        # * volumen fsx
        # * volumen ambiental
        # * salida de audio ??
    vbox:
        box_wrap True
        
        vbox:
            style_prefix "slider"
            #box_wrap True

            if config.has_music:
                label _("Volumen música")

                hbox:
                    bar value Preference("music volume")

            if config.has_sound:

                label _("Volumen sonido")

                hbox:
                    bar value Preference("sound volume")

                    if config.sample_sound:
                        textbutton _("Prueba") action Play("sound", config.sample_sound)


            if config.has_voice:
                label _("Volumen voz")

                hbox:
                    bar value Preference("voice volume")

                    if config.sample_voice:
                        textbutton _("Prueba") action Play("voice", config.sample_voice)

            if config.has_music or config.has_sound or config.has_voice:
                null height gui.pref_spacing

                textbutton _("Silenciar todo"):
                    action Preference("all mute", "toggle")
                    style "mute_all_button"

    null width (4 * gui.pref_spacing)

    vbox:
        box_wrap True
        
        text "algo va aquí _A_ 2"

screen voice_opt():

    # TODO : feats:
        # * Volumen de voces
        # * texto a  vox
        #  * opciones de texto y voz
        # * voz del sistema o vocesrandom

    vbox:
        box_wrap True

        text "algo va aquí _V_ 1"

    null width (4 * gui.pref_spacing)


    vbox:
        box_wrap True

        text "algo va aquí _V_ 2"


screen save_load_opt():
    # TODO : feats:
        # * autosave
        # * salvados al salir
        # reanudar automatico
        # preguntas sobre salvar en momentos criticos

    vbox:
        box_wrap True

        text "algo va aquí _S_ 1"

    null width (4 * gui.pref_spacing)

    vbox:
        box_wrap True

        text "algo va aquí _S_ 2"

# 

# OPCIONES DE GAME PLAY # TODO: va en otro lado
# dificultad, tiempo en elecciones, dificultad de puzzles, consejos en puzzles
# indicadores de interaccion en imagemaps
# tutoriales
# confirmaciones dde si o no en promts del sistema
# facilitar u omitir quick time events
# Passwords y desbloqueso
# marcas en las elecciones, ayudas, ya leejidas, 
# reset de persistentes.

# OPCIONES DE accesiblidad # TODO: va en otro lado
# daltonimsmo
# subtitulos
# alto contraste
# indicadores visuales,
# shake
# 

# OPCIONES DE dlc18 # TODO: va en otro lado
# activar des activar contenido
# intensidad
# filtros de contenido


# TODO opciones de partida. una vez por partida
# filtros contenido permitido
# 

# TODO : OPCIONES DE CONTROLES

# TODO IDIOMAS, texto y voz, subtitulos,


# EXTRAS. Galerias, cg, bg, bgm, logros, creditos, replays, developer notes, 
# porcentaje de texto completado, desbloqeable y coleccionables y sus porcentajes, finales 


# BOTON Restaurar por pestaña
# ventana de preview de texto


style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 3

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 338

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.text_properties("check_button")

style slider_slider:
    xsize 525

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 15

style slider_button_text:
    properties gui.text_properties("slider_button")

style slider_vbox:
    xsize 675





## Pantalla de historial #######################################################
##
## Esta pantalla muestra el historial de diálogo al jugador. Aunque no tiene
## nada de especial, sí debe acceder al historial de diálogo almacenado en
## '_history_list'.
##
## https://www.renpy.org/doc/html/history.html

# screen history():

#     tag menu

#     ## Evita la predicción de esta pantalla, que podría ser demasiado grande.
#     predict False

#     # TODO: sacar el USE
#     use game_menu(_("Historial"), scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0, spacing=gui.history_spacing):

#         style_prefix "history"

#         for h in _history_list:

#             window:

#                 ## Esto distribuye los elementos apropiadamente si
#                 ## 'history_height' es 'None'.
#                 has fixed:
#                     yfit True

#                 if h.who:

#                     label h.who:
#                         style "history_name"
#                         substitute False

#                         ## Toma el color del texto 'who' de 'Character', si ha
#                         ## sido establecido.
#                         if "color" in h.who_args:
#                             text_color h.who_args["color"]

#                 $ what = renpy.filter_text_tags(h.what, allow=gui.history_allow_tags)
#                 text what:
#                     substitute False

#         if not _history_list:
#             label _("El historial está vacío.")


# ## Esto determina qué etiquetas se permiten en la pantalla de historial.

# define gui.history_allow_tags = { "alt", "noalt", "rt", "rb", "art" }


# style history_window is empty

# style history_name is gui_label
# style history_name_text is gui_label_text
# style history_text is gui_text

# style history_label is gui_label
# style history_label_text is gui_label_text

# style history_window:
#     xfill True
#     ysize gui.history_height

# style history_name:
#     xpos gui.history_name_xpos
#     xanchor gui.history_name_xalign
#     ypos gui.history_name_ypos
#     xsize gui.history_name_width

# style history_name_text:
#     min_width gui.history_name_width
#     textalign gui.history_name_xalign

# style history_text:
#     xpos gui.history_text_xpos
#     ypos gui.history_text_ypos
#     xanchor gui.history_text_xalign
#     xsize gui.history_text_width
#     min_width gui.history_text_width
#     textalign gui.history_text_xalign
#     layout ("subtitle" if gui.history_text_xalign else "tex")

# style history_label:
#     xfill True

# style history_label_text:
#     xalign 0.5


# ## Pantalla de ayuda ###########################################################
# ##
# ## Una pantalla que da información sobre el uso del teclado y el ratón. Usa
# ## otras pantallas con el contenido de la ayuda ('keyboard_help', 'mouse_help',
# ## y 'gamepad_help').

# screen help():

#     tag menu

#     default device = "keyboard"

#     use game_menu(_("Ayuda"), scroll="viewport"):

#         style_prefix "help"

#         vbox:
#             spacing 23

#             hbox:

#                 textbutton _("Teclado") action SetScreenVariable("device", "keyboard")
#                 textbutton _("Ratón") action SetScreenVariable("device", "mouse")

#                 if GamepadExists():
#                     textbutton _("Control") action SetScreenVariable("device", "gamepad")

#             if device == "keyboard":
#                 use keyboard_help
#             elif device == "mouse":
#                 use mouse_help
#             elif device == "gamepad":
#                 use gamepad_help


# screen keyboard_help():

#     hbox:
#         label _("Intro")
#         text _("Avanza el diálogo y activa la interfaz.")

#     hbox:
#         label _("Espacio")
#         text _("Avanza el diálogo sin seleccionar opciones.")

#     hbox:
#         label _("Teclas de flecha")
#         text _("Navega la interfaz.")

#     hbox:
#         label _("Escape")
#         text _("Accede al menú del juego.")

#     hbox:
#         label _("Ctrl")
#         text _("Salta el diálogo mientras se presiona.")

#     hbox:
#         label _("Tabulador")
#         text _("Activa/desactiva el salto de diálogo.")

#     hbox:
#         label _("Av. pág.")
#         text _("Retrocede al diálogo anterior.")

#     hbox:
#         label _("Re. pág.")
#         text _("Avanza hacia el diálogo siguiente.")

#     hbox:
#         label "H"
#         text _("Oculta la interfaz.")

#     hbox:
#         label "S"
#         text _("Captura la pantalla.")

#     hbox:
#         label "V"
#         text _("Activa/desactiva la asistencia por {a=https://www.renpy.org/l/voicing}voz automática{/a}.")

#     hbox:
#         label "Shift+A"
#         text _("Abre el menú de accesibilidad.")


# screen mouse_help():

#     hbox:
#         label _("Clic izquierdo")
#         text _("Avanza el diálogo y activa la interfaz.")

#     hbox:
#         label _("Clic medio")
#         text _("Oculta la interfaz.")

#     hbox:
#         label _("Clic derecho")
#         text _("Accede al menú del juego.")

#     hbox:
#         label _("Rueda del ratón arriba")
#         text _("Retrocede al diálogo anterior.")

#     hbox:
#         label _("Rueda del ratón abajo")
#         text _("Avanza hacia el diálogo siguiente.")


# screen gamepad_help():

#     hbox:
#         label _("Gatillo derecho\nA/Botón inferior")
#         text _("Avanza el diálogo y activa la interfaz.")

#     hbox:
#         label _("Gatillo izquierdo\nBotón sup. frontal izq.")
#         text _("Retrocede al diálogo anterior.")

#     hbox:
#         label _("Botón sup. frontal der.")
#         text _("Avanza hacia el diálogo siguiente.")

#     hbox:
#         label _("D-Pad, Sticks")
#         text _("Navega la interfaz.")

#     hbox:
#         label _("Inicio, Guía, B/Botón Derecho")
#         text _("Accede al menú del juego.")

#     hbox:
#         label _("Y/Botón superior")
#         text _("Oculta la interfaz.")

#     textbutton _("Calibrar") action GamepadCalibrate()


# style help_button is gui_button
# style help_button_text is gui_button_text
# style help_label is gui_label
# style help_label_text is gui_label_text
# style help_text is gui_text

# style help_button:
#     properties gui.button_properties("help_button")
#     xmargin 12

# style help_button_text:
#     properties gui.text_properties("help_button")

# style help_label:
#     xsize 375
#     right_padding 30

# style help_label_text:
#     size gui.text_size
#     xalign 1.0
#     textalign 1.0


screen help():

    tag menu

    default device = "keyboard"

    use game_menu(_("Ayuda"), scroll="viewport", menu_type="help"):

        style_prefix "help"

        vbox:
            spacing 23

            hbox:

                textbutton _("Teclado") action SetScreenVariable("device", "keyboard")
                textbutton _("Ratón") action SetScreenVariable("device", "mouse")

                if GamepadExists():
                    textbutton _("Mando") action SetScreenVariable("device", "gamepad")

            if device == "keyboard":
                use keyboard_help
            elif device == "mouse":
                use mouse_help
            elif device == "gamepad":
                use gamepad_help


screen keyboard_help():

    hbox:
        label _("Intro")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Espacio")
        text _("Avanza el diálogo sin seleccionar opciones.")

    hbox:
        label _("Teclas de flecha")
        text _("Navega la interfaz.")

    hbox:
        label _("Escape")
        text _("Accede al menú del juego.")

    hbox:
        label _("Ctrl")
        text _("Salta el diálogo mientras se presiona.")

    hbox:
        label _("Tabulador")
        text _("Activa/desactiva el salto de diálogo.")

    hbox:
        label _("Av. pág.")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Re. pág.")
        text _("Avanza hacia el diálogo siguiente.")

    hbox:
        label "H"
        text _("Oculta la interfaz.")

    hbox:
        label "S"
        text _("Captura la pantalla.")

    hbox:
        label "V"
        text _("Activa/desactiva la asistencia por {a=https://www.renpy.org/l/voicing}voz-automática{/a}.")

    hbox:
        label "Shift+A"
        text _("Abre el menú de accesibilidad.")


screen mouse_help():

    hbox:
        label _("Clic izquierdo")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Clic medio")
        text _("Oculta la interfaz.")

    hbox:
        label _("Clic derecho")
        text _("Accede al menú del juego.")

    hbox:
        label _("Rueda del ratón arriba")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Rueda del ratón abajo")
        text _("Avanza hacia el diálogo siguiente.")


screen gamepad_help():

    hbox:
        label _("Gatillo derecho\nA/Botón inferior")
        text _("Avanza el diálogo y activa la interfaz.")

    hbox:
        label _("Gatillo izquierdo\nBotón sup. frontal izq.")
        text _("Retrocede al diálogo anterior.")

    hbox:
        label _("Botón sup. frontal der.")
        text _("Avanza hacia el diálogo siguiente.")

    hbox:
        label _("D-Pad, Sticks")
        text _("Navega la interfaz.")

    hbox:
        label _("Inicio, Guía, B/Botón Derecho")
        text _("Accede al menú del juego.")

    hbox:
        label _("Y/Botón superior")
        text _("Oculta la interfaz.")

    textbutton _("Calibrar") action GamepadCalibrate()


style help_button is gui_button
style help_button_text is gui_button_text
style help_label is gui_label
style help_label_text is gui_label_text
style help_text is gui_text

style help_button:
    properties gui.button_properties("help_button")
    xmargin 12

style help_button_text:
    properties gui.text_properties("help_button")

style help_label:
    xsize 375
    right_padding 30

style help_label_text:
    size gui.text_size
    xalign 1.0
    textalign 1.0



################################################################################
## Pantallas adicionales
################################################################################


## Pantalla de confirmación ####################################################
##
## Ren'Py llama la pantalla de confirmación para presentar al jugador preguntas
## de sí o no.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Asegura que otras pantallas no reciban entrada mientras se muestra esta
    ## pantalla.
    modal True

    zorder 200

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 45

            label _(message):
                style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 150

                textbutton _("Sí") action yes_action
                textbutton _("No") action no_action

    ## Clic derecho o escape responden "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    textalign 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.text_properties("confirm_button")


## Pantalla del indicador de salto #############################################
##
## La pantalla de indicador de salto se muestra para indicar que se está
## realizando el salto.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    style_prefix "skip"

    frame:

        hbox:
            spacing 9

            text _("Saltando")

            text "▸" at delayed_blink(0.0, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.2, 1.0) style "skip_triangle"
            text "▸" at delayed_blink(0.4, 1.0) style "skip_triangle"


## Esta transformación provoca el parpadeo de las flechas una tras otra.
transform delayed_blink(delay, cycle):
    alpha 0.5

    pause delay

    block:
        linear 0.2 alpha 1.0
        pause 0.2
        linear 0.2 alpha 0.5
        pause (cycle - 0.4)
        repeat


style skip_frame is empty
style skip_text is gui_text
style skip_triangle is skip_text

style skip_frame:
    ypos gui.skip_ypos
    background Frame("gui/skip.png", gui.skip_frame_borders, tile=gui.frame_tile)
    padding gui.skip_frame_borders.padding

style skip_text:
    size gui.notify_text_size

style skip_triangle:
    ## Es necesario usar un tipo de letra que contenga el glifo BLACK RIGHT-
    ## POINTING SMALL TRIANGLE.
    font "DejaVuSans.ttf"


## Pantalla de notificación ####################################################
##
## La pantalla de notificación muestra al jugador un mensaje. (Por ejemplo, con
## un guardado rápido o una captura de pantalla.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear 0.25 alpha 1.0
    on hide:
        linear 0.5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## Pantalla NVL ################################################################
##
## Esta pantalla se usa para el diálogo y los menús en modo NVL.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Presenta el diálogo en una 'vpgrid' o una 'vbox'.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Presenta el menú, si lo hay. El menú puede ser presentado
        ## incorrectamente si 'config.narrator_menu' está ajustado a 'True'.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## Esto controla el número máximo de entradas en modo NVL que pueden ser
## mostradas de una vez.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    textalign gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    textalign gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    textalign gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.text_properties("nvl_button")


## Pantalla de globos ##########################################################
##
## La pantalla de burbujas se utiliza para mostrar el diálogo al jugador cuando
## se utilizan burbujas de diálogo. La pantalla de burbujas toma los mismos
## parámetros que la pantalla "say", debe crear un visualizable con el id de
## "what", y puede crear visualizables con los ids "namebox", "who", y "window".
##
## https://www.renpy.org/doc/html/bubble.html#bubble-screen

screen bubble(who, what):
    style_prefix "bubble"

    window:
        id "window"

        if who is not None:

            window:
                id "namebox"
                style "bubble_namebox"

                text who:
                    id "who"

        text what:
            id "what"

        default ctc = None
        showif ctc:
            add ctc

style bubble_window is empty
style bubble_namebox is empty
style bubble_who is default
style bubble_what is default

style bubble_window:
    xpadding 30
    top_padding 5
    bottom_padding 5

style bubble_namebox:
    xalign 0.5

style bubble_who:
    xalign 0.5
    textalign 0.5
    color "#000"

style bubble_what:
    align (0.5, 0.5)
    text_align 0.5
    layout "subtitle"
    color "#000"

define bubble.frame = Frame("gui/bubble.png", 55, 55, 55, 95)
define bubble.thoughtframe = Frame("gui/thoughtbubble.png", 55, 55, 55, 55)

define bubble.properties = {
    "bottom_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "bottom_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=1),
        "window_bottom_padding" : 27,
    },

    "top_left" : {
        "window_background" : Transform(bubble.frame, xzoom=1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "top_right" : {
        "window_background" : Transform(bubble.frame, xzoom=-1, yzoom=-1),
        "window_top_padding" : 27,
    },

    "thought" : {
        "window_background" : bubble.thoughtframe,
    }
}

define bubble.expand_area = {
    "bottom_left" : (0, 0, 0, 22),
    "bottom_right" : (0, 0, 0, 22),
    "top_left" : (0, 22, 0, 0),
    "top_right" : (0, 22, 0, 0),
    "thought" : (0, 0, 0, 0),
}



################################################################################
## Variantes móviles
################################################################################

style pref_vbox:
    variant "medium"
    xsize 675

## Como puede que no haya un ratón, reemplazamos el menú rápido con una versión
## que usa menos botones y más grandes, más fáciles de tocar.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:            
            style "quick_menu"
            style_prefix "quick"

            textbutton _("Atrás") action Rollback()
            textbutton _("Saltar") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Auto") action Preference("auto-forward", "toggle")
            textbutton _("Menú") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 510

style game_menu_content_frame:
    variant "small"
    top_margin 0

style game_menu_viewport:
    variant "small"
    xsize 1305
    
style pref_vbox:
    variant "small"
    xsize 600

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_vbox:
    variant "small"
    xsize None

style slider_slider:
    variant "small"
    xsize 900


#####################33###################3
## [*] Personalizados PRopios
###############################3##############3


################################################################################

screen after_selector():
    # TODO: mejorar:
    #       * botones
    #       grid añadir a image butons con texto como sutitulo
    tag menu

    frame:
        style_prefix "submenu"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 25
            label _("After Stories Disponibles")
            
            grid 2 3:  # Ajusta según cuantos afters tengas
                spacing 25
                for story in after_titles:
                    if story in persistent.after_story_unlocked:
                        textbutton "🔓 " + "[after_titles[story]]":
                            action Start(story)
                    else:
                        text "🔒 ? ? ?"
            hbox:
                textbutton _("Regresar") action ShowMenu("main_menu")
                textbutton _("Rutas") action ShowMenu("route_selector")

    key "game_menu" action ShowMenu("main_menu")

# TODO hacer sus propios stilo que no hereden del main menu
# TODO crear su archivo gui




################################################################################
screen route_selector(): 
    # TODO: mejorar:
    #       * botones
    #       grid añadir a image butons con texto como sutitulo
    tag menu

    frame:
        style_prefix "submenu"
        xalign 0.5
        yalign 0.5

        vbox:
            spacing 25
            label _("Seleccionar Ruta")
            
            grid 2 3:  # Ajusta según cuantos afters tengas
                spacing 25
                for route in route_titles:
                    if route in persistent.unlocked_routes:
                        textbutton "🔓 " + "[route_titles[route]]" action Start(route)
                        # hover_sound gui.hover_sound
                        # activate_sound gui.activate_sound
                    else:
                        text "🔒 ? ? ?"
            hbox:
                textbutton _("Regresar") action ShowMenu("main_menu")
                textbutton _("After Stories") action ShowMenu("after_selector")

    key "game_menu" action ShowMenu("main_menu")

# TODO hacer sus propios stilo que no hereden del main menu
# TODO crear su archivo gui.