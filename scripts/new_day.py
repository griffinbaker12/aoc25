import json
from pathlib import Path
import sys

project_root = Path.cwd()
json_path = project_root / "scripts" / "day.json"

with open(json_path, "r") as f:
    data = json.load(f)
    day_number = data["day_number"]

new_day_dir = project_root / f"day_{day_number:02d}"

if new_day_dir.exists():
    print(f"Error: Directory for day {day_number} already exists!")
    sys.exit(1)  # Exit with error code 1

new_day_dir.mkdir()

for file_name in ("main.py", "input.txt", "test.txt"):
    (new_day_dir / file_name).touch()

data["day_number"] = day_number + 1
with open(json_path, "w") as f:
    json.dump(data, f)

print(f"Created directory for day {day_number} with main.py, input.txt, and test.txt")
