""" import subprocess

from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp

def system_build_time(compile_time_opt):
    # subprocess.run(["./buildconf"])
    subprocess.run(["autoreconf", "-fi"])
    subprocess.run(["./configure", "--with-openssl"] + compile_time_opt)
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    subprocess.run(["make"]) # try to use: subprocess.run(["time"", "make", "-j8"]) with STDOUT  ; CC='ccache gcc' 
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()
    
    bt_real = f"{end_time - start_time:0.4f}"
    bt_user = f"{end_resources.ru_utime - start_resources.ru_utime:0.4f}"
    bt_sys = f"{end_resources.ru_stime - start_resources.ru_stime:0.4f}"
    
    return bt_real, bt_user, bt_sys

def i_system_build_time(compile_time_opt):
    subprocess.run(["./configure", "--with-openssl"] + compile_time_opt)
    start_time, start_resources = timestamp(), resource_usage(RUSAGE_SELF)
    subprocess.run(["make"]) # try to use: subprocess.run(["time"", "make", "-j8"]) with STDOUT  ; CC='ccache gcc' 
    end_resources, end_time = resource_usage(RUSAGE_SELF), timestamp()
    
    bt_real = f"{end_time - start_time:0.4f}"
    bt_user = f"{end_resources.ru_utime - start_resources.ru_utime:0.4f}"
    bt_sys = f"{end_resources.ru_stime - start_resources.ru_stime:0.4f}"
    
    return bt_real, bt_user, bt_sys """

import subprocess, sys

from resource import getrusage as resource_usage, RUSAGE_SELF
from time import time as timestamp

def read_time():
    with open("time.txt", "r") as file:
        for last_value in file:
            pass
        return last_value

def system_build_time(compile_time_opt):
    #subprocess.run(["make", "clean"])
    #subprocess.run(["make", "distclean"])
    subprocess.run(["autoreconf", "-fi"])
    proca = subprocess.run(["./configure", "--with-openssl"] + compile_time_opt)

    # Calculates the bash time
    proc = subprocess.run(["TIMEFORMAT='%4R %4U %4S' ; { time make 2> make.stderr ; } 2>> time.txt"], shell=True)

    if ( proc.returncode == 0 & proc.returncode == 0 ):
        # Calculates the GNU time
        # subprocess.run(["/usr/bin/time", "-pao", "time.txt", "--format=%e", "make"])

        # Get the build time from the file; it's the last value
        rus_time = read_time()
        tmp = rus_time.split(" ")
        tmp2 = [x.strip(' ') for x in tmp]
        three_time = [x.strip('\n') for x in tmp2]
    else:
        three_time = [-1, -1, -1]


    return three_time[0], three_time[1], three_time[2]

def i_system_build_time(compile_time_opt):
    subprocess.run(["./configure", "--with-openssl"] + compile_time_opt)

    # Calculates the bash time
    proc = subprocess.run(["TIMEFORMAT='%4R %4U %4S' ; { time make 2> make.stderr ; } 2>> time.txt"], shell=True)

    if ( proc.returncode == 0 ):
        # Calculates the GNU time
        # subprocess.run(["/usr/bin/time", "-pao", "time.txt", "--format=%e", "make"])

        # Get the build time from the file; it's the last value
        rus_time = read_time()
        tmp = rus_time.split(" ")
        tmp2 = [x.strip(' ') for x in tmp]
        three_time = [x.strip('\n') for x in tmp2]
    else:
        three_time = [-1, -1, -1]


    return three_time[0], three_time[1], three_time[2]