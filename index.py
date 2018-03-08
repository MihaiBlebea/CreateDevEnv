from open_program import OpenProgram

'''
Create executable file: pyinstaller --onefile <your_script_name>.py
'''

tasks = [
    { "program" : "Laragon", "exe" : r"C:\Laragon\laragon.exe" },
    { "program" : "Atom", "exe" : r"C:\Users\Serban\AppData\Local\atom\atom.exe" },
    { "program" : "CommandLine", "exe" : r"C:\Cygwin\bin\mintty.exe" },
    { "program" : "Chrome", "exe" : r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" }
]

open_program = OpenProgram(tasks)
open_program.add_program({ "program" : "Chrome", "exe" : r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" })
open_program.add_script({ "script" : "Make directory", "exe": "mkdir CevaFrumos"})
open_program.run()
