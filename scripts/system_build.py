import subprocess

from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp

def system_build_time(compile_time_opt):
    subprocess.run(["autoreconf", "-fi"])
    subprocess.run(["./configure", "--disable-shared"] + compile_time_opt)
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    subprocess.run(["make"]) # try to use: subprocess.run(["time"", "make", "-j8"]) with STDOUT  ; CC='ccache gcc' 
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()
    
    bt_real = f"{end_time - start_time:0.4f}"
    bt_user = f"{end_resources.ru_utime - start_resources.ru_utime:0.4f}"
    bt_sys = f"{end_resources.ru_stime - start_resources.ru_stime:0.4f}"
    
    return bt_real, bt_user, bt_sys