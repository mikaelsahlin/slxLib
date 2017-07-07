#!/usr/bin/env python3
import xml.etree.ElementTree as et
import sys
import os
#import argparse #To make input arguments... better than sys.arg...
#import xmltodict
#from dictdiffer import diff
import zipfile
#from difflib import unified_diff
def main():

# prints input argument...
  the_file = sys.argv[1]
  full_file = os.path.abspath(the_file)
  print(full_file)

#slxFile = zip.Zipfile(sys.argv[1])
  with zipfile.ZipFile(sys.argv[1],'r') as model:
    block_diag = str(model.read('simulink/blockdiagram.xml')).replace('\\t','\t').replace('.\\n','\n')
    print(model.read('simulink/blockdiagram.xml'))

#print(model.read('simulink/blockdiagram.xml'))

# create tree 
#tree = et.parse(full_file)
#root = tree.getroot()
  root = et.fromstring(block_diag)
  modelelement = root.find('Model')
  editList = modelelement.find('EditorSettings')# Returns empty lists
  sysDefList = modelelement.find('SystemDefaults')# Returns empty lists
  graphList = modelelement.find('Graphical')# Returns empty lists
  sysList = modelelement.find('System')# Returns empty lists
  flushSystemInfo('Outport',sysList)

def _flushSystemInfo(name,sysList)
  if issubclass(type(name),str)
    for its in sysList:
#  print(its.iterfind('Outport'))
      the_list = its.iterfind(args)
    return the_list
  else
    return ""

# how to print (to debug)?
# how to make new tree from subelements?

main()

