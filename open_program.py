import subprocess
import os

class OpenProgram:

    def __init__(self, tasks = None):
        self.tasks = tasks

    def add_program(self, task):
        if "program" and "exe" in task:
            self.tasks.append(task)

    def add_script(self, task):
        if "script" and "exe" in task:
            self.tasks.append(task)

    def open_from_path(self, path):
        subprocess.Popen([ path ])
        message = "Task {} has started".format(path)
        print(message)

    def list_programs(self):
        for index, task in enumerate(self.tasks):
            message = "{}. {}".format(index + 1, task["program"])
            if index == ( len(self.tasks) - 1 ):
                print(message + "\n")
            else:
                print(message)

    def open(self, selected):
        for task in self.tasks:
            if task["program"] == selected:
                subprocess.Popen([ task["exe"] ])
                message = "Task {} has started".format(task["program"])
                print(message)

    def run(self):
        for index, task in enumerate(self.tasks):
            if "program" in task:
                subprocess.Popen([ task["exe"] ])
            else:
                os.system( task["exe"] )

            message = "{}. Task {} has started".format(index + 1, task["program"])
            print(message)
