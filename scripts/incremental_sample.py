import git 
import csv

from system_build import system_build_time
from options import all_options, specialized_files
from binarysize import calculate_binary_size

#repo = git.Repo('/home/xternava/Documents/GitHub/xz-ib/')
repo = git.Repo('/github/xz/')

header = ['Branch', 'Option', 'bt_real', 'bt_user', 'bt_sys', 'BinarySize']
#f = open('/home/xternava/Documents/GitHub/Incremental-build/data/buildtime_i2.csv', 'w')
f = open('/src/data/buildtime_di1.csv', 'w')
writer = csv.writer(f)
writer.writerow(header)

# Add all clean build branches to a list, 
# so only those branches are incrementaly build
clean_build_branches = []

for branch in repo.branches:
    if(branch.name[3:] in specialized_files):
        clean_build_branches.append(branch.name)

print(clean_build_branches)

def incremental_build():
    for br in clean_build_branches:
        print(br)
        for finx, spec_file in enumerate(specialized_files):
            if(spec_file != br[3:]):
                print(br[3:])
                for idx, spec in enumerate(all_options):
                    if(idx == finx):
                        # To checkout the main branch
                        repo.git.checkout(br)

                        # Create a new branch
                        repo.git.branch('i'+ str(br) + '-' + str(spec_file))
                        # To checkout the branch after creating it, to use it
                        repo.git.checkout('i'+ str(br) + '-' + str(spec_file))

                        print(repo.active_branch)
                        build_time = system_build_time(spec)
                        try:
                            #bs = calculate_binary_size("./src/xz/xz")
                            bs = calculate_binary_size("/github/xz/src/xz/xz")
                        except FileNotFoundError as e:
                            bs = -1
                        bt = [str(repo.active_branch), str(spec), build_time[0], build_time[1], build_time[2], bs]
                        writer.writerow(bt)

                        # stage all changes (i.e., object files) and commit
                        repo.git.add(all=True, force=True)
                        repo.index.commit('incremental build of ixz branch with ' + str(spec_file))

incremental_build()