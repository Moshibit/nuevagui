## Pantalla del menú principal #################################################
##
## Usado para mostrar el menú principal cuando Ren'Py arranca.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    style_prefix "main_menu"
    tag menu

    ## --- Variables de pantalla ---
    default start_submenu = False
    default load_submenu = False

    ## --- Fondo del menú---
    add gui.main_menu_background

    ## --- Logo del juego (posición configurable) ---
    add gui.main_menu_logo:
        xalign gui.main_menu_logo_position[0] 
        ypos gui.main_menu_logo_position[1]


    ## --- Botones superiores ---
    hbox:
        style_prefix "navi"
        style "top_buttons"

        imagebutton:
            idle "gui/button/mmaccesibility_idle.png"
            hover "gui/button/mmaccesibility_hover.png"
            action ShowMenu("accesibility")

        imagebutton:
            idle "gui/button/mmlanguage_idle.png"
            hover "gui/button/mmlanguage_hover.png"
            action ShowMenu("language")


    ## --- Botones principales ---
    hbox:
        style_prefix "navi"
        #style "navi_hbox"

        vbox: # Iniciar
            imagebutton:
                auto "gui/button/mmplay_%s.png"
                action If(persistent.first_run, Start(), ToggleScreenVariable("start_submenu", True))
            text _("Iniciar")
            #style "navi_vbox"
        vbox: # Cargar
            imagebutton:
                auto "gui/button/mmload_%s.png"
                action ToggleScreenVariable("load_submenu", True)
                sensitive not persistent.first_run
            text _("Cargar")
        vbox: # Opciones
            imagebutton:
                auto "gui/button/mmoptions_%s.png"
                action ShowMenu("preferences")
            text _("Opciones")
        vbox: # Extras
            imagebutton:
                auto "gui/button/mmextras_%s.png"
                action ShowMenu("extras")
            text _("Extras")
        vbox: # Acerca de
            imagebutton:
                auto "gui/button/mmabout_%s.png"
                action ShowMenu("about")
            text _("Acerca de")
        vbox: # Salir
            imagebutton:
                auto "gui/button/mmexit_%s.png"
                action Quit()
            text _("Salir")


    ## --- Capa de cierre de submenus ---
    if start_submenu or load_submenu:
        button:
            style "close_layer"
            action [SetScreenVariable("start_submenu",False), SetScreenVariable("load_submenu",False)]


    # --- Submenús ---
    if start_submenu: # Submenú Iniciar
        # NOTE: persistene.end_game, persistent.unlocked_routes y persistent.after_story_unlocked deben definirse = True en algun lugar del script de juego
        frame:
            style_prefix "submenu"

            vbox:
                spacing gui.submenu_spacing
                
                textbutton "▶ " + _("Nueva partida"):
                    action [Start(), Hide("start_submenu")]
                if persistent.end_game:
                    textbutton "➕ " + _("Nueva partida +"):
                        action [Start("new_game_plus"), Hide("start_submenu")]
                if persistent.unlocked_routes:
                    textbutton "🔀 " + _("Selector de Rutas"):
                        action [ShowMenu("route_selector"), Hide("start_submenu")] #TODO: hacer una pantalla con tag menu, en la pantalla se eligen las rrutas desbloqueadas
                if persistent.after_story_unlocked:
                    textbutton "💞 " + _("After Stories"):
                        action [ShowMenu("after_story_selector"), Hide("start_submenu")] #TODO  hacer una pantalla con tag menu, en la pantalla se eligen los after disponibles

    if load_submenu: # Submenú carga
        frame:
            style_prefix "submenu"

            vbox:
                spacing gui.submenu_spacing

                textbutton "💾 " + _("Continuar"):
                    action [QuickLoad(), Hide("load_submenu")]
                    sensitive FileLoadable(1)
                textbutton "➡️ " + _("Cargar partida"):
                    action [ShowMenu("load"), Hide("load_submenu")]


    ## --- información del juegos ---
    vbox: # Copyright (inferior izquierdo)
        style_prefix "copyright"

        text _("© [gui.year] [gui.developer]. Todos los derechos reservados.")

    vbox: # Versión (inferior derecho)
        style_prefix "version"

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
        # En screens.rpy (main_menu)
        if config.developer:
            text _("Build de desarrollo"):
                style "dev_build_text"

# === Estilos ===
style main_meni_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text:
    font gui.interface_text_font
    color "#ffffff" # TODO hacer que sean variables gui. y que se hereden a los otros textos
    outlines [(1, "#000000aa", 0, 0)] # TODO hacer que sean variables gui. y que se hereden a los otros texto
    # TODO con los cambios sobre los TODO anteriores deben eliminarse las redundancias por herencia

## --- Botones superiores
style top_buttons:
    xalign 1.0
    xoffset -20
    ypos 20 
    spacing 10

## --- Navegación principal ---
style navi_hbox is hbox:
    xalign 0.5
    yalign 0.92
    spacing gui.main_menu_buttons_spacing

style navi_vbox is vbox:
    xalign 0.5
    spacing 5

style navi_text is main_menu_text:
    size gui.main_menu_button_size
    color gui.main_menu_button_color
    hover_color gui.main_menu_button_hover_color
    outlines gui.main_menu_button_outlines
    xalign 0.5


## --- Submenus ---
style submenu_frame is frame:
    background Frame ("gui/overlay/submenu.png", 12, 12) # gui.submenu_f_bg
    padding gui.submenu_padding
    xalign 0.5
    ypos 0.35

style submenu_vbox is vbox:
    spacing gui.submenu_spacing

style submenu_button is button:
    xsize gui.submenu_button_width
    background None
    hover_background Frame("gui/button/hover.png", 6, 6) # gui.hover_btn_bg

style submenu_button_text is navi_text:
    size gui.submenu_button_text_size


# --- Información del juego
style copyright_vbox is vbox:
    xalign 0.0
    xoffset gui.main_menu_copyright_position[0]
    yalign 1.0
    yoffset gui.main_menu_copyright_position[1]

style copyright_text is main_menu_text:
    font gui.main_menu_info_font
    size gui.main_menu_info_size
    color gui.main_menu_info_color

style version_vbox is vbox:
    xalign 1.0
    xoffset gui.main_menu_version_position[0]
    yalign 1.0
    yoffset gui.main_menu_version_position[1]

style version_text is main_menu_text:
    font gui.main_menu_info_font
    size gui.main_menu_info_size
    color gui.main_menu_info_color
    xalign 1.0 # text_align 1.0

style dev_build_text is version_text:
    color "#ff0000"
    outlines [(1, "#ffffff", 0, 0)]

# --- Capa de cierre ---
style close_layer:
    area (0, 0, config.screen_width, config.screen_height)



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