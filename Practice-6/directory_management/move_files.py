from pathlib import Path
import shutil

source = Path("Top Secret/Expedition/Reports.txt")
destination = Path("Top Secret/Backups/Reports.txt")

shutil.move(source, destination)
