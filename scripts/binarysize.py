import os

# Is used to calculate the binary size of an executable
def calculate_binary_size(exe_name):
    exe_stats = os.stat(exe_name)
    print(exe_stats)
    exe_size = exe_stats.st_size
    return exe_size