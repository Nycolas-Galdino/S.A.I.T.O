from cx_Freeze import setup, Executable


exe_opt = {"packages": ["os", "sys", "json", "pyttsx3", "pywhatkit","requests", "speech_recognition", "webbrowser", "wikipedia", "actions", "config"],
           "include_files":["User.txt", "Saito.reg", "Dicionário.json"],
           "replace_paths":[("*","")],
           "optimize": 1,}



setup(
    name="Saito IA",
    version="2.1.1",
    description="The Saito Inteligence Artificial",
    options={"build_exe": exe_opt},
    executables=[Executable(
            "main.py",
            copyright="Copyright reserved by Nycolas Pimentel Galdino 2022",
            base=None,
            icon="icon.ico",
            shortcut_name="Saito Inteligente Artificial",
            shortcut_dir="SaitoIA")],
)