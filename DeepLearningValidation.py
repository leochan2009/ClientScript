import subprocess

def RunValidataion(inputVolumeFileName, outputLableFileName):
	tempDir = os.path.join(os.path.realpath(__file__), '.tmp')
	deepInferDir = '/home/deepinfer/data'
	cmd = []
	cmd.extend(('/usr/local/bin/docker', 'run', '-t', '-v')) # TODO: adapt for Windows
	cmd.append(tempDir + ':' + deepInferDir)
	cmd.append('deepinfer/prostate-segmenter-cpu')
	cmd.extend(("--InputVolume", os.path.join(deepInferDir, inputVolumeFileName)))
	cmd.extend(("--OutputLabel", os.path.join(deepInferDir, outputLabelFileName)))
	p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
	