################################################################################
## Inicialización
################################################################################

## La sentencia 'init offset' hace que las sentencias de inicialización de este
## archivo se ejecuten antes que las sentencias init de cualquier otro archivo.
init offset = -2

## Al llamar a 'gui.init' se restablecen los estilos a valores predeterminados
## razonables, y se establecen el ancho y la altura del juego.
init python:
    gui.init(1920, 1080)

## Habilitar comprobaciones de propiedades no válidas o inestables en pantallas
## o transformaciones.
define config.check_conflicting_properties = True


################################################################################
## Variables de configuración de la interfaz.
################################################################################


## Colores #####################################################################
##
## Los colores del texto de la interfaz.

## El color de acento usado en toda la interfaz para etiquetar y resaltar el
## texto.
define gui.accent_color = '#0099cc'

## El color usado para un botón de texto cuando no está seleccionado ni tiene el
## cursor encima.
define gui.idle_color = '#888888'

## El color 'small' se usa para texto pequeño, que necesita ser más claro/oscuro
## para lograr el mismo efecto.
define gui.idle_small_color = '#aaaaaa'

## El color usado para botones y barras cuando el cursor está encima.
define gui.hover_color = '#66c1e0'

## El color usado en el botón de texto cuando está seleccionado pero no
## enfocado. Un botón está seleccionado si representa la pantalla actual o el
## valor actual de un ajuste.
define gui.selected_color = '#ffffff'

## El color de los botones de texto que no pueden ser seleccionados.
define gui.insensitive_color = '#8888887f'

## Colores de la parte vacía de las barras. No se usan directamente, sino al
## regenerar los archivos de imagen de las barras.
define gui.muted_color = '#003d51'
define gui.hover_muted_color = '#005b7a'

## Colores usados para el texto del diálogo y de las decisiones de menú.
define gui.text_color = '#ffffff'
define gui.interface_text_color = '#ffffff'

## [*] Color del borde del texto de la interface: (grosor, color, x_offset, y_offset) 
# define gui.interface_text_outlines = [(2, "#000000cc", 0, 0)]


## Fuentes y tamaños de fuentes ################################################

## La fuente usada para el texto del juego.
define gui.text_font = "DejaVuSans.ttf"

## La fuente usada para nombres de personajes.
define gui.name_text_font = "DejaVuSans.ttf"

## La fuente usada para el texto externo al juego.
define gui.interface_text_font = "DejaVuSans.ttf"

## El tamaño normal del texto del diálogo.
define gui.text_size = 33

## El tamaño de los nombres de los personajes.
define gui.name_text_size = 45

## El tamaño del texto en la interfaz.
define gui.interface_text_size = 33

## El tamaño de etiquetas en la interfaz.
define gui.label_text_size = 36

## El tamaño del texto en las notificaciones.
define gui.notify_text_size = 24

## El tamaño del título del juego.
define gui.title_text_size = 75


## Menú principal y menús del juego ############################################

## Imágenes del menú principal y menús del juego.
define gui.main_menu_background = "gui/main_menu.png"
define gui.game_menu_background = "gui/game_menu.png"


## Diálogo #####################################################################
##
## Estas variables controlan cómo se muestra el diálogo en la pantalla, una
## línea a la vez.

## Altura de la caja de texto que contiene el diálogo.
define gui.textbox_height = 278

## Colocación vertical de la caja de texto en la pantalla. 0.0 para la parte
## superior, 0.5 para el centro y 1.0 para la parte inferior.
define gui.textbox_yalign = 1.0


## La posición del nombre del personaje que habla, relativa a la caja de texto.
## Puede ser un número entero de píxeles desde la izquierda o la parte superior,
## o 0.5 para centrar.
define gui.name_xpos = 360
define gui.name_ypos = 0

## La alineación horizontal del nombre del personaje. (0.0 es izquierda, 0.5 es
## centro, 1.0 es derecha).
define gui.name_xalign = 0.0

## El ancho, la altura y los bordes de la caja que contiene el nombre del
## personaje, o 'None' para ajustar el tamaño automáticamente.
define gui.namebox_width = None
define gui.namebox_height = None

## Los bordes de la caja que contiene el nombre del personaje, en orden:
## izquierda, arriba, derecha, abajo.
define gui.namebox_borders = Borders(5, 5, 5, 5)

## Si es 'True', el fondo de la caja del nombre se mostrará en mosaico; si es
## 'False', se escalará.
define gui.namebox_tile = False


## La posición del diálogo relativa a la caja de texto. Puede ser un número
## entero de píxeles desde la izquierda o la parte superior de la caja de texto,
## o 0.5 para centrar.
define gui.dialogue_xpos = 402
define gui.dialogue_ypos = 75

## El ancho máximo del texto del diálogo, en píxeles.
define gui.dialogue_width = 1116

## La alineación horizontal del texto del diálogo. (0.0 es izquierda, 0.5 es
## centro, 1.0 es derecha).
define gui.dialogue_text_xalign = 0.0


## Botones #####################################################################
##
## Estas variables, junto con las imágenes de 'gui/button', controlan el aspecto
## de los botones.

## El ancho y la altura del botón, en píxeles. Si es 'None', Ren'Py calcula el
## tamaño.
define gui.button_width = None
define gui.button_height = None

## Los bordes de cada lado del botón, en orden: izquierda, arriba, derecha,
## abajo.
define gui.button_borders = Borders(6, 6, 6, 6)

## Si es 'True', la imagen de fondo se mostrará en mosaico. Si es 'False', la
## imagen de fondo se escalará linealmente.
define gui.button_tile = False

## La fuente usada por el botón.
define gui.button_text_font = gui.interface_text_font

## El tamaño del texto usado por el botón.
define gui.button_text_size = gui.interface_text_size

## El color del texto del botón en varios estados.
define gui.button_text_idle_color = gui.idle_color
define gui.button_text_hover_color = gui.hover_color
define gui.button_text_selected_color = gui.selected_color
define gui.button_text_insensitive_color = gui.insensitive_color

## La alineación horizontal del texto del botón. (0.0 es izquierda, 0.5 es
## centro, 1.0 es derecha).
define gui.button_text_xalign = 0.0


## Estas variables invalidan ajustes para diversos tipos de botones. Ver en la
## documentación los tipos de botones disponibles y el uso de cada uno.
##
## Personalizaciones de la interfaz por defecto:

define gui.radio_button_borders = Borders(27, 6, 6, 6)

define gui.check_button_borders = Borders(27, 6, 6, 6)

define gui.confirm_button_text_xalign = 0.5

define gui.page_button_borders = Borders(15, 6, 15, 6)

define gui.quick_button_borders = Borders(15, 6, 15, 0)
define gui.quick_button_text_size = 21
define gui.quick_button_text_idle_color = gui.idle_small_color
define gui.quick_button_text_selected_color = gui.accent_color

## Se pueden añadir personalizaciones propias agregando variables con los
## nombres adecuados. Por ejemplo, es posible descomentar la línea siguiente
## para ajustar el ancho de los botones de navegación.

# define gui.navigation_button_width = 250


## Botones de decisión #########################################################
##
## Los botones de decisión se utilizan en los menús del juego.

define gui.choice_button_width = 1185
define gui.choice_button_height = None
define gui.choice_button_tile = False
define gui.choice_button_borders = Borders(150, 8, 150, 8)
define gui.choice_button_text_font = gui.text_font
define gui.choice_button_text_size = gui.text_size
define gui.choice_button_text_xalign = 0.5
define gui.choice_button_text_idle_color = '#888888'
define gui.choice_button_text_hover_color = "#ffffff"
define gui.choice_button_text_insensitive_color = '#8888887f'


## Botones de partidas #########################################################
##
## El botón de hueco de partida es un botón especial. Contiene una miniatura y
## texto que describe el contenido del hueco de partida. Usa imágenes en 'gui/
## button' como los otros botones.

## Botón de guardar partida
define gui.slot_button_width = 414
define gui.slot_button_height = 309
define gui.slot_button_borders = Borders(15, 15, 15, 15)
define gui.slot_button_text_size = 21
define gui.slot_button_text_xalign = 0.5
define gui.slot_button_text_idle_color = gui.idle_small_color
define gui.slot_button_text_selected_idle_color = gui.selected_color
define gui.slot_button_text_selected_hover_color = gui.hover_color

## Ancho y altura de las miniaturas de las partidas guardadas.
define config.thumbnail_width = 384
define config.thumbnail_height = 216

## Número de columnas y filas de la cuadrícula de partidas guardadas.
define gui.file_slot_cols = 3
define gui.file_slot_rows = 2


## Posicionamiento y espacios ##################################################
##
## Estas variables controlan la posición y espacios de diversos elementos de la
## interfaz.

## Posición del lado izquierdo de los botones de navegación, relativa al lado
## izquierdo de la pantalla.
define gui.navigation_xpos = 60

## Posición vertical del indicador de salto.
define gui.skip_ypos = 15

## Posición vertical de la pantalla de notificación.
define gui.notify_ypos = 68

## Espacio entre decisiones del menú.
define gui.choice_spacing = 33

## Botones en la sección de navegación del menú principal y el menú del juego.
define gui.navigation_spacing = 6

## Controla el espacio entre ajustes.
define gui.pref_spacing = 15

## Controla el espacio entre botones de ajustes.
define gui.pref_button_spacing = 0

## Espacio entre botones de página.
define gui.page_spacing = 0

## Espacio entre huecos de guardado.
define gui.slot_spacing = 15

## Posición del texto del menú principal.
define gui.main_menu_text_xalign = 1.0


## Marcos ######################################################################
##
## Estas variables controlan la apariencia de los marcos que pueden contener
## componentes de la interfaz cuando no hay un 'overlay' o ventana.

## Marcos genéricos
define gui.frame_borders = Borders(6, 6, 6, 6)

## Marco usado en la pantalla de confirmación.
define gui.confirm_frame_borders = Borders(60, 60, 60, 60)

## Marco usado en la pantalla de salto.
define gui.skip_frame_borders = Borders(24, 8, 75, 8)

## Marco usado en la pantalla de notificación.
define gui.notify_frame_borders = Borders(24, 8, 60, 8)

## ¿El fondo del marco debe ser en mosaico?
define gui.frame_tile = False


## Barras, barras de desplazamiento y deslizadores #############################
##
## Aquí se controla la apariencia y el tamaño de barras, barras de
## desplazamiento y deslizadores.
##
## La GUI por defecto solo usa deslizadores y barras de desplazamiento
## verticales. Todas las demás barras solo se usan en pantallas escritas por el
## creador.

## Altura de las barras, barras de desplazamiento y deslizadores horizontales.
## El ancho de barras, barras de desplazamiento y deslizadores verticales.
define gui.bar_size = 38
define gui.scrollbar_size = 18
define gui.slider_size = 38

## 'True' si las imágenes de las barras deben mostrarse en mosaico. 'False' si
## deben escalarse linealmente.
define gui.bar_tile = False
define gui.scrollbar_tile = False
define gui.slider_tile = False

## Bordes horizontales.
define gui.bar_borders = Borders(6, 6, 6, 6)
define gui.scrollbar_borders = Borders(6, 6, 6, 6)
define gui.slider_borders = Borders(6, 6, 6, 6)

## Bordes verticales.
define gui.vbar_borders = Borders(6, 6, 6, 6)
define gui.vscrollbar_borders = Borders(6, 6, 6, 6)
define gui.vslider_borders = Borders(6, 6, 6, 6)

## Qué hacer con las barras de desplazamiento no desplazables en el menú del
## juego. 'hide' las oculta, mientras que 'None' las muestra.
define gui.unscrollable = "hide"


## Historial ###################################################################
##
## La pantalla de historial muestra diálogo que el jugador ya ha visto.

## Número de bloques de historial de diálogo que Ren'Py conserva.
define config.history_length = 250

## Altura de la entrada de la pantalla de historial, o 'None' para que la altura
## sea variable a costa del rendimiento.
define gui.history_height = 210

## Espacio adicional para añadir entre las entradas de la pantalla de historial.
define gui.history_spacing = 0

## La posición, el ancho y la alineación de la etiqueta que muestra el nombre
## del personaje que habla.
define gui.history_name_xpos = 233
define gui.history_name_ypos = 0
define gui.history_name_width = 233
define gui.history_name_xalign = 1.0

## La posición, el ancho y la alineación del texto del diálogo.
define gui.history_text_xpos = 255
define gui.history_text_ypos = 3
define gui.history_text_width = 1110
define gui.history_text_xalign = 0.0


## Modo NVL ####################################################################
##
## La pantalla del modo NVL muestra el diálogo hablado por los personajes en
## modo NVL.

## Bordes del fondo de la ventana del modo NVL.
define gui.nvl_borders = Borders(0, 15, 0, 30)

## El número máximo de entradas en modo NVL que Ren'Py mostrará. Cuando haya más
## entradas que este número, se eliminará la más antigua.
define gui.nvl_list_length = 6

## Altura de la entrada en modo NVL. Establece esto en 'None' para que las
## entradas ajusten su altura dinámicamente.
define gui.nvl_height = 173

## Espacio entre entradas en modo NVL cuando 'gui.nvl_height' es 'None', y entre
## las entradas en modo NVL y un menú en modo NVL.
define gui.nvl_spacing = 15

## La posición, el ancho y la alineación de la etiqueta que muestra el nombre
## del personaje que habla.
define gui.nvl_name_xpos = 645
define gui.nvl_name_ypos = 0
define gui.nvl_name_width = 225
define gui.nvl_name_xalign = 1.0

## La posición, el ancho y la alineación del texto del diálogo.
define gui.nvl_text_xpos = 675
define gui.nvl_text_ypos = 12
define gui.nvl_text_width = 885
define gui.nvl_text_xalign = 0.0

## La posición, el ancho y la alineación del texto 'nvl_thought' (el texto dicho
## por el personaje 'nvl_narrator').
define gui.nvl_thought_xpos = 360
define gui.nvl_thought_ypos = 0
define gui.nvl_thought_width = 1170
define gui.nvl_thought_xalign = 0.0

## Posición de los botones de menú NVL.
define gui.nvl_button_xpos = 675
define gui.nvl_button_xalign = 0.0


## Localización ################################################################

## Esto controla dónde se permite un salto de línea. El valor por defecto es
## adecuado para la mayoría de los idiomas. Puede encontrar una lista de valores
## disponibles en https://www.renpy.org/doc/html/style_properties.html#style-
## property-language

define gui.language = "unicode"


################################################################################
## Dispositivos móviles
################################################################################

init python:

    ## Esto aumenta el tamaño de los botones rápidos para facilitar su acceso en
    ## tabletas y teléfonos.
    @gui.variant
    def touch():

        gui.quick_button_borders = Borders(60, 21, 60, 0)

    ## Esto cambia el tamaño y espaciado de varios elementos de la GUI para
    ## asegurar que sean fácilmente visibles en los teléfonos.
    @gui.variant
    def small():

        ## Tamaños de fuente.
        gui.text_size = 45
        gui.name_text_size = 54
        gui.notify_text_size = 38
        gui.interface_text_size = 45
        gui.button_text_size = 45
        gui.label_text_size = 51

        ## Ajusta la colocación de la caja de texto.
        gui.textbox_height = 360
        gui.name_xpos = 120
        gui.dialogue_xpos = 135
        gui.dialogue_width = 1650

        ## Cambia el tamaño y espaciado de varios elementos.
        gui.slider_size = 54

        gui.choice_button_width = 1860
        gui.choice_button_text_size = 45

        gui.navigation_spacing = 30
        gui.pref_button_spacing = 15

        gui.history_height = 285
        gui.history_text_width = 1035

        gui.quick_button_text_size = 30

        ## Distribución de botones de archivo.
        gui.file_slot_cols = 2
        gui.file_slot_rows = 2

        ## Modo NVL
        gui.nvl_height = 255

        gui.nvl_name_width = 458
        gui.nvl_name_xpos = 488

        gui.nvl_text_width = 1373
        gui.nvl_text_xpos = 518
        gui.nvl_text_ypos = 8

        gui.nvl_thought_width = 1860
        gui.nvl_thought_xpos = 30

        gui.nvl_button_width = 1860
        gui.nvl_button_xpos = 30


################################################################################
## [*]Personalización propia
################################################################################

## Colores #####################################################################
##
## Los colores del texto de la interfaz.

## [*] Color del borde del texto de la interface: (grosor, color, x_offset, y_offset) 
# define gui.interface_text_outlines = [(2, "#000000cc", 0, 0)]


## Fuentes y tamaños de fuentes ################################################
##
## las feuntes usadas

# [placeholder]

## Menú principal y menús del juego ############################################
##
## Controla la apariencia del menú principal y menús del juego

## Logo del juego
define gui.main_menu_logo = "gui/game_logo.png"
# define gui.main_menu_logo_position = (0.5, 0.6) [X]
define gui.main_menu_logo_xaling = 0.5
define gui.main_menu_logo_ypos = 0.6

## --- Navi
## Estilos de textos del menu principal
define gui.navi_button_text_size = 26
define gui.navi_button_text_xalign = 0.5

## Estilos de textos informativos
define gui.version_text_size = 18
define gui.version_text_outlines = [(1, "#000000aa", 0, 0)]

## Posiciones de texto informativo
define gui.main_menu_version_position = (-20, -20)
define gui.main_menu_copyright_position = (20, -20)

## Estilos de botones principales
define gui.main_menu_navi_orientation = "horizontal" 
# OPTIONS: "horizontal" o "vertical"

define gui.main_menu_navi_hposition = (0.5, 0.9) # (xalign, yalign)
define gui.navi_buttons_hspacing = 30

define gui.main_menu_navi_vposition = (0.05, 0.5) # (xalign, yalign)
define gui.navi_buttons_vspacing = 2

define gui.navi_button_text_size = 26 # [x]
define gui.navi_button_text_xalign = 0.5 # [x]

    ## NOTE: Ejemplos de ajustes recomendados 
    ##                                       position  / spacing
    ##                                 (xalign, yalign)
    ## Horizontal inferior centrado       -> (0.5, 0.9),  30
    ## Horizontal inferiro a la izquierda -> (0.1, 0.9),  30
    ## Horizontal inferiro a la derecha   -> (0.9, 0.9),  30
    ## Vertical centrado                  -> (0.5, 0.5),  30 Horizontal / 2 Vertical
    ## Vertical a la izquierda            -> (0.1, 0.5),  2 
    ## Vertical a la derecha              -> (0.9, 0.5),  2 

## Textos al pie
define gui.footer_text_size = 20
# define gui.footer_text_outlines = [(1, "#000000aa", 0, 0)]

## Submenús
define gui.submenu_hspacing = 30
define gui.submenu_vspacing = 10
define gui.submenu_padding = (25, 25)
define gui.submenu_button_text_size = 24
define gui.submenu_button_text_xalign = 0.0

# TODO: las demas varaibles GUI
