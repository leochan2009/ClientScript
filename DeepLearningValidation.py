import subprocess, os
import shutil
class ClientValidationObject(object):
  def __init__(self):
    pass
  def RunValidataion(self, inputVolumeFile, outputLabelFile):
    executeDir = os.path.join(os.path.abspath(os.path.join(inputVolumeFile, os.pardir)), '.tmp')
    if not os.path.exists(executeDir):
      os.mkdir(executeDir)
    shutil.copyfile(inputVolumeFile, os.path.join(executeDir,"MRProstate.nrrd"))
    deepInferDir = '/home/deepinfer/data'
    cmd = []
    cmd.extend(('/usr/local/bin/docker', 'run', '-t', '-v'))
    cmd.append(executeDir + ':' + deepInferDir)
    cmd.append('deepinfer/prostate-segmenter-cpu')
    cmd.extend(("--InputVolume", os.path.join(deepInferDir, "MRProstate.nrrd")))
    cmd.extend(("--OutputLabel", os.path.join(deepInferDir, "ResultLabel.nrrd")))
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    for line in p.stdout:
      print line
    p.wait()
    shutil.copyfile(os.path.join(executeDir, "ResultLabel.nrrd"), outputLabelFile)
    shutil.rmtree(executeDir)
    print "Validation finished"