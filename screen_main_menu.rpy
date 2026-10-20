################################################################################
## Inicialización
################################################################################

init offset = -1


################################################################################

## Pantalla del menú principal #################################################
##
## Usado para mostrar el menú principal cuando Ren'Py arranca.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

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

        hbox: # Copyright (inferior izquierda)
            style_prefix "main_menu_footer"
            # text "© ":
            #     style "main_menu_footer_emoji"
            text _("© [gui.developer] [gui.year]. Todos los derechos reservados.")

        vbox: # Versión (inferior derecha)
            style_prefix "main_menu_footer"

            if gui.show_name:
                text "[config.name!t]"
                text _("versión: [config.version]")
                ## Muestra información si es relevante
                if gui.edition != "standar":
                    text _("edición: [gui.edition]")
                if gui.rated != "all":
                    text _("clasificación: [gui.rated]")
                if gui.platform != "multiplataform":
                    text _("plataforma: [gui.platform]")
                if gui.market != "general":
                    text _("distribución: [gui.market]")
                if config.developer:
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
style main_menu_footer_text is main_menu_text:
    properties gui.text_properties("footer")

style main_menu_footer_emoji is emoji:
    take main_menu_footer_text
    # outlines [ ]
    
style main_menu_footer_vbox is vbox:
    # box_align 1.0
    xalign 1.0
    xoffset -20
    yalign 1.0
    yoffset -20

style main_menu_footer_hbox is hbox:
    xalign 0.0
    xoffset 20
    yalign 1.0
    yoffset -20

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
        textbutton "⭐ " + _("Iniciar"):
            action If(persistent.first_run, Start(), Show("submenu_screen"))
    vbox: # Opciones
        # imagebutton:
        #     auto "gui/button/mmoptions_%s.png"
        #     action ShowMenu("preferences")
        textbutton _("⚙️ Opciones") action ShowMenu("preferences")
    vbox: # Extras
        # imagebutton:
        #     auto "gui/button/mmextras_%s.png"
        #     action ShowMenu("extras")
        textbutton _("🎁 Extras") action ShowMenu("extras")
    vbox: # Salir
        # imagebutton:
        #     auto "gui/button/mmexit_%s.png"
        #     action Quit()
        textbutton _("🚪 Salir") action Quit()

#       ## TODO agregar un boton para sideStories. oculto[debe ser oculto y no desvanecido]  solos al finalizar el juegon
#       ##      o cambiar el comportamiento de del boton para mostrar un selector de historias.



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


