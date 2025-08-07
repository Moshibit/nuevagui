## Pantalla de preferencias ####################################################
##
## La pantalla de preferencias permite al jugador configurar el juego a su
## gusto.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

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
