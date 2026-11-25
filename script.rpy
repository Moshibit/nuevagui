# Coloca el código de tu juego en este archivo.

# Declara los personajes usados en el juego como en el ejemplo:

define e = Character("Eileen")

# --- Presistentes ---
default persistent.first_game_run = False
default persistent.end_game = False
default persistent.unlocked_routes = set()
default persistent.after_story_unlocked = set()
default persistent.ends = set()

# Se establece en True desde el script del DLC.
default persistent.adult_dlc_installed = False

# Variable para controlar el contenido de la primera ejecución.
default persistent.first_run_completed = False

# --- Persistentes de splash
default persistent.chose_lang = False
default persistent.asked_accessibility = False




# Diccionarios para nombres más legibles
define route_titles = {
    "route_1": "Camino del Bosque",
    "route_2": "Camino del Río",
    "route_3": "Camino Seguro"
}

define after_titles = {
    "after_love": "Historia de Amor",
    "after_friendship": "Amistad Eterna"
}


# label quit:
# # Se ejecuta cada vez que el jugador sale del juego
#     return

# • Despedidas personalizadas por personaje: Hacer que el personaje activo en ese momento diga una frase de despedida diferente según su nivel de afecto o el estado de la historia antes de cerrar la ventana.
# • Negarse a cerrar (Terror / Meta): En juegos de terror psicológico, puedes hacer que al intentar cerrar el juego aparezca un diálogo donde el villano o una IA te diga "No puedes irte todavía" y te devuelva a la partida (usando return en lugar de renpy.quit()).
# • Autoguardado silencioso: Guardar datos críticos en persistent justo antes de que la aplicación se cierre por completo.


# label splashscreen:
# # Se ejecuta al iniciar el juego

    # Elegir idionma una sola vez
    # Accesibilidad una sola vez
    # desarroladores
    # creditos del motor
    # publisher
    # discliamers 
    # verificación edad y si dlc esta activado una sola vez
    # Experiencia first run una sola vez
    # titulo del juego (opcional)

    # # --- 1. SELECCIÓN DE IDIOMA (UNA SOLA VEZ) --- TODO:
    # if not persistent.chose_lang:
    #     call screen language_selection_screen
    #     $ persistent.chose_lang = True

    # # --- 2. ACCESIBILIDAD (UNA SOLA VEZ) --- # TODO:
    # if not persistent.asked_accessibility:
    #     scene black
    #     "¿Deseas configurar las opciones de accesibilidad ahora?"
    #     extend "Puedes ajustar el tamaño del texto, activar la lectura por voz y más."
        
    #     menu:
    #         "Sí, abrir opciones de accesibilidad":
    #             # Abre el menú nativo de accesibilidad de Ren'Py.
    #             $ renpy.run(Preference("accessibility menu"))
            
    #         "No, continuar":
    #             pass
        
    #     $ persistent.asked_accessibility = True

    # # --- 3. DESARROLLADORES ---
    # show screen title_screen("Un Juego de NOMBRE_DEL_ESTUDIO", subtitle="presenta")
    # with dissolve 
    # pause(1.0)
    # hide screen title_screen
    # with dissolve

    # # --- 4. CRÉDITOS DEL MOTOR ---
    # show screen title_screen("Creado con Ren'Py", subtitle="© 2004-2026 Tom Rothamel")
    # with dissolve 
    # pause(1.0)
    # hide screen title_screenSS
    # with dissolve

    # return

    # ----------------------------------------------------------------------------
    # # --- FASE 2.5: SELECCIÓN DE IDIOMA (SOLO LA PRIMERA VEZ) ---
    # if not persistent.chose_lang:
    #     # Llama a la pantalla de selección de idioma.
    #     call screen language_selection_screen
    #     # Marca que el jugador ya eligió un idioma.
    #     $ persistent.chose_lang = True

    # # --- FASE 0: LÓGICA DE VERIFICACIÓN DE EDAD (SOLO SI EL DLC ESTÁ ACTIVO) ---
    # # Se comprueba la variable persistente Y la existencia del archivo marcador del DLC.
    # if persistent.adult_dlc_installed and renpy.loadable("dlc/adult_enabled.flag"):
        
    #     # Lógica de verificación de edad proporcionada.
    #     $ age_lower, age_upper = renpy.get_user_age()

    #     if age_upper < 18:
    #         # El usuario es menor de 18 años con certeza. Acceso denegado.
    #         jump under_18_screen
    #     elif age_lower >= 18:
    #         # El usuario es mayor de 18 años con certeza. Acceso permitido.
    #         jump bypass_age_check
    #     else:
    #         # El rango de edad no es concluyente. Se solicita verificación manual.
    #         jump age_check

    # # Si el DLC no está activo, o la plataforma no soporta la verificación de edad,
    # # se continúa al juego con normalidad sin contenido adulto.

    # # ---

    # # --- FASE 1: DISCLAIMERS Y ADVERTENCIAS INICIALES ---
    # scene black
    # with Pause(0.5)

    # # Disclaimer de obra de ficción y contenido general.
    # "{size=+4}{b}AVISO IMPORTANTE{/b}{/size}\n\n"
    # # extend "{i}Este es un trabajo de ficción. Cualquier parecido con la realidad es pura coincidencia.{/i}\n\n"
    # # extend "Este juego puede contener temas sensibles como {b}[[TEMAS_SENSIBLES, EJ. VIOLENCIA, TRAUMAS, ETC.]{/b}.\n"
    # # extend "Se recomienda discreción del jugador."
    # with Pause(3.0)

    # if persistent.adult_dlc_installed and renpy.loadable("dlc/adult_enabled.flag"):
    #     "{size=+4}{b}ADVERTENCIA DE CONTENIDO ADULTO{/b}{/size}\n\n"
    #     extend "Este juego contiene material explícito para audiencias maduras.\n"
    #     extend "Todos los personajes son adultos y las situaciones son ficticias."
    #     with Pause(4.0)
# -----------------------------------------------------------------------------------------


# ADVERTENCIA DE CONTENIDO ADULTO

# Este videojuego contiene material explícito de naturaleza erótica, desnudez y temas para audiencias maduras.
# Al continuar, usted confirma y declara que:
#     Es mayor de 18 años (o la edad de mayoría legal en su jurisdicción) y que el acceso a este tipo de contenido es legal en su lugar de residencia.
#     Todas las situaciones son ficticias. La totalidad de los personajes, eventos y diálogos son producto de la ficción. Cualquier parecido con personas reales, vivas o muertas, es pura coincidencia.
#     Todos los personajes son adultos. Todos los personajes que aparecen en este juego, incluyendo cualquier representación de ellos en escenas de naturaleza sexual, tienen 18 años o más.
#     No se ha utilizado a personas reales. Ninguna persona real fue utilizada, fotografiada o filmada en la creación de este software. Todo el contenido gráfico es de naturaleza artística y digital.
# Si usted es menor de edad, o si este tipo de contenido no es legal en su jurisdicción, por favor, abandone el juego ahora.


    # # Créditos del motor (obligatorio por la licencia de Ren'Py).
    # scene black
    # "{b}Motor de Juego{/b}\n\n"
    # # extend "Creado con {b}Ren'Py {renpy.version_string}{/b}\n"
    # # extend "© 2004-2026 Tom Rothamel y colaboradores.\n"
    # # extend "Visita {a=https://www.renpy.org}www.renpy.org{/a} para más información."
    # with Pause(3.0)

    # # Disclaimer de marcas registradas y derechos de autor.
    # scene black
    # "{size=+2}Créditos y Propiedad Intelectual{/size}\n\n"
    # extend "Ren'Py® es una marca registrada de Tom Rothamel.\n"
    # extend "Todos los personajes, escenarios y situaciones son propiedad de {b}[[NOMBRE_DEL_ESTUDIO/AUTOR]{/b}.\n"
    # extend "Queda prohibida la redistribución no autorizada de este material."
    # with Pause(3.0)

    # # 2. Nota breve de redirección
    # scene black
    # "{i}Para ver los créditos completos, los disclaimers legales y la información del motor, visita la pantalla \"About\" en el menú principal.{/i}"

    # # --- FASE 2: CONTENIDO ÚNICO DE LA PRIMERA EJECUCIÓN ---
    # if not persistent.first_run_completed:
    #     # TODO: colocar
    #     # Aquí puedes colocar una secuencia jugable, un tutorial interactivo,
    #     # una introducción especial o una pantalla de selección de idioma.
    #     # Ejemplo: una pequeña escena cinemática o un minijuego.
    #     call screen first_run_experience  # Llama a una screen personalizada.
        
    #     # Marca la primera ejecución como completada.
    #     $ persistent.first_run_completed = True


# --- LABELS DE SOPORTE PARA LA VERIFICACIÓN DE EDAD ---

label under_18_screen:
    scene black
    "{size=+4}ACCESO DENEGADO{/size}\n\n"
    extend "Lo sentimos, este contenido no está disponible para menores de 18 años."
    with Pause(5.0)
    
    # Cierra el juego o vuelve al menú principal.
    $ renpy.quit()
    return

label bypass_age_check:
    # La plataforma confirmó que el usuario es mayor de edad.
    # Aquí puedes registrar el evento o simplemente continuar.
    $ persistent.age_verified_by_platform = True
    return

label age_check:
    # Pantalla para que el usuario introduzca su fecha de nacimiento o confirme su edad.
    # Debes crear la screen "age_verification_screen" en tu proyecto.
    call screen age_verification_screen
    
    # La screen debe devolver True si el usuario confirma ser mayor de edad.
    if _return == True:
        $ persistent.age_verified_manually = True
        return
    else:
        jump under_18_screen


# • Introducción interactiva o jugable: En lugar de un simple logo estático, puedes poner una escena jugable corta, un minijuego o una cinemática que varíe según el progreso guardado en persistent.
# • Comprobación de archivos externos (Meta-juego): Puedes usar Python para leer archivos del sistema del jugador (como en Doki Doki Literature Club o OneShot), cambiar el título de la ventana (config.window_title) o modificar el splashscreen si detecta que el jugador ya terminó el juego o borró algún archivo.
# • Aviso de contenido dinámico: Mostrar advertencias de contenido sensible con botones para activar o desactivar filtros (como sangre o luces parpadeantes) antes de que cargue la interfaz principal.

# # selector de contenido

# ✨ Otros Disclaimers y Elementos para el Splashscreen

# Además de los legales, puedes incluir otros avisos y contenidos para mejorar la experiencia y la transparencia:
# Disclaimers Adicionales

#     Advertencia de "Obra de Ficción": Un recordatorio general de que todo es ficticio, independientemente del contenido adulto. "Este es un trabajo de ficción. Cualquier parecido con la realidad es pura coincidencia."
#     Advertencia de Disparadores (Trigger Warnings): Si tu juego trata temas sensibles como violencia, abuso, autolesión, etc., es una buena práctica listarlos. Puedes hacerlo en una pantalla aparte o en el texto del disclaimer principal.
#     Disclaimer de Licencia de Contenido de Terceros: Si usas música, arte o fuentes de otros creadores, es importante acreditar la licencia (por ejemplo, Creative Commons) y al autor.
#     Aviso de "Fair Use" (Uso Justo): Si tu juego es una parodia o hace referencias a obras con derechos de autor, un aviso de que dicho uso se ampara en la doctrina del "Fair Use" (especialmente relevante en EE. UU.).
#     Disclaimer de Exactitud Legal: Un aviso de que el jugador es responsable de verificar que el contenido es legal en su país antes de jugar.

# Otros Contenidos para el Splashscreen

#     Logos de Empresas/Estudios: Los logotipos de tu estudio, del motor (Ren'Py) y de cualquier colaborador. Pueden mostrarse con animaciones (fundidos, zooms).
#     Créditos de Motor y Herramientas: Un texto que diga "Creado con Ren'Py" y quizás mencione otras herramientas importantes (Daz3d, Photoshop, etc.).
#     Pantalla de "Consejos" o "Did You Know?": Mientras se carga el juego, puedes mostrar una pantalla con curiosidades sobre el desarrollo o la historia.
#     Agradecimientos Especiales: Un espacio para agradecer a patrocinadores de Kickstarter/Patreon, beta testers o contribuidores clave.
#     Verificación de Consentimiento: En lugar de solo un disclaimer pasivo, puedes requerir una acción del jugador, como hacer clic en un botón de "Acepto" o marcar una casilla de verificación para confirmar que ha leído y entendido las advertencias.
#     Selector de Contenido (Content Toggle): Una pantalla que permita al jugador activar o desactivar ciertos tipos de contenido (por ejemplo, violencia excesiva o escenas explícitas) antes de comenzar.
#     Mini-juego o Interacción Única: Como ya tenías planeado, una pequeña escena interactiva o un tutorial que solo se muestra la primera vez que se abre el juego.


label before_main_menu:
# Se ejecuta al antes del main menu

    $ _preferences.afm_enable = False
    return 


# Se ejecuta cada vez que el juego va a entrar al menú principal (tanto al iniciar como al volver desde una partida).
# • Menú principal evolutivo: Puedes cambiar variables globales o persistentes para que el fondo, la música o los botones del menú principal cambien dinámicamente según el capítulo en el que se quedó el jugador, el final que sacó o la hora real del sistema (datetime).
# • Falso crasheo o cambio de identidad: Hacer que, tras un evento dramático en la historia, el jugador sea enviado aquí y el menú principal parezca de otro juego completamente distinto.


# label main_menu:
# Se ejecuta en lugar de la pantalla main menu

    #
    #return # NOTE: si se hace return salta a label start sin mostrar el menu.

#     Se ejecuta cada vez que el juego va a entrar al menú principal (tanto al iniciar como al volver desde una partida).
# • Menú principal evolutivo: Puedes cambiar variables globales o persistentes para que el fondo, la música o los botones del menú principal cambien dinámicamente según el capítulo en el que se quedó el jugador, el final que sacó o la hora real del sistema (datetime).
# • Falso crasheo o cambio de identidad: Hacer que, tras un evento dramático en la historia, el jugador sea enviado aquí y el menú principal parezca de otro juego completamente distinto.


# label enter_game_menu:
# # esta special label la encontré en el código fuente, no esta en la documentación

#     #
#     return


# label after_load:
# # Se ejecuta inmediatamente después de cargar una partida   
#     return

# • Parches retroactivos (Save-file patching): Si actualizas tu juego y añades una variable nueva o corriges un bug de una versión anterior, puedes comprobar aquí si la variable existe (if not hasattr(store, 'nueva_var'):) e inicializarla para no romper las partidas guardadas viejas de tus jugadores.
# • Eventos por "hacer trampa" (Save Scumming): Puedes guardar un contador en persistent cada vez que se toma una decisión importante. Si el jugador carga una partida anterior para cambiar su respuesta, after_load puede detectar la discrepancia entre el persistent y la partida cargada, haciendo que un personaje rompa la cuarta pared y le reclame por volver atrás en el tiempo.
# • Recapitulación automática: Mostrar un breve mensaje o pantalla de "Anteriormente en..." con un resumen de los objetivos actuales si ha pasado mucho tiempo (en tiempo real) desde la última vez que se guardó esa partida.


label before_load:
# Se ejecuta antes de cargar una partida 

    $ _preferences.afm_enable = False
    return


# label after_warp:
# # asd
#     return


# label hide_windows:
# # asd
#     return

# Secretos ocultos a simple vista: Puedes aprovechar esta etiqueta para mostrar elementos ocultos en el escenario 
# (pistas, fantasmas en el fondo, mensajes secretos) que solo aparecen cuando el jugador oculta los diálogos, y 
# volver a ocultarlos al salir de la etiqueta.


label end_chapter:
# Se ejecuta al finalizar capítulos (responsabilidad del programador hacer llamada)
    $ _preferences.afm_enable = False
    return


# Ren'Py also uses the following labels to show some of the special screens:
#     label main_menu_screen
#     label load_screen
#     label save_screen
#     label preferences_screen
#     label joystick_preferences_screen

# label _library_main_menu
# _save_screen / _save_screen_hook
# _load_screen / _load_screen_hook

##  wrapper de label > 00start.rpy y 00gamemenu.rpy


label title(message, subtitle=None):

    show screen title_screen(message, subtitle)
    with dissolve
    pause 2
    hide screen title_screen
    with dissolve

    return

# El juego comienza aquí.

label new_game_plus:
    # TODO: new game actions # TODO: quizas deberia mejor cargarse en una special label, o en star, usando una flag 
    "Comienzas una nueva partida con ventajas especiales"
    jump start

# TODO POR DEFAULT las velocidad de avance de letras no debe estar al maximo

label start:
    $ _quit_slot = "quitsave"

    if not persistent.first_game_run:
        $ persistent.first_game_run = True
        "¡Bienvenido por primera vez!"
    else:
        "¡Bienvenido de nuevo!"

    # Muestra una imagen de fondo: Aquí se usa un marcador de posición por
    # defecto. Es posible añadir un archivo en el directorio 'images' con el
    # nombre "bg room.png" o "bg room.jpg" para que se muestre aquí.

    scene bg room

    # Muestra un personaje: Se usa un marcador de posición. Es posible
    # reemplazarlo añadiendo un archivo llamado "eileen happy.png" al directorio
    # 'images'.

    show eileen happy

    # Presenta las líneas del diálogo.

    e "Has creado un nuevo juego Ren'Py."

    e "Añade una historia, imágenes y música, ¡Y presentarlo al mundo!"


    "1"

    "2"

    "3"

    return
        

    "Ruta común..."
    "Avanzas por la calle"

    menu choices_1:
        "Que ruta tomaré?"

        "Ir a la izquierda":
            "Elejiste ir a la izquerda"
            $ persistent.unlocked_routes.add("route_1")
            jump route_1

        "Ir a la derecha":
            "Elejiste ir a la derecha"
            $ persistent.unlocked_routes.add("route_2")
            jump route_2

        "Regresar a casa":
            "Decidiste no ir de aventura"
            $ persistent.unlocked_routes.add("route_3")
            jump route_3

label route_1:
    "Te adentras en un bosque misterioso."
    # ... Contenido  de la ruta ...
    $ persistent.ends.add("end_1")
    jump game_end

label route_2:
    "Llegas a un río cristalino."
    # ... Contenido  de la ruta ...
    $ persistent.ends.add("end_2")
    jump game_end

label route_3:
    "Regresas a casa seguro."
    # ... Contenido  de la ruta ...
    $ persistent.ends.add("end_3")
    jump game_end

label game_end:
    $ persistent.end_game = True

    $ renpy.unlink_save("quitsave")
    $ _quit_slot = None

    # Desbloquear after story si se cumplen condiciones
    if "end_1" in persistent.ends and "end_2" in persistent.ends:
        $ persistent.after_story_unlocked.add("after_love")
    
    if "end_3" in persistent.ends:
        $ persistent.after_story_unlocked.add("after_friendship")

    ".:. Fin del camino .:."

    return


# After stories
label after_love:
    "Historia romántica posterior al juego..."
    return

label after_friendship:
    "Historia de amistad posterior al juego..."
    return



################33
# ejemplo de save scumming  
#######################33
# default decision_tomada = False

# label escena_critica:
#     menu:
#         "Salvar al personaje":
#             $ decision_tomada = True
#             $ persistent.ya_decidio = True
#         "Abandonarlo":
#             $ decision_tomada = False
#             $ persistent.ya_decidio = True

# label after_load:
#     # Si en el archivo persistente consta que ya tomó una decisión,
#     # pero la partida cargada tiene la variable en False (porque cargó antes de elegir):
#     if persistent.ya_decidio and not decision_tomada:
#         "Narrador" "Crees que cargando la partida podrás cambiar lo que hiciste, ¿verdad?"
#     return
################################33
####################################3