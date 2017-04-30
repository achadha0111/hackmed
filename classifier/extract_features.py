import subprocess
from subprocess import Popen, PIPE
import numpy as np

def extract_features():
	# sp.call(['/Applications/Praat.app/Contents/MacOS/Praat', '--run', 'script.praat'])
	# print(sp.check_output([]))
	p = Popen(['/Applications/Praat.app/Contents/MacOS/Praat', '--run', '../script.praat'], stdout=subprocess.PIPE)
	output = p.stdout.read()
	arr = str(output).split("\\n")
	arr[0] = arr[0].replace("b'", "")
	del arr[-1]
<<<<<<< HEAD:extract_features.py
	for a in arr:
		if a == "--undefined--":
			a = 0
=======
	arr.append(0)
	print ('Extracted features')
>>>>>>> 2a0638707897cbbf4f7bd1d4b8bb0663fe0f5d4e:classifier/extract_features.py
	return np.array(arr).reshape(1, len(arr))
	# command = ""
	# for i, value in enumerate(arr):
	# 	if i == len(arr)-1:
	# 		command += str(value)
	# 	else:
	# 		command += str(value) + ","

	# return command



