from module import Module
from typing import Dict
import sys


modules: Dict[str, Module] = {
    # Add modules here
}


if len(sys.argv) == 1:
    print("Usage: python main.py <module_name>")
    print("Available modules:")
    for name, module in modules.items():
        print(f"\t{name}: {module.description}")
    sys.exit()

module_name = sys.argv[1]
if module_name not in modules:
    print(f"Module {module_name} not found")
    sys.exit(1)

module = modules[module_name]
module.prepare_dataset()
module.train_model()
module.evaluate_model()
