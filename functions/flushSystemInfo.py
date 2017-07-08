#!/usr/bin/env python3
def flushSystemInfo(name,sysList):
  print("running flushSystemInfo")
  if issubclass(type(name),str):    
    for its in sysList:
      the_list = its.iterfind(name)
      return the_list    
  else:
    return ""
