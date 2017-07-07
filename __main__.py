#!/usr/bin/env python3
import xml.etree.ElementTree as et
import sys
import os
import zipfile
from functions import *
from slxFile import *

def main():
  the_file = sys.argv[1]
  full_file = os.path.abspath(the_file)
  print(full_file)

  slxFile = zipfile.ZipFile(sys.argv[1],'r')
  alist = listFileContent(slxFile)

  print("##################THE CONTENT OF THE SLX FILE IS##################")
  for it in alist:
    print(it)
  print("##################################################################")

  with slxFile as model:
    alist = model.namelist()
    block_diag = str(model.read('simulink/blockdiagram.xml')).replace('\\t','\t').replace('.\\n','\n')

  root = et.fromstring(block_diag)
  modelelement = root.find('Model')
  editList = modelelement.find('EditorSettings')
  sysDefaultList = modelelement.find('SystemDefaults')
  graphList = modelelement.find('Graphical')
  sysList = modelelement.find('System')
  outputs = flushSystemInfo('Outport',sysList)
    
#Works this far.
  return outputs

if __name__ == '__main__':
  main()
