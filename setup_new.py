import sys

from cx_Freeze import *
includefiles= ["mana.ico"]
excludes=[]
packages=[]
base=None
if sys.platform =="win32":
    base ="Win32GUI"

shortcut_table= [
    ("DesktopShortcut",
     "DesktopFolder",
     "student_management_system",
     "TARGETDIR",
     "[TARGETDIR]\student_management_system.exe",

     None,
     None,
     None,
     None,
     None,
     None,
     "TARGETDIR"

    )
]

msi_data= {"Shortcut":shortcut_table}
bdist_msi_options ={'data': msi_data}
setup(
    version='0.1',
    description="Student management system developed by PRATIK PATIL",
    author="PRATIK PATIL",
    name="Student management system",
    options={'build.exe':{'inculde_files':includefiles},"bdist_msi":bdist_msi_options,},
    executables=[
        Executable(
            script="student_management_system.py",
            base=base,
            icon="mana.ico",
        )
    ]
)
