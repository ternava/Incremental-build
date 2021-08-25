import subprocess

from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp

def system_build_time(compile_time_opt):
    subprocess.run(["autoreconf", "-fi"])
    subprocess.run(["./configure", "--disable-shared"] + compile_time_opt)
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    proc2 = subprocess.Popen(["make"], stdout=subprocess.PIPE, stderr=subprocess.PIPE) # try to use: subprocess.run(["time"", "make", "-j8"]) with STDOUT  ; CC='ccache gcc' 
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()
    
    (stdout, stderr) = proc2.communicate()

    if proc2.returncode != 0:
        print(stderr)
        bt_real = -1
        bt_user = -1
        bt_sys = -1
    else:
        print("success")
        bt_real = f"{end_time - start_time:0.4f}"
        bt_user = f"{end_resources.ru_utime - start_resources.ru_utime:0.4f}"
        bt_sys = f"{end_resources.ru_stime - start_resources.ru_stime:0.4f}"
    
    return bt_real, bt_user, bt_sys

def i_system_build_time(compile_time_opt):
    subprocess.run(["./configure", "--disable-shared"] + compile_time_opt)
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    subprocess.run(["make"]) # try to use: subprocess.run(["time"", "make", "-j8"]) with STDOUT  ; CC='ccache gcc' 
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()
    
    bt_real = f"{end_time - start_time:0.4f}"
    bt_user = f"{end_resources.ru_utime - start_resources.ru_utime:0.4f}"
    bt_sys = f"{end_resources.ru_stime - start_resources.ru_stime:0.4f}"
    
    return bt_real, bt_user, bt_sys
