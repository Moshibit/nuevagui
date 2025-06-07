# init python:
#     # Verificar y cargar DLCs disponibles
#     def load_dlc_content():
#         # Inicializar persistente si no existe
#         if not hasattr(persistent, 'has_dlc'):
#             persistent.has_dlc = {}
        
#         for dlc_name in dlc_config.keys():
#             dlc_path = os.path.join(config.gamedir, f"{dlc_name}_dlc.zip")
#             if os.path.exists(dlc_path):
#                 # Montar DLC
#                 config.searchpath.append(dlc_path)
#                 renpy.load_archive(dlc_path)
#                 persistent.has_dlc[dlc_name] = True
#                 renpy.log(f"DLC cargado: {dlc_name}")
#             else:
#                 persistent.has_dlc[dlc_name] = False

#     # Verificar al inicio del juego
#     config.start_callbacks.append(load_dlc_content)

#     # Función para verificar contenido AO
#     def has_ao_content():
#         return persistent.has_dlc.get("ao_content", False) or gui.rated == "M" #AO


## En screens.rpy (ejemplo de uso):

    # style_prefix "after_story"
    
    # if has_ao_content():
    #     textbutton _("Escenas Adultas"):
    #         action Start("ao_scenes_path")
    # else:
    #     textbutton _("Contenido Adulto (DLC requerido)"):
    #         action [
    #             OpenURL("https://tienda.com/ao_dlc"),
    #             Notify(_("Redirigiendo a la tienda..."))
    #         ]


########### idea aparrte

# label start:
#     if DEMO_VERSION:
#         "¡Esta es una versión demo del juego!"
    
#     if ADULT_CONTENT:
#         show explicit_scene
#     elif CENSORED_VERSION:
#         show censored_scene