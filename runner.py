import sys
import subprocess
from pathlib import Path


def run_pytest(test_path):

    command = [
        sys.executable,
        "-m",
        "pytest",
        "-v",
        "-s",
        test_path
    ]

    subprocess.run(command)


if __name__ == "__main__":

    if len(sys.argv) > 1:
        test_path = sys.argv[1]

        if Path(test_path).exists():
            run_pytest(test_path)
        else:
            print(f"❌ Path not found: {test_path}")
    else:
        print("❌ Please provide test path")
