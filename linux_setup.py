import subprocess

# Using a shell pipeline to find python files
try:
    cmd = "ls"
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, check=True)

    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(f"Script failed due to:\n{e}")