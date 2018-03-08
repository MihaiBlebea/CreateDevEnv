from open_program import OpenProgram
import json

'''
Get string from file
'''

json_data = open("tasks.json")
data = json.load(json_data)

'''
Init OpenProgram class
'''
open_program = OpenProgram( data )

'''
Start CLI flow with messages
'''
print("list      - get all programs available")
print("open      - select program to open from list")
print("open path - open a program from path")
print("exit      - exit the program \n")

loop = True
while loop == True:
    command = input("What do you want to do today? ")

    if command == "list":
        open_program.list_programs()

    elif command == "open":
        program = input("Please specify program to open from list: ")
        open_program.open(program)
        loop = False

    elif command == "open path":
        path = input("Please give me the path to the program executable: ")
        open_program.open_from_path(path)
        loop = False
        
    elif command == "exit":
        loop = False

    else:
        print("Command not found, please try again")
