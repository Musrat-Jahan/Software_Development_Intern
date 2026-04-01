import os
import subprocess
import sys

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))


def run_script(script_name: str):
    script_path = os.path.join(CURRENT_DIR, script_name)
    print(f"\nRunning {script_name}...")
    result = subprocess.run([sys.executable, script_path], check=True)
    return result.returncode


def main():
    run_script("extract_data.py")
    run_script("eda.py")
    run_script("preprocess.py")
    run_script("train_lead_model.py")
    try:
        run_script("train_revenue_model.py")
    except subprocess.CalledProcessError:
        print("Revenue model training skipped because data was insufficient or unavailable.")
    print("\nAll pipeline steps finished.")


if __name__ == "__main__":
    main()
