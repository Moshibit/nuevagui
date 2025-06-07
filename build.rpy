# build.rpy
init python:
    import os
    import datetime
    import subprocess
    import shutil

    # Configuración general
    build.directory_name = "build"
    gui.platform = "Multiplataform"
    gui.market = "General"
    # NOTE: config.name y config.versión se definen en options.rpy.

    # Plataformas objetivo
    build.targets = [
        "windows",
        "linux",
        "mac",
        "web",
        "android",
    ]

    # Mapeo de plataformas a nombres legibles
    PLATFORM_NAMES = {
        "windows": "Windows",
        "linux": "Linux",
        "mac": "MacOS",
        "web": "Web",
        "android": "Android",
    }

    # Ignorar archivos no necesarios
    build.excludes = [
        "build/",
        "*.psd",
        "*.kra",
        "*.rpyc",
    ]

    # Directorios a excluir solo para DEMO
    DEMO_EXCLUDES = [
        "game/advanced_content/",
        "game/secret_endings/",
        "game/ao_scenes.rpy"
    ]

    # Ediciones disponibles
    ediciones = {
        "standard": {"edition": "Standard", "rated": "E", "type": "full"},
        "deluxe": {"edition": "Deluxe", "rated": "T", "type": "full"},
        "adult": {"edition": "Adult", "rated": "M", "type": "full"},
        "demo": {"edition": "Demo", "rated": "E", "type": "demo"}
    }

    # Plataformas de publicación
    mercados = {
        "steam": "Steam",
        "itch": "Itch.io",
        "general": "General"
    }

    # Versión 2.0: Crear variables específicas para GUI
    def crear_gui_variables(edition_key="standard", market_key="general", target=""):
        now = datetime.datetime.now()
        datos = ediciones.get(edition_key, ediciones["standard"])
        market = mercados.get(market_key, "General")
        
        # Determinar plataforma basada en target
        platform = PLATFORM_NAMES.get(target, "Multiplataforma")
        
        contenido = f"""\
# ARCHIVO GENERADO AUTOMÁTICAMENTE - NO MODIFICAR MANUALMENTE
# Variables específicas para la distribución: {edition_key}-{market_key}-{target}

define gui.year = "{now.year}"
define gui.developer = "TuNombreEstudio"
define gui.edition = "{datos['edition']}"
define gui.rated = "{datos['rated']}"
define gui.market = "{market}"
define gui.platform = "{platform}"
"""
        ruta_archivo = os.path.join("game", "gui_developer_variables.rpy")
        with open(ruta_archivo, "w", encoding="utf-8") as archivo:
            archivo.write(contenido)

    def comprimir_archivos():
        renpy.compile_script()
        renpy.store.persistent._compress_images = True

    def firmar_apk():
        renpy.android.build_apk(apk_path=None)

    def subir_itch(path, canal):
        try:
            subprocess.run(["butler", "push", path, canal], check=True)
        except Exception as e:
            renpy.say("Error al subir a Itch.io", str(e))

    def subir_steam():
        renpy.say("Subida a Steam no implementada directamente. Usa SteamCMD con tu AppID.")

    def build_distributions():
        for edition_key in ediciones.keys():
            # Configurar exclusiones específicas
            current_excludes = list(base_excludes)
            if ediciones[edition_key]["type"] == "demo":
                current_excludes.extend(DEMO_EXCLUDES)
            
            for market_key in mercados.keys():
                for target in build.targets:
                    crear_gui_variables(edition_key, market_key, target)
                    
                    # Aplicar exclusiones actualizadas
                    build.excludes = current_excludes
                    renpy.compile_script()
                    
                    nombre_base = f"{config.name}-{edition_key}-{market_key}-{target}-{config.version}"
                    build.directory_name = nombre_base
                    renpy.build(target)

                    output_path = os.path.join("build", build.directory_name)

                    if market_key == "itch":
                        canal = f"usuariojuego/{config.name}:{edition_key}-{target}"
                        subir_itch(output_path, canal)

                    elif market_key == "steam":
                        subir_steam()
                
                # Construir DLC si es necesario
                if "requires_dlc" in ediciones[edition_key]:
                    build_dlc(ediciones[edition_key]["requires_dlc"])


    def build_dlc(dlc_name):
        """Construye un DLC independiente"""
        dlc = dlc_config.get(dlc_name)
        if not dlc:
            renpy.say("Error", f"DLC {dlc_name} no configurado")
            return
        
        # Crear paquete DLC
        dlc_dir = os.path.join("dlc_build", dlc_name)
        os.makedirs(dlc_dir, exist_ok=True)
        
        # Copiar archivos
        for pattern in dlc["files"]:
            if os.path.isdir(pattern):
                shutil.copytree(pattern, os.path.join(dlc_dir, os.path.basename(pattern)))
            else:
                shutil.copy(pattern, dlc_dir)
        
        # Comprimir
        shutil.make_archive(f"build/{dlc_name}_dlc", 'zip', dlc_dir)
        renpy.say("Éxito", f"DLC {dlc_name} construido en build/{dlc_name}_dlc.zip")


# label build:
#     python:
#         build_distributions()

# label build_ao_dlc:
#     python:
#         build_dlc("ao_content")


# build.rpy (al final)
init python:
    def limpiar_archivos_temporales():
        temp_file = os.path.join("game", "gui_developer_variables.rpy")
        if os.path.exists(temp_file):
            os.remove(temp_file)