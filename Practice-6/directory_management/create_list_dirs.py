from pathlib import Path

# Create nested directories
base = Path("Top Secret")

folders = [
	base / "Dr.Clara Veyra" / "Works",
	base / "Expedition" / "Casualties",
	base / "Images",
	base / "Backups"
]

for folder in folders:
    folder.mkdir(parents=True, exist_ok=True)

# List files and folders
folder  = Path("Top Secret")
print("Files: ")
for item in folder.iterdir():
	print(item.name)
print('\n')

# Find files by extension
print("txt files inside of Top Secret/Expedition")
folder  = Path("Top Secret/Expedition")
for file in folder.glob("*.txt"):
	print(file.name)
