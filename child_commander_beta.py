import os
import subprocess  # https://queirozf.com/entries/python-3-subprocess-examples

# run() requires list, with final element being directory command is run in
# hence the append and pop()
command = "touch cat.txt"
command = command.split()

currentpath = os.path.realpath(__file__)  # or os.path.abspath(__file__)
# split into path and filename. I want only path
currentpath = os.path.split(os.path.abspath(currentpath))[0]  # /path/file.py


# def git_children_dirs(currentpath=currentpath, command=command):
# get immediate child folders
immediate_subfolder = next(os.walk(currentpath))[1]

subfolders = []
for sub in immediate_subfolder:
    subfolder = os.path.join(currentpath, sub)
    subfolders.append(subfolder)

for subfolder in subfolders:
    command.append(subfolder)
    print(command)
    result = subprocess.run(command, capture_output=True, text=True)
    print('stdout: ', result.stdout)
    print('stderr: ', result.stderr)
    command.pop()


# git_children_dirs(currentpath, command)
