import subprocess
from subprocess import Popen, PIPE
import numpy as np

def extract_features():
	# sp.call(['/Applications/Praat.app/Contents/MacOS/Praat', '--run', 'script.praat'])
	# print(sp.check_output([]))
	p = Popen(['/Applications/Praat.app/Contents/MacOS/Praat', '--run', 'script.praat'], stdout=subprocess.PIPE)
	output = p.stdout.read()
	arr = str(output).split("\\n")
	arr[0] = arr[0].replace("b'", "")
	del arr[-1]
	arr.append(0)
	return np.array(arr).reshape(1, len(arr))
	# command = ""
	# for i, value in enumerate(arr):
	# 	if i == len(arr)-1:
	# 		command += str(value)
	# 	else:
	# 		command += str(value) + ","

	# return command



