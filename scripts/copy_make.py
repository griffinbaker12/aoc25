from pathlib import Path

root = Path.cwd()
makefile_path = root / "Makefile"

day_dirs = [d for d in root.iterdir() if d.is_dir() and "day" in d.name.lower()]
for dir in sorted(day_dirs):
    dest_path = dir / "Makefile"
    dest_path.write_bytes(makefile_path.read_bytes())
    print(f"Created Makefile in {dir.name}")
