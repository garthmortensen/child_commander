import os
import subprocess  # https://queirozf.com/entries/python-3-subprocess-examples

command = 'echo mr president, i am only a cat > cat.txt'


def run_child_command(command):
    """Provide a bash command to be run on all immediate child directories,
    That is, this is not recursive 5 nested directories down. Just depth=1.
    """
    currentpath = os.path.realpath(__file__)  # or os.path.abspath(__file__)
    # split into path and filename. I want only path
    currentpath = os.path.split(os.path.abspath(currentpath))[0]  # /path/file.py
    
    # def git_children_dirs(currentpath=currentpath, command=command):
    # get child folders, only 1 depth deep
    immediate_subfolder = next(os.walk(currentpath))[1]
    subfolders = []
    for sub in immediate_subfolder:
        subfolder = os.path.join(currentpath, sub)
        subfolders.append(subfolder)
    
    # execute command in all child folders
    for subfolder in subfolders:
        print(f"subfolder: {subfolder}")
        result = subprocess.run(command,
                                cwd=subfolder,  # current dir to execute cmd
                                capture_output=True,  # output stdout, stderr
                                text=True,  # outputs str, not bytes
                                shell=True)  # allows space seperated, not []
        print('stdout: ', result.stdout)
        print('stderr: ', result.stderr)


git_child_dirs(command)
