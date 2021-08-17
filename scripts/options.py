import glob
import ntpath

# Add considered sets with configurations
sample_configurations = []
specialized_files = []

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def spec_to_array():
    #for variant in glob.glob("/home/xternava/Documents/GitHub/Incremental-build/x264-sample-configurations/sample-02/*.config"):
    for variant in glob.glob("/src/x264-sample-configurations/sample-02/*.config"):
        specialized_files.append(path_leaf(variant[:-7]))
        lineList = list()
        with open(variant) as f:
            for line in f:
                lineList = [line.rstrip('\n') for line in open(variant)]
            sample_configurations.append(lineList)

spec_to_array()
all_options =  [*sample_configurations]