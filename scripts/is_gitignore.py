import os.path
from os import path

def remove_gitignore_content():

    path = '/github/curl/'
    if os.path.exists(str(path) + ".gitignore"):
        f_ignore = open(os.path.join(path, ".gitignore"), 'w')
        f_ignore.truncate()
        f_ignore.close()
    else: 
        with open(os.path.join(path, ".gitignore"), 'w') as fp:
            pass

remove_gitignore_content()