import subprocess
import os

os.environ['HOME'] = "C:\\Users\\Bryan"
os.environ['PATH'] += ";" + os.path.join(os.getcwd(), "_upload-site")

cmd = "rsync -rv -e ssh /cygdrive/c/Users/Bryan/Dropbox/bryanwweber.com/_site/"
cmd += " darthbith@bryanwweber.com:bryanwweber.com"


def execute(command):
    popen = subprocess.Popen(command, stdout=subprocess.PIPE)
    for line in popen.stdout:
        print(line.decode(), end='')  # yield line

execute(cmd.split(' '))
