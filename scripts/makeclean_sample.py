import git 
import csv

from system_build import system_build_time
from options import all_options, specialized_files
from binarysize import calculate_binary_size

#repo = git.Repo('/home/xternava/Documents/GitHub/xz-ib/')
repo = git.Repo('/github/xz/')

print(all_options)

header = ['Branch', 'Option', 'bt_real', 'bt_user', 'bt_sys', 'BinarySize']
#f = open('/home/xternava/Documents/GitHub/Incremental-build/data/buildtime_s2.csv', 'w')
f = open('/src2/data/buildtime_dc2.csv', 'w')
writer = csv.writer(f)
writer.writerow(header)

# To checkout the main branch
repo.git.checkout('master')

# Create the minimal new branch, just copy the master one
repo.git.branch('xz-mcopy')


def clean_build():
    for idx, spec in enumerate(all_options):
        for finx, spec_file in enumerate(specialized_files):
            if(idx == finx):
                # To checkout the main branch
                repo.git.checkout('xz-mcopy')

                # Create a new branch
                repo.git.branch('xz-'+ str(spec_file))
                # To checkout the branch after creating it, to use it
                repo.git.checkout('xz-'+ str(spec_file))

                build_time  = system_build_time(spec)
                #bs = calculate_binary_size("./src/xz/xz")
                bs = calculate_binary_size("/github/xz/src/xz/xz")
                bt = [str(repo.active_branch), str(spec), build_time[0], build_time[1], build_time[2], bs]
                writer.writerow(bt)

                # stage all changes (i.e., object files) and commit
                repo.git.add(all=True, force=True)
                repo.index.commit('clean build xz master copy with ' + str(spec_file))

def main():
    clean_build()

if __name__== "__main__":
   main()