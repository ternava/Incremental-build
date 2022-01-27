import glob
import ntpath

# Add considered sets with configurations
sample_configurations = []
specialized_files = []

def path_leaf(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)

def spec_to_array():
    
    """     Here you can chose which Batch with configurations you want to use.
        Batch 1: set the path to "/src/configurations/sample-03/*.config"
        Batch 2: set the path to "/src/configurations/sample-04/*.config" """
        
    for variant in glob.glob("/src/configurations/sample-04/*.config"):
        specialized_files.append(path_leaf(variant[:-7]))
        lineList = list()
        with open(variant) as f:
            for line in f:
                lineList = [line.rstrip('\n') for line in open(variant)]
            sample_configurations.append(lineList)

spec_to_array()
all_options =  [*sample_configurations]