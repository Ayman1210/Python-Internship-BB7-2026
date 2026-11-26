from pathlib import Path
import shutil

# Find the Python folder
root = Path.cwd()

if (root / "Python").is_dir():
    base = root / "Python"
else:
    base = root

# Day-wise topic and file mapping
organization = {
    "Day3": {
        "Dictionary": ["dic*.py"],
        "List": ["list*.py"]
    },
    "Day4": {
        "Tuple": ["tuple*.py"]
    },
    "Day5": {
        "Functions": ["func*.py"]
    },
    "Day6": {
        "Closures": ["cl*.py"],
        "Scope": ["scope*.py"],
        "Exception_Handling": ["eh*.py"]
    },
    "Day7": {
        "OOP_Concepts": ["oop*.py"]
    },
    "Day8": {
        "Inheritance_and_Polymorphism": ["in*.py"]
    },
    "Day9": {
        "Encapsulation_and_Magic_Methods": ["enc*.py"]
    }
}

print("Python Internship Folder Organizer")
print("-----------------------------------")

# Show planned changes
for day, topics in organization.items():
    print(f"\n{day}:")
    for folder, patterns in topics.items():
        files = []
        for pattern in patterns:
            files.extend((base / day).glob(pattern))

        print(f"  {folder}: {len(files)} files")

confirm = input("\nMove all these files? (yes/no): ")

if confirm.lower() != "yes":
    print("Operation cancelled.")
else:
    total = 0

    for day, topics in organization.items():
        day_path = base / day

        if not day_path.is_dir():
            continue

        for folder, patterns in topics.items():
            destination = day_path / folder

            for pattern in patterns:
                for file in day_path.glob(pattern):
                    if not file.is_file():
                        continue

                    destination.mkdir(
                        parents=True, exist_ok=True
                    )

                    target = destination / file.name

                    if target.exists():
                        print(f"Skipped: {file.name}")
                        continue

                    shutil.move(str(file), str(target))
                    print(f"Moved: {day}/{file.name}")
                    total += 1

    print("\nSuccessfully organized!")
    print("Total files moved:", total)