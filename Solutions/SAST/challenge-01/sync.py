import subprocess


def run_sync(target):
    subprocess.run(["rsync", target], check=True)
