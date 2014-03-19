import os
from glob import glob
from subprocess import call


def main():
    script_path = os.path.dirname(os.path.realpath(__file__))
    weeks = glob(script_path + "/Week_*")
    for week_path in weeks:
        solutions_dirs = glob(week_path + "/*/")
        for solution_dir in solutions_dirs:
            tests = glob(solution_dir + "/*tests.py")
            if len(tests) == 0:
                continue
            os.chdir(solution_dir)  # in case any test creates and messes with some files
            for test in tests:
                call("py " + test, shell=True)


if __name__ == '__main__':
    main()
