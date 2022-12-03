# Folder Commander

This script accepts a terminal command, and runs it on all immediate child directories, at depth = 1.

It does not run the command in deeply nested folders within folders, only the immediate one.

Why useful?

in all subfolders, you can `git init`, `git checkout feature_my_cat`, or even `rm -r tmp` .