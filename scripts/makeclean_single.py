import git 
import csv

from system_build import system_build_time
from binarysize import calculate_binary_size

# You need to provide the path to the repo of your project
#repo = git.Repo('/home/xternava/Documents/GitHub/curl-ib/')
repo = git.Repo('/github/curl/')

# List all branches
""" for branch in repo.branches:
    print(branch)
 """
# Delete all existing branches: git branch | grep -v "master" | xargs git branch -D

# Used options for a minimal configuration in curl
min_ct_options = ["--disable-ares","--disable-cookies","--disable-ipv6","--disable-manual"]
    
lst_options = min_ct_options[:]

# You need to provide the path to the repo where you want to save the results
#f = open('/home/xternava/Documents/GitHub/Incremental-build/data/buildtime_s1.csv', 'w')
f = open('/src/data/buildtime_dc1.csv', 'w')
header = ['Branch', 'Option', 'bt_real', 'bt_user', 'bt_sys', 'BinarySize']
writer = csv.writer(f)
writer.writerow(header)

def clean_build_minimal():
    # To checkout the main branch
    repo.git.checkout('master')

    # Create the minimal new branch
    repo.git.branch('curl-minimal')
    repo.git.checkout('curl-minimal')

    # The project in the minimal branch is compiled and commited
    build_time_1 = system_build_time(min_ct_options)
    #bsm = calculate_binary_size("./curl")
    bsm = calculate_binary_size("/github/curl/src/curl")

    bt = [str(repo.active_branch.name), str(min_ct_options), build_time_1[0], build_time_1[1], build_time_1[2], bsm]
    writer.writerow(bt)

    print(repo.active_branch.name)

    repo.git.add(all=True)
    repo.index.commit('clean build curl minimal')

def clean_build():
    # we remove one option at e time from the minimal configuration,
    # create a branch with its name from the 'master' and then 
    # compile the project with the remained options in the set and commit it
    for opt in lst_options:
        # To checkout the master branch
        repo.git.checkout('master')

        # Create a new branch
        repo.git.branch('curl'+ opt[1:])

        # To checkout the branch after creating it, to use it
        repo.git.checkout('curl'+ opt[1:])

        # Copy the list with minimal "configuration"
        lst = min_ct_options[:] 

        # Remove the option used to create the branch
        lst.remove(opt) 

        build_time_2  = system_build_time(lst)
        #bs = calculate_binary_size("./curl")
        bs = calculate_binary_size("/github/curl/src/curl")

        bt = [str(repo.active_branch.name), str(opt), build_time_2[0], build_time_2[1], build_time_2[2], bs]
        writer.writerow(bt)

        repo.git.add(all=True, force=True)
        repo.index.commit('clean build curl minimal without ' + opt[1:])

def main():
    clean_build_minimal()
    clean_build()

if __name__== "__main__":
   main()