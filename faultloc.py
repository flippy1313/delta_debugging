import sys
import math

def main(argv):
	passes = list()
	fails = list()
	read = list()
	totalfailed = 0
	ps = 0
	fs = 0
	for gcov in argv:
		if len(gcov) >= 4 and gcov[0:4] == "pass":
			passes.append(gcov)
		if len(gcov) >= 4 and gcov[0:4] == "fail":
			totalfailed += 1
			fails.append(gcov)
	with open(passes[0], 'r') as f:
		read = f.readlines()
	f.close()
	length = len(read)
	result = [{"p":0.0,"f":0.0, "line":-1} for i in range(length)]
	for pas in passes:
		with open(pas, 'r') as f:
			read = f.readlines()
		f.close()
		for i, lines in enumerate(read):
			lines = lines.split()
			execute = lines[0][:-1]
			line_num = lines[1].split(":")[0]
			if execute.isnumeric and execute > '0':
				result[i]["p"] += 1.
				result[i]["line"] = line_num
	for fail in fails:
		with open(fail, 'r') as f:
			read = f.readlines()
		f.close()
		for i, lines in enumerate(read):
			lines = lines.split()
			execute = lines[0][:-1]
			line_num = lines[1].split(":")[0]
			if execute.isnumeric and execute > '0':
				result[i]["f"] += 1.
				result[i]["line"] = line_num
	tuples = list()
	for i,cache in enumerate(result):
		denum = math.sqrt(totalfailed * (cache["f"] + cache["p"]))
		if denum != 0:
			tuples.append((int(cache["line"]),cache["f"]/math.sqrt(totalfailed * (cache["f"] + cache["p"]))))
	tuples.sort(key=lambda x:x[0])
	tuples.sort(reverse=True, key=lambda x:x[1])

	if length > 100:
		print(tuples[0:100])
	else:
		print(tuples)
if __name__ == "__main__":
	main(sys.argv)
