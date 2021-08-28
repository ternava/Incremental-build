
import subprocess

def read_time():
    with open("time.txt", "r") as file:
        for last_value in file:
            pass
        return last_value

def system_build_time(compile_time_opt):
    #subprocess.run(["make", "clean"])
    #subprocess.run(["make", "distclean"])
    subprocess.run(["./configure"] + compile_time_opt)

    # Calculates the bash time
    subprocess.run(["TIMEFORMAT='%4R %4U %4S' ; { time make 2> make.stderr ; } 2>> time.txt"], shell=True)
    
    # Calculates the GNU time
    # subprocess.run(["/usr/bin/time", "-pao", "time.txt", "--format=%e", "make"])

    # Get the build time from the file; it's the last value
    rus_time = read_time()
    tmp = rus_time.split(" ")
    tmp2 = [x.strip(' ') for x in tmp]
    three_time = [x.strip('\n') for x in tmp2]

    return three_time[0], three_time[1], three_time[2]