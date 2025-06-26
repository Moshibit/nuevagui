# --- Capa de cierre ---
screen close_layer:
    key "game_menu" action Hide(screen=None)

    button:
        style "close_layer"
        action Hide(screen=None)

style close_layer:
    area (0, 0, config.screen_width, config.screen_height)
    background "#000000aa"
