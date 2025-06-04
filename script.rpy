# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")

# --- Presistentes ---
default persistent.first_run = True
default persistent.end_game = False
default persistent.unlocked_routes = set()
default persistent.after_story_unlocked = set()
default persistent.ends = set()

# El juego comienza aquí.

label start:
    "#inicio"
    $ persistent.first_run = False

    "#ruta común"
    "..."
    ".."
    "."
    "Avanzas por la calle"

    "#Punto de inflexión"
    menu choices_1:
        "Que ruta tomaré?"

        "ir a la izquierda":
            "elejiste ir a la izquerda"
            $ persistent.unlocked_routes.add("r1")
            jump rute_1

        "ir a la derecha":
            "elejiste ir a la derecha"
            $ persistent.unlocked_routes.add("r2")
            jump rute_2

        "regresar a casa":
            "decidiste no ir de aventura"
            $ persistent.unlocked_routes.add("r3")
            jump ruta_3

label rute_1:
    "Te adentras en un bosque."
    "Qué haras ahora?"
    "..."
    ".."
    "."
    $ persistent.ends.add("end1")
    jump game_end

label rute_2:
    "Llegas a un río"
    "ves un pequeño bote."
    "..."
    ".."
    "."
    $ persistent.ends.add("end2")
    jump game_end

label rute_3:
    "Regresas a casa seguro"
    "..."
    ".."
    "."
    $ persistent.ends.add("end3")
    jump game_end

label game_end:
    # Finaliza el juego:
    "#Fin"
    "..."
    ".."
    "."
    $ persistent.end_game = True
    return

