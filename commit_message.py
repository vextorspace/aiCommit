import commit_prompt
from git_diff import GitDiff
from commit_prompt import CommitPrompt

import os
import sys
import unittest
from unittest.mock import MagicMock

class CommitMessage:
    def __init__(self, gitDiff, commitPrompt = None):
        self.gitDiff = gitDiff
        self.commitPrompt = commitPrompt

    def is_good_commit(self):
        diff = self.gitDiff.get_diff()
        if diff == "":
            return False
        return True

    def get_commit_message(self):
        if self.is_good_commit() and self.commitPrompt is not None:
            diff = self.gitDiff.get_diff()
            return self.commitPrompt.get_commit_message(diff)
        return ""

class TestCommitMessage(unittest.TestCase):
    def test_no_diff_makes_bad_commit(self):
        mock_diff = MagicMock(spec=GitDiff)
        mock_diff.get_diff.return_value = ""

        commit_gen = CommitMessage(mock_diff)
        assert(commit_gen.is_good_commit() == False)

    def test_diff_makes_good_commit(self):
        mock_diff = MagicMock(spec=GitDiff)
        mock_diff.get_diff.return_value = "::ANY DIFF AT ALL::"

        commit_gen = CommitMessage(mock_diff)
        assert(commit_gen.is_good_commit() == True)

    def test_bad_diff_does_not_call_commit_prompt(self):
        mock_diff = MagicMock(spec=GitDiff)
        mock_diff.get_diff.return_value = ""

        mock_commit_prompt = MagicMock(spec=CommitPrompt)

        commit_gen = CommitMessage(mock_diff, mock_commit_prompt)
        commit_gen.get_commit_message()
        assert(mock_commit_prompt.get_commit_message.called == False)

    def test_good_diff_calls_commit_prompt(self):
        mock_diff = MagicMock(spec=GitDiff)
        mock_diff.get_diff.return_value = "::ANY DIFF AT ALL::"

        mock_commit_prompt = MagicMock(spec=CommitPrompt)

        commit_gen = CommitMessage(mock_diff, mock_commit_prompt)
        commit_gen.get_commit_message()
        assert(mock_commit_prompt.get_commit_message.called == True)

    def test_good_diff_returns_commit_message(self):
        mock_diff = MagicMock(spec=GitDiff)
        mock_diff.get_diff.return_value = "::ANY DIFF AT ALL::"

        mock_commit_prompt = MagicMock(spec=CommitPrompt)
        mock_commit_prompt.get_commit_message.return_value = "::COMMIT MESSAGE::"

        commit_gen = CommitMessage(mock_diff, mock_commit_prompt)
        assert(commit_gen.get_commit_message() == "::COMMIT MESSAGE::")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        repo_path = os.getcwd()
    else:
        repo_path = sys.argv[1]

    if not os.path.isdir(repo_path):
        print(f"Error: {repo_path} is not a valid directory")
        sys.exit(1)

    print(f"Using repo path: {repo_path}")
    git_diff = GitDiff(repo_path)
    commit_prompt = CommitPrompt()
    commit_message_generator = CommitMessage(git_diff, commit_prompt)
    print(commit_message_generator.get_commit_message())
