import cx_Freeze

cx_Freeze.setup(
    name="Chico bomba",
    version="1.0.0",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["assets/"]}
             },
    executables=[cx_Freeze.Executable("main.py")]
)
