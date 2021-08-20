import os.path
from os import path

def main():

    #path = '/home/xternava/Documents/GitHub/curl-ib/'
    path = '/github/curl/'
    if os.path.exists(str(path) + ".gitignore"):
        f_ignore = open(os.path.join(path, ".gitignore"), 'w')
        f_ignore.truncate()
        f_ignore.close()
    else: 
        with open(os.path.join(path, ".gitignore"), 'w') as fp:
            pass

if __name__== "__main__":
   main()