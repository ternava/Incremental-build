import git 
import subprocess
import csv

from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp
from binarysize import calculate_binary_size

# You need to provide the path to the repo of your project
repo = git.Repo('/home/xternava/Documents/GitHub/x264-ib/')

# List all branches
""" for branch in repo.branches:
    print(branch)
 """
# Delete all existing branches: git branch | grep -v "master" | xargs git branch -D

# Used options for a minimal configuration in x264
min_ct_options = ["--disable-asm", "--disable-bashcompletion", "--disable-opencl", "--disable-gpl", "--disable-thread", 
    "--disable-win32thread", "--disable-interlaced", "--bit-depth=8", "--chroma-format=400"]
    
lst_options = min_ct_options[:]

def compilex264(compile_time_opt):
    #subprocess.run(["make", "clean"])
    #subprocess.run(["make", "distclean"])
    subprocess.run(["./configure"] + compile_time_opt)
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    subprocess.run(["make"])
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()
    
    # Calculates three times, just like the 'time' command in unix
    bt_real = f"{end_time - start_time:0.4f}"
    bt_user = f"{end_resources.ru_utime - start_resources.ru_utime:0.4f}"
    bt_sys = f"{end_resources.ru_stime - start_resources.ru_stime:0.4f}"
    
    return bt_real, bt_user, bt_sys

# You need to provide the path to the repo where you want to save the results
f = open('/home/xternava/Documents/GitHub/Incremental-build/data/buildtime_s1.csv', 'w')
header = ['Branch', 'Option', 'bt_real', 'bt_user', 'bt_sys', 'BinarySize']
writer = csv.writer(f)
writer.writerow(header)

# To checkout the main branch
repo.git.checkout('master')

# Create the minimal new branch
repo.git.branch('x264-minimal')
repo.git.checkout('x264-minimal')

# The project in the minimal branch is compiled and commited
build_time_1 = compilex264(min_ct_options)
bsm = calculate_binary_size("./x264")

bt = [str(repo.active_branch.name), str(min_ct_options), build_time_1[0], build_time_1[1], build_time_1[2], bsm]
writer.writerow(bt)

print(repo.active_branch.name)

repo.git.add(all=True)
repo.index.commit('clean build x264 minimal')

# we remove one option at e time from the minimal configuration,
# create a branch with its name from the 'master' and then 
# compile the project with the remained options in the set and commit it
for opt in lst_options:
    # To checkout the master branch
    repo.git.checkout('master')

    # Create a new branch
    repo.git.branch('x264'+ opt[1:])

    # To checkout the branch after creating it, to use it
    repo.git.checkout('x264'+ opt[1:])

    # Copy the list with minimal "configuration"
    lst = min_ct_options[:] 

    # Remove the option used to create the branch
    lst.remove(opt) 

    build_time_2  = compilex264(lst)
    bs = calculate_binary_size("./x264")

    bt = [str(repo.active_branch.name), str(opt), build_time_2[0], build_time_2[1], build_time_2[2], bs]
    writer.writerow(bt)

    repo.git.add(all=True)
    repo.index.commit('clean build x264 minimal without ' + opt[1:])