import subprocess

class GitDiff:
    def __init__(self, path):
        self.path = path

    def get_diff(self):
        return subprocess.check_output(['git', 'diff', '-U10', 'HEAD', self.path])
