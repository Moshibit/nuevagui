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

screen grafics_opt():
    vbox:
        text "algo va aquí _G_"

screen text_opt():

    hbox:
        box_wrap True

        if renpy.variant("pc") or renpy.variant("web"):

            vbox:
                style_prefix "radio"
                label _("Pantalla")
                textbutton _("Ventana") action Preference("display", "window")
                textbutton _("Pantalla completa") action Preference("display", "fullscreen")

        vbox:
            style_prefix "check"
            label _("Saltar")
            textbutton _("Texto no visto") action Preference("skip", "toggle")
            textbutton _("Tras elecciones") action Preference("after choices", "toggle")
            textbutton _("Transiciones") action InvertSelected(Preference("transitions", "toggle"))

        ## Aquí se pueden añadir 'vboxes' adicionales del tipo
        ## "radio_pref" o "check_pref" para nuevas preferencias.

    null height (4 * gui.pref_spacing)

    hbox:
        style_prefix "slider"
        box_wrap True

        vbox:

            label _("Veloc. texto")

            bar value Preference("text speed")

            label _("Veloc. autoavance")

            bar value Preference("auto-forward time")

        vbox:

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


screen audio_opt():
    vbox:
        text "algo va aquí _A_"

screen voice_opt():
    vbox:
        text "algo va aquí _V_"

screen save_load_opt():
    vbox:
        text "algo va aquí _S_"


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
