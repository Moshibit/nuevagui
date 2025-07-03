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