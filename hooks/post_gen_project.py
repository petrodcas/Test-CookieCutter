from collections import OrderedDict

def get_all_conditional_removable_dirs(context):
  return [key for key, value in context.items() if key.endswith('_dir') and key.startswith('include_') and value is False]

if __name__ == '__main__':
  import os
  context = {{cookiecutter}}
  for dir in get_all_conditional_removable_dirs(context):
    dir_path = dir.replace('_dir', '').replace('include_', '')
    os.rmdir(dir_path)