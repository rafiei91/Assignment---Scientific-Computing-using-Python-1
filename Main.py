import argparse
import sys
import os

parser = argparse.ArgumentParser()
# Execution selection
parser.add_argument('--code_select', default='', type=str)
parser.add_argument('--case_number', default='0', type=str)

args = parser.parse_args()
code = args.code_select
case = args.case_number
c = int(case)

if (code == "case") & (c in range(1, 6, 1)):
  cwd = os.getcwd()
  cwd = cwd + "/" + code
  os.chdir(cwd)
  file_to_open = code + case + ".py"
  exec(open(file_to_open).read())
elif code == "test":
  cwd = os.getcwd()
  cwd = cwd + "/" + code
  os.chdir(cwd)
  os.system("python -m unittest -v")
else:
  print("Wrong input. \n code_select (case or test) \n case_number: 1 to 5")
  
