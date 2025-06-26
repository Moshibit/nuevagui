## Pantalla del menú principal #################################################
##
## Usado para mostrar el menú principal cuando Ren'Py arranca.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    style_prefix "main_menu"
    tag menu

    ## --- Variables de pantalla ---

    ## --- Fondo del menú---
    add gui.main_menu_background

    ## --- Logo del juego (posición configurable) ---
    add gui.main_menu_logo:
        xalign gui.main_menu_logo_position[0] 
        ypos gui.main_menu_logo_position[1]

    ## --- información del juegos ---
    vbox: # Copyright (inferior izquierdo)
        style_prefix "copyright"

        text _("© [gui.year] [gui.developer]. Todos los derechos reservados.")

    vbox: # Versión (inferior derecho)
        style_prefix "version"

        if config.developer:
            text _("Build de desarrollo"):
                style "dev_build_text"
        if gui.show_name:
            text "[config.name!t]"
        text _("versión: [config.version]")
        text _("edición: [gui.edition]")
        if gui.rated != "All":
            text _("Clasificación: [gui.rated]")
        # Mostrar plataforma y mercado si son relevantes
        if gui.platform != "Multiplataform":
            text _("Plataforma: [gui.platform]")
        if gui.market != "General":
            text _("Distribución: [gui.market]")

    ## --- Botones superiores ---
    hbox:
        style_prefix "top_buttons"

        imagebutton:
            auto "gui/button/mmaccesibility_%s.png"
            action ShowMenu("accesibility")

        imagebutton:
            auto "gui/button/mmlanguage_%s.png"
            action ShowMenu("language")

        imagebutton:
            auto "gui/button/mmabout_%s.png"
            action ShowMenu("about")


    ## --- Botones principales ---
    if gui.main_menu_navi_orientation == "horizontal":
        hbox:
            style_prefix "navi"
            style "navi_horizontal"
            use navi_content

    else: # Vertical
        vbox:
            style_prefix "navi"
            style "navi_vertical"
            use navi_content

## === Estilos ===
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text

style navi_button is gui_button
style navi_button_text is gui_button_text

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style navi_button:
    size_group "navi"
    properties gui.button_properties("navi_button")

style navi_button_text:
    properties gui.text_properties("navi_button")


## --- Botones superiores
style top_buttons_hbox:
    xalign 1.0
    xoffset -20
    ypos 20 
    spacing 10

## --- Navegación principal ---
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

## --- Submenus ---
style submenu_frame is frame:
    modal True
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

# --- Información del juego
style version_vbox is vbox:
    xalign 0.0
    xoffset gui.main_menu_version_position[0]
    yalign 1.0
    yoffset gui.main_menu_version_position[1]

style version_text is main_menu_text:
    properties gui.text_properties("version")

style dev_build_text is version_text:
    color "#ff0000"

style copyright_vbox is vbox:
    xalign 1.0
    xoffset gui.main_menu_copyright_position[0]
    yalign 1.0
    yoffset gui.main_menu_copyright_position[1]

style copyright_text is version_text:
    properties gui.text_properties("copyright")
    xalign 1.0 # text_align 0.0


# === Pantallas Auxiliares ===
screen navi_content(): # --- Contenido del navi ---
    vbox: # Iniciar
        imagebutton:
            auto "gui/button/mmplay_%s.png"
            action If(persistent.first_run, Start(), Show("submenu_screen"))
        textbutton _("Iniciar"):
            action If(persistent.first_run, Start(), Show("submenu_screen"))
    vbox: # Opciones
        imagebutton:
            auto "gui/button/mmoptions_%s.png"
            action ShowMenu("preferences")
        textbutton _("Opciones") action ShowMenu("preferences")
    vbox: # Extras
        imagebutton:
            auto "gui/button/mmextras_%s.png"
            action ShowMenu("extras")
        textbutton _("Extras") action ShowMenu("extras")
    vbox: # Salir
        imagebutton:
            auto "gui/button/mmexit_%s.png"
            action Quit()
        textbutton _("Salir") action Quit()


screen submenu_screen: # --- Submenús ---
    # TODO: hacer que sea una pantalla completa y no una ventana flotante.
    #       poner boton de return para regresar al mine menu. 
    #       eliminar el zorder y añadir tag menu, quitar el close layer
    # NOTE: persistene.end_game, persistent.unlocked_routes y 
    #       persistent.after_story_unlocked deben definirse = True 
    #       en algun lugar del script de juego

    zorder 100

    use close_layer

    frame:
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
                    textbutton "💾 " + _("Reanudar") action FileLoad("quitsave", slot=True)
                textbutton "E " + _("Continuar") action Continue(regexp='r"\d"')
                textbutton "➡️ " + _("Cargar partida") action [ShowMenu("load"), Hide("submenu_screen")]


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




################################################################################
## Principal y Pantalla de menu del juego.
################################################################################

## Pantalla del menú principal #################################################
##
## Usado para mostrar el menú principal cuando Ren'Py arranca.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

## TODO: hacer que el main menu muestre algo si permanece idle

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

#     ## Logo del juego
#     # TODO cambiar de momento sera un place holder
#     # TODO: hacer un image button que mande a una web
#     #add gui.game_logo:
#     #    xsize 354 ysize 222 #252*252 o 252*141 o 384*222
#     #    xalign 0.0 yalign 0.0
#     #    xoffset 20 yoffset 20

#     ## información de versión
#     if gui.show_name:

#         vbox:

#             style "main_menu_vbox"

#             text "[config.name!t] [config.version]":
#                 style "main_menu_textinfo" # "main_menu_title"

#             if persistent.adt:
#                 text "18+ Edition":
#                     style "main_menu_textinfo"

#             text "[gui.year] [gui.developer]": # " All Rights Recerved" ## definidos en options.rpy
#                 style "main_menu_textinfo"

#     # Esto invoca una label al pasar el tiempo.
#     timer 45.0 action Start("main_menu_wait")


# style main_menu_frame is empty
# style main_menu_vbox is vbox
# style main_menu_text is gui_text
# style main_menu_title is main_menu_text
# style main_menu_version is main_menu_text
# style main_menu_textinfo is main_menu_version

# style main_menu_frame:
#     xsize 420 # 280<720, 420<1080
#     yfill True

#     background "gui/overlay/main_menu.png"

# style main_menu_vbox:
#     xalign 1.0
#     xoffset -30 #-20<720, -30<1080
#     xmaximum 1200 # 800<720, 1200<1080
#     yalign 1.0
#     yoffset -30 #-20<720, -30<1080

# style main_menu_text:
#     properties gui.text_properties("main_menu", accent=True)

# style main_menu_title:
#     properties gui.text_properties("title")

# style main_menu_version:
#     properties gui.text_properties("version")

# style main_menu_textinfo:
#     size 16 #14


################################################################################
## Principal y Pantalla de menu del juego.
################################################################################

## Pantalla de navegación ######################################################
##
## Esta pantalla está incluída en el menú principal y los menús del juego y
## ofrece navegación a los otros menús y al inicio del juego.

# screen navigation():

#     vbox:
#         style_prefix "navigation"

#         xpos gui.navigation_xpos
#         yalign 0.5

#         spacing gui.navigation_spacing

#         if main_menu:

#             textbutton _("Comenzar") action Start()

#             ## TODO agregar un boton para sideStories. oculto[debe ser oculto y no desvanecido]  solos al finalizar el juegon
#             ##      o cambiar el comportamiento de del boton para mostrar un selector de historias.

#             if renpy.can_load("quitsave"):
#                 textbutton _("Continuar") action FileLoad("quitsave", slot=True)

#         elif _in_replay:

#             textbutton _("Finaliza repetición") action EndReplay(confirm=True)

#         elif not main_menu:

#             textbutton _("Menú principal") action MainMenu()

#         if not main_menu and not _in_replay:

#             textbutton _("Guardar") action ShowMenu("save")

#         if not _in_replay:

#             textbutton _("Cargar") action ShowMenu("load")

#         null height (2 * gui.pref_spacing)

#         textbutton _("Opciones") action ShowMenu("preferences")

#         # if not main_menu:

#             # textbutton _("Historial") action ShowMenu("history") # TODO retirar? si es asi solo comentar

#             #X textbutton _("Estado") action ShowMenu("stats") ## TODO: hacer. quisas mandar al quick menu

#         # if not main_menu:
#         #     textbutton _("Enciclopedia") action ShowMenu("wiki_index") # ubicado en wiki.py

#         if main_menu:

#             textbutton _("Extras") action ShowMenu("navigation_extras") ## TODO: completar menus

#             null height (2 * gui.pref_spacing)

#             textbutton _("Acerca de") action ShowMenu("about")

#         if renpy.variant("pc") or (renpy.variant("web") and not renpy.variant("mobile")):

#             ## La ayuda no es necesaria ni relevante en dispositivos móviles.
#             textbutton _("Ayuda") action ShowMenu("help_s") # original ShowMenu("help") #imagebutton auto "gui/button/help_%s.png" action ShowMenu("help_s")

#             null height (2 * gui.pref_spacing)

#             ## El botón de salida está prohibido en iOS y no es necesario en
#             ## Android y Web.
#             textbutton _("Salir") action Quit(confirm=not main_menu)


# style navigation_button is gui_button
# style navigation_button_text is gui_button_text

# style navigation_button:
#     size_group "navigation"
#     properties gui.button_properties("navigation_button")

#     #idle_background Frame("gui/button/menu_idle_background.png", 12, 12) # TODO este par deberia ser constantes en 01gui.rpy
#     #hover_background Frame("gui/button/menu_hover_background.png", 12, 12)
#     #xpadding 20 #ypadding 10
#     #xmargin 5 ymargin 5

# style navigation_button_text:
#     properties gui.button_text_properties("navigation_button")



################################################################################
## Principal y Pantalla de menu del juego.
################################################################################


## Pantalla del menú del juego #################################################
##
## Esto distribuye la estructura de base del menú del juego. Es llamado con el
## título de la pantalla y presenta el fondo, el título y la navegación.
##
## El parámetro 'scroll' puede ser 'None', "viewport" o "vpgrid". Cuando se usa
## esta pantalla con uno o más elementos, que son transcluídos (situados) en su
## interior.

# screen game_menu(title, scroll=None, yinitial=0.0):

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

#                         transclude

#                 else:

#                     transclude

#     use navigation

#     ## https://patreon.renpy.org/very-old-features.html ------------------------
#     if not main_menu:

#         $ minutes, seconds = divmod(int(renpy.get_game_runtime()), 60)

#         text _("Tiempo de juego:\n[minutes]:[seconds:02d]"):
#             style "gui_text"
#             xpos 44
#             ypos 850 # original 620 # antes 600
#     ## -------------------------------------------------------------------------


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
#     bottom_padding 45 # 30<720, 45<1080
#     top_padding 180 # 120<720, 180<1080

#     background "gui/overlay/game_menu.png"

# style game_menu_navigation_frame:
#     xsize 420 # 280<720, 420<1080
#     yfill True

# style game_menu_content_frame:
#     left_margin 60 # 40<720, 60<1080
#     right_margin 30 # 20<720, 30<1080
#     top_margin 15 # 10<720, 15<1080

# style game_menu_viewport:
#     xsize 1380 # 920<720, 1380<1080

# style game_menu_vscrollbar:
#     unscrollable gui.unscrollable

# style game_menu_side:
#     spacing 15 # 15<720, 15<1080

# style game_menu_label:
#     xpos 75 # 50<720, 75<1080
#     ysize 180 # 120<720, 180<1080

# style game_menu_label_text:
#     size gui.title_text_size
#     color gui.accent_color
#     yalign 0.5

# style return_button:
#     xpos gui.navigation_xpos
#     yalign 1.0
#     yoffset -45 # -30<720, -45<1080