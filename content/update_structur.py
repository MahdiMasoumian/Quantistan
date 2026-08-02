import subprocess
from pathlib import Path


PROJECT_PATH = Path(r"C:\Users\Mahdi\quantistan\content")
OUTPUT_FILE = PROJECT_PATH / "structure.txt"


def update_structure():

    subprocess.run(
        ["cmd", "/c", "tree", "/F", ">", str(OUTPUT_FILE)],
        cwd=PROJECT_PATH,
        shell=True
    )

    print("Project structure updated.")


if __name__ == "__main__":
    update_structure()
