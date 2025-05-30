## Pantalla del menú principal #################################################
##
## Usado para mostrar el menú principal cuando Ren'Py arranca.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    style_prefix "main_menu"
    tag menu # Esto asegura que cualquier otra pantalla de menú es remplazada.
    #zorder 100

    default start_submenu = False
    default load_submenu = False
    # default ng_plus = False

    ## Fondo del menú ------
    add gui.main_menu_background

    ## Logo del juego (posición configurable) ------
    add gui.main_menu_logo:
        
        xalign gui.main_menu_logo_position[0] 
        ypos gui.main_menu_logo_position[1]

    ## Botones de idioma y accesibilidad ------
    hbox:
        style "top_buttons_hbox"
        # xalign 1.0 xoffset -20 ypos 20 
        # spacing 10

        imagebutton:
            idle "gui/button/mmaccesibility_idle.png"
            hover "gui/button/mmaccesibility_hover.png"
            action ShowMenu("accesibility")

        imagebutton:
            idle "gui/button/mmlanguage_idle.png"
            hover "gui/button/mmlanguage_hover.png"
            action ShowMenu("language")

    ## Botones principales ------
    hbox:
        style_prefix "main_menu_navi"
        xalign 0.5
        yalign 0.92
        spacing 50
        
        #1030*161--> 1133*177        
        vbox:
            imagebutton:
                auto "gui/button/mmplay_%s.png"
                action ToggleScreenVariable("start_submenu", True)
            text _("Iniciar")

        # Cargar
        vbox:
            imagebutton:
                auto "gui/button/mmload_%s.png"
                action ToggleScreenVariable("load_submenu", True)
            text _("Cargar")

        # Opciones
        vbox:
            imagebutton:
                auto "gui/button/mmoptions_%s.png"
                action ShowMenu("preferences")
            text _("Opciones")

        # Extras
        vbox:
            imagebutton:
                auto "gui/button/mmextras_%s.png"
                action ShowMenu("extras")
            text _("Extras")

        # Acerca de
        vbox:
            imagebutton:
                auto "gui/button/mmabout_%s.png"
                action ShowMenu("about")
            text _("Acerca de")

        # Salir
        vbox:
            imagebutton:
                auto "gui/button/mmexit_%s.png"
                action Quit()
            text _("Salir")

    ## Capa de cierre de submenus ------
    if start_submenu or load_submenu:
        button:
            style "close_layer"#area (0, 0, 1, 1) #(0, 0, 1.0, 1.0)
            action [SetScreenVariable("start_submenu",False), SetScreenVariable("load_submenu",False)]

    # Submenú Iniciar ~~~~~~
    if start_submenu:
        #$ btn = renpy.get_widget("main_menu", "btn_iniciar")
        frame:
            style_prefix "submenu"
            #style "submenu_frame"
            #align (0.5, 0.35)
            #padding (35, 35)
            
            vbox:
                #spacing gui.submenu_spacing
                #first_spacing 35
                
                textbutton "▶ " + _("Nueva partida"):
                    action [Start(), Hide("start_submenu")]
                    style "submenu_button"
                if persistent.end_game:
                    textbutton "➕ " + _("Nueva partida +"):
                        action [Start(), Hide("start_submenu")] # TODO: ajustar variable ng_plus en True
                        style "submenu_button"   
                if persistent.ruta_desbloqueada:
                    textbutton "🔀 " + _("Selector de Rutas"):
                        action [ShowMenu("route_selector"), Hide("start_submenu")]
                        style "submenu_button"
                if persistent.after_story_unlocked:
                    textbutton "💞 " + _("After Stories"):
                        action [ShowMenu("after_story_selector"), Hide("start_submenu")]
                        style "submenu_button"


            # NOTE: persistene.end_game, persistent.ruta_desbloqueada y persistent.after_story_unlocked deben definirse = True en algun lugar del script de juego

               
                
        if load_submenu:
            #$ btn = renpy.get_widget("main_menu_navigation", "Cargar")
            frame:
                style "submenu_frame"
                pos (0.5, 0.8)
                has vbox:
                    spacing gui.submenu_spacing

                    textbutton "💾 " + _("Continuar"):
                        action [QuickLoad(), Hide("load_submenu")]
                        style "submenu_button"
                        sensitive FileLoadable(1)
                    
                    textbutton " ➡️ " + _("Cargar partida"):
                        action [ShowMenu("load"), Hide("load_submenu")]
                        style "submenu_button"
                        
            # TODO: usar emticones como bullets

    ## información del juegos -----
    vbox:
        # Copyright (inferior izquierdo)
        style "copyright_vbox"
        text _("© [gui.year] [gui.developer]. Todos los derechos reservados."):
            style "main_menu_textinfo" # XXX

    ## información de versión, edición, clasificación
    vbox:
        # Versión (inferior derecho)
        style "version_vbox"
        
        if gui.show_name:
            text "[config.name!t]":
                style "main_menu_textinfo" # XXX
        text _("versión: [config.version]"):
            style "main_menu_textinfo" # XXX
        text _("edición: [gui.edition]"):
            style "main_menu_textinfo" # XXX
        if gui.rated != "All":
            text _("Clasificación: [gui.rated]"):
                style "main_menu_textinfo" # XXX
        

# Estilos ====
style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_textbutton is main_menu_text
style main_menu_textinfo is main_menu_text

style copyright_vbox is vbox:
    xalign 0.0
    xoffset gui.main_menu_copyright_position[0]
    yalign 1.0
    yoffset gui.main_menu_copyright_position[1]
    xmaximum 900

style version_vbox is vbox:
    xalign 1.0
    xoffset gui.main_menu_version_position[0]
    yalign 1.0
    yoffset gui.main_menu_version_position[1]
    xmaximum 900
    text_align 1.0 #?

style navi_hbox:
    xalign 0.5
    yalign 0.92
    spacing gui.main_menu_buttons_spacing
    #box_align 0.5

style navi_vbox:
    spacing 5
    xalign 0.5

style submenu_vbox:
    spacing gui.submenu_spacing

style top_buttons_hbox:
    xalign 1.0
    pos (20, 20)
    spacing 10

style main_menu_text:
    #properties gui.text_properties("main_menu", accent=True)
    font gui.interface_text_font
    color "#ffffff"
    outlines [(1, "#000000aa", 0, 0)]

style navi_text:
    properties gui.text_properties("button")

style main_menu_textinfo:
    properties gui.text_properties("version")

style navi_text is main_menu_text:
    size gui.main_menu_button_size
    color gui.main_menu_button_color # ojo
    xalign 0.5

style close_layer:
    area (0, 0, 1, 1)

style main_menu_textinfo is main_menu_text:
    # font gui.interface_text_font
    size gui.main_menu_info_size
    xalign 1.0
    color gui.main_menu_info_color
    outlines gui.main_menu_info_outlines
    
style submenu_frame:
    # background gui.submenu_bg 
    #    // 
    # background Frame("gui/overlay/submenu.png", 12, 12)
    padding gui.submenu_padding
    xsize gui.submenu_button_width
    #ysize gui.submenu_button_height
    xalign 0.5
    ypos 0.35

style submenu_button is gui_button:
    xsize gui.submenu_button_width
    #ysize gui.submenu_button_height
    foreground Text("", size=24)  # Para emojis
    #background Solid("#00000000")  # Transparente
    hover_background Frame("gui/button/hover.png", 6, 6)








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