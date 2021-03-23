#!/usr/bin/env python
import sys
import os

RED='\033[0;31m'    # bunch of colours
GREEN='\033[0;32m'
BLUE='\033[0;34m'
LBUE='\033[1;34m'
OR='\033[0;33m'
PURP='\033[0;35m'
NC='\033[0m'

def runAll(targets, scripts):
    for t in targets:
        print("\n" + PURP + "########"+OR+" Target: "+ t + NC + "\n")
        for s in scripts:
            print("\n" + PURP + "####" + LBUE + " Running: " + s + NC + "\n")
            os.system(s + " " + t)
    print(RED + "##################################################")
    print("###################### END #######################" + NC + "\n")


if __name__ == "__main__":
  if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " <path/to/targets> <path/to/scripts>\n")
    sys.exit(-1)

  print(GREEN + "#################### STARTING ####################")
  print("##################################################" + NC)

  try:
    print("Targets File: " + str(sys.argv[1]))
    print("Scripts File: " + str(sys.argv[2]))
    f = open(sys.argv[1], 'r') # parse targets into list, sepearate by new line
    targets = f.readlines()
    targets = [x.strip() for x in targets] 
    f.close()
    f = open(sys.argv[2], 'r') # parse scripts into list
    scripts = f.readlines()
    scripts = [x.strip() for x in scripts] 
    runAll(targets, scripts)
  except Exception as e:
    print("An exception occurred\n" + str(e))