# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")

# --- Presistentes ---
default persistent.first_run = True
default persistent.end_game = False
default persistent.unlocked_routes = set()
default persistent.after_story_unlocked = set()
default persistent.ends = set()

# Diccionarios para nombres más legibles
define route_titles = {
    "r1": "Camino del Bosque",
    "r2": "Camino del Río",
    "r3": "Camino Seguro"
}

define after_titles = {
    "love": "Historia de Amor",
    "friendship": "Amistad Eterna"
}


# El juego comienza aquí.

label new_game_plus:
    # TODO: new game actions
    "Comienzas una nnueva partida con ventajas especiales"
    jump start

label start:
    $ _quit_slot = "quitsave"

    if persistent.first_run:
        $ persistent.first_run = False
        "¡Bienvenido por primera vez!"
    else:
        "¡Bienvenido de nuevo!"
    

    "Ruta común..."
    "Avanzas por la calle"

    menu choices_1:
        "Que ruta tomaré?"

        "ir a la izquierda":
            "elejiste ir a la izquerda"
            $ persistent.unlocked_routes.add("r1")
            jump route_1

        "ir a la derecha":
            "elejiste ir a la derecha"
            $ persistent.unlocked_routes.add("r2")
            jump route_2

        "regresar a casa":
            "decidiste no ir de aventura"
            $ persistent.unlocked_routes.add("r3")
            jump route_3

label route_1:
    "Te adentras en un bosque misterioso."
    # ... Contenido  de la ruta ...
    $ persistent.ends.add("end1")
    jump game_end

label route_2:
    "Llegas a un río cristalino."
    # ... Contenido  de la ruta ...
    $ persistent.ends.add("end2")
    jump game_end

label route_3:
    "Regresas a casa seguro."
    # ... Contenido  de la ruta ...
    $ persistent.ends.add("end3")
    jump game_end

label game_end:
    $ persistent.end_game = True

    $ renpy.unlink_save("quitsave")
    $ _quit_slot = None

    # Desbloquear after story si se cumplen condiciones
    if "end1" in persistent.ends and "end2" in persistent.ends:
        $ persistent.after_story_unlocked.add("love")
    
    if "end3" in persistent.ends:
        $ persistent.after_story_unlocked.add("friendship")

    ".:. Fin del camino .:."
    "..."
    ".."
    "."

    return

# After stories
label after_love:
    "Historia romántica posterior al juego..."
    return

label after_friendship:
    "Historia de amistad posterior al juego..."
    return