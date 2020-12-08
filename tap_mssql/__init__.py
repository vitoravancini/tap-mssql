import subprocess
import sys
import os
from shutil import copyfile

def main():
    package_path = os.path.dirname(os.path.realpath(__file__))
    args = sys.argv[1:]
    for arg in args:
        if not arg.startswith('-'):
            index = args.index(arg)
            arg = os.path.abspath(arg)
            args[index] = arg
    cwd = package_path + "/tap-mssql"
    cmd = ['lein', 'run', '-m', 'tap-mssql.core']
    cmd = cmd + args

    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, cwd=cwd)
    for c in iter(lambda: process.stdout.read(1), b''):
        sys.stdout.write(c.decode('utf-8'))
    
    process.poll() # getting return code
    sys.exit(process.returncode)

if __name__ == "__main__":
    main()