# Child Commander

Got children directories? This script accepts a terminal command, and runs it on all immediate child directories, depth = 1.

That is, it does not run the command in deeply nested folders within folders, only immediate one.

Why useful?

in all subfolders, you can `git init`, `git checkout feature_my_cat`, or even `rm -r tmp` .