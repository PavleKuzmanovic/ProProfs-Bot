from cx_Freeze import setup, Executable

base = None    

executables = [Executable("ProProfsScripterPro.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "ProProfsPro",
    options = options,
    version = "1.0",
    description = 'ProProfs Scripting Bot',
    executables = executables
)