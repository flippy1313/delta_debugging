import sys
import os
from subprocess import run
from subprocess import PIPE

def main(argv):
	os.chdir('libpng-1.6.34')
	run(["make" + " " + "clean;" + " " + "make"], shell = True)
	for png in argv:
		run(["./pngtest" + " large-png-suite/" + png + ".png"], shell = True)
	result = run(["gcov" + " " + "*.c"], shell = True, stdout=PIPE)
	result_str = str(result.stdout)
	result_split = result_str.split()
	coverage = result_split[-3][9:]
	print(coverage)
	if coverage >= "25%":
		return 1
	else:
		return 0


if __name__ == "__main__":
	main(sys.argv)
