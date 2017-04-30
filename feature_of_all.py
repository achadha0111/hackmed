import subprocess
from subprocess import Popen, PIPE
import numpy as np

def extract_features():
	# sp.call(['/Applications/Praat.app/Contents/MacOS/Praat', '--run', 'script.praat'])
	# print(sp.check_output([]))
	p = Popen(['/Applications/Praat.app/Contents/MacOS/Praat', '--run', 'script2.praat'], stdout=subprocess.PIPE)
	output = p.stdout.read()
	arr = str(output).split("\\n")
	arr[0] = arr[0].replace("b'", "")
	del arr[-1]
	np.save("npyarrs/28.npy",np.array(arr).reshape(1, len(arr)))


extract_features()
