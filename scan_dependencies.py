import ast
import sys
from pathlib import Path
import importlib.util

project_root = Path(".")

std_lib = set(sys.stdlib_module_names)

third_party = set()

for file in project_root.rglob("*.py"):
    try:
        tree = ast.parse(file.read_text(encoding="utf-8"))

        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for n in node.names:
                    name = n.name.split(".")[0]
                    third_party.add(name)

            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    name = node.module.split(".")[0]
                    third_party.add(name)

    except Exception:
        pass

# FILTER STEP (critical)
clean = set()

for mod in third_party:
    if mod in std_lib:
        continue
    if mod.startswith("_"):
        continue

    # check if it's actually installed package
    spec = importlib.util.find_spec(mod)
    if spec and "site-packages" in (spec.origin or ""):
        clean.add(mod)

print("\n=== CLEAN REQUIREMENTS CANDIDATES ===")
for m in sorted(clean):
    print(m)