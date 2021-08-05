import git 
import subprocess
import csv


from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp
from options import all_options, specialized_files
from binarysize import calculate_binary_size

#repo = git.Repo('/home/xternava/Documents/GitHub/x264-ib/')
repo = git.Repo('/GitHub/x264/')

def compilex264(compile_time_opt):
    
    subprocess.run(["./configure"] + compile_time_opt)
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    subprocess.run(["make"]) # try to use: subprocess.run(["time"", "make", "-j8"]) with STDOUT  ; CC='ccache gcc' 
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()
    
    bt_real = f"{end_time - start_time:0.4f}"
    bt_user = f"{end_resources.ru_utime - start_resources.ru_utime:0.4f}"
    bt_sys = f"{end_resources.ru_stime - start_resources.ru_stime:0.4f}"
    
    return bt_real, bt_user, bt_sys


header = ['Branch', 'Option', 'bt_real', 'bt_user', 'bt_sys', 'BinarySize']
#f = open('/home/xternava/Documents/GitHub/Incremental-build/data/buildtime_i2.csv', 'w')
f = open('/src/data/buildtime_di1.csv', 'w')
writer = csv.writer(f)
writer.writerow(header)

# Add all clean build branches to a list, 
# so only those branches are incrementaly build
clean_build_branches = []

for branch in repo.branches:
    if(branch.name[5:] in specialized_files):
        clean_build_branches.append(branch.name)

print(clean_build_branches)

for br in clean_build_branches:
    print(br)
    for finx, spec_file in enumerate(specialized_files):
        if(spec_file != br[5:]):
            print(br[5:])
            for idx, spec in enumerate(all_options):
                if(idx == finx):
                    # To checkout the main branch
                    repo.git.checkout(br)

                    # Create a new branch
                    repo.git.branch('i'+ str(br) + '-' + str(spec_file))
                    # To checkout the branch after creating it, to use it
                    repo.git.checkout('i'+ str(br) + '-' + str(spec_file))

                    print(repo.active_branch)
                    build_time = compilex264(spec)
                    bs = calculate_binary_size("./x264")
                    bt = [str(repo.active_branch), str(spec), build_time[0], build_time[1], build_time[2], bs]
                    writer.writerow(bt)

                    # stage all changes (i.e., object files) and commit
                    repo.git.add(all=True)
                    repo.index.commit('incremental build of ix264 branch with ' + str(spec_file))