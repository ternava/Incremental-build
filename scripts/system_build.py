
import subprocess

from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp

def system_build_time(compile_time_opt):
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