from datetime import datetime

def set_current_year(context):
  context['_year'] = datetime.now().year

if __name__ == "__main__":
  import json

  vars_file = "cookiecutter.json"
  with open(vars_file, "r", encoding="utf-8") as f:
    context = json.load(f)

  set_current_year(context)
  
  with open(vars_file, "w", encoding="utf-8") as f:
    json.dump(context, f, indent=2)