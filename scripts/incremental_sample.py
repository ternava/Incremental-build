import git 
import csv, sys

from system_build import i_system_build_time
from options import all_options, specialized_files
from binarysize import calculate_binary_size

#repo = git.Repo('/home/xternava/Documents/GitHub/curl-ib/')
repo = git.Repo('/github/curl/')


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

def incremental_build():
    for br in clean_build_branches:
        print(br)
        for finx, spec_file in enumerate(specialized_files):
            if(spec_file != br[5:]):
                print(br[5:])
                for idx, spec in enumerate(all_options):
                    if(idx == finx):
                        # To checkout the main starting branch
                        repo.git.checkout(br)

                        # Create a new branch
                        repo.git.branch('i'+ str(br) + '-' + str(spec_file))
                        # To checkout the branch after creating it, to use it
                        repo.git.checkout('i'+ str(br) + '-' + str(spec_file))

                        #repo.git.checkout(br, b='i'+ str(br) + '-' + str(spec_file)) 

                        print(repo.active_branch)
                        build_time = i_system_build_time(spec)
                        try:
                            #bs = calculate_binary_size("./src/curl")
                            bs = calculate_binary_size("/github/curl/src/curl")
                        except FileNotFoundError as e:
                             bs = -1

                        bt = [str(repo.active_branch), str(spec), build_time[0], build_time[1], build_time[2], bs]
                        writer.writerow(bt)

                        # stage all changes (i.e., object files) and commit
                        repo.git.add(all=True, force=True)
                        repo.index.commit('incremental build of icurl branch with ' + str(spec_file))

incremental_build()