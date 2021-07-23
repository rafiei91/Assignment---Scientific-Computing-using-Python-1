import argparse

def get_args_parser():
  # Execution selection
  parser.add_argument('--code_select', default='')
  
def main(args):
  code = arg.code_select
  sys.path.append('/ "code"')
  execfile('"code".py')
  
if __name__ == '__main__':
  main(args)
