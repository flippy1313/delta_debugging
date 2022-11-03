from subprocess import run
import sys
def convert(list_in):
	# Converter
	result = ""
	if not list_in:
		return result
	for num in list_in:
		result = result + str(num) + " "
	return result


def delta_recursive(script, previous, set_to_minimize):
	# Helper
	if len(set_to_minimize) == 1:
		return set_to_minimize
	else:
		list_to_minimize = list(set_to_minimize)
		set1 = set(list_to_minimize[:(len(set_to_minimize)//2)])
		set2 = set(list_to_minimize[(len(set_to_minimize)//2):])
		result_num1 = convert(list(set1 | previous))
		result_num2 = convert(list(set2 | previous))
		# 1
		result1 = run([script + " " + result_num1], shell = True)
		returncode1 = result1.returncode
		# 2
		result2 = run([script + " " + result_num2], shell = True)
		returncode2 = result2.returncode
		if returncode1 == 1:
			return delta_recursive(script, previous, set1)
		if returncode2 == 1:
			return delta_recursive(script, previous, set2)
		if returncode1 == 0 and returncode2 == 0:
			return delta_recursive(script, previous | set2, set1) | delta_recursive(script, previous | set1, set2)
		
def main(num, script):
	# Delta debugging
	previous = set()
	set_to_minimize = set(range(int(num)))
	result = list(delta_recursive(script, previous, set_to_minimize))
	#for i in range(len(result)):
	#	result[i] = str(result[i])
	print(sorted(result))
if __name__ == "__main__":
	main(sys.argv[1], sys.argv[2])


