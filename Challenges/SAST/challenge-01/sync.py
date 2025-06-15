import os


def run_sync(target):
    command = "rsync " + target
    os.system(command)
