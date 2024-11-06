from git_diff import GitDiff
from commit_prompt import CommitPrompt

from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os
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





if __name__ == '__main__':
    unittest.main()
