import git 
import subprocess
import csv

from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp
from options import all_options, specialized_files
from binarysize import calculate_binary_size

#repo = git.Repo('/home/xternava/Documents/GitHub/x264-ib/')
repo = git.Repo('/github/x264/')

# Delete all existing branches: git branch | grep -v "master" | xargs git branch -D

print(all_options)

def compilex264(compile_time_opt):
    #subprocess.run(["make", "clean"])
    #subprocess.run(["make", "distclean"]) 
    subprocess.run(["./configure"] + compile_time_opt)
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    subprocess.run(["make"]) # try to use: subprocess.run(["time"", "make", "-j8"]) with STDOUT  ; CC='ccache gcc' 
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()
    
    bt_real = f"{end_time - start_time:0.4f}"
    bt_user = f"{end_resources.ru_utime - start_resources.ru_utime:0.4f}"
    bt_sys = f"{end_resources.ru_stime - start_resources.ru_stime:0.4f}"
    
    return bt_real, bt_user, bt_sys

header = ['Branch', 'Option', 'bt_real', 'bt_user', 'bt_sys', 'BinarySize']
#f = open('/home/xternava/Documents/GitHub/Incremental-build/data/buildtime_s2.csv', 'w')
f = open('/src/data/buildtime_dc2.csv', 'w')
writer = csv.writer(f)
writer.writerow(header)

# To checkout the main branch
repo.git.checkout('master')

# Create the minimal new branch, just copy the master one
repo.git.branch('x264-mcopy')



for idx, spec in enumerate(all_options):
    for finx, spec_file in enumerate(specialized_files):
        if(idx == finx):
            # To checkout the main branch
            repo.git.checkout('x264-mcopy')

            # Create a new branch
            repo.git.branch('x264-'+ str(spec_file))
            # To checkout the branch after creating it, to use it
            repo.git.checkout('x264-'+ str(spec_file))

            build_time  = compilex264(spec)
            bs = calculate_binary_size("/github/x264/x264")
            bt = [str(repo.active_branch), str(spec), build_time[0], build_time[1], build_time[2], bs]
            writer.writerow(bt)

            # stage all changes (i.e., object files) and commit
            repo.git.add(all=True)
            repo.index.commit('clean build x264 master copy with ' + str(spec_file))