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