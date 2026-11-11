import importlib
import pkgutil

import app

failed = False
for module in pkgutil.walk_packages(app.__path__, "app."):
    try:
        importlib.import_module(module.name)
    except Exception as error:
        failed = True
        print(f"FAILED  {module.name}: {error}")

print("Fix the files listed above." if failed else "All modules import correctly.")