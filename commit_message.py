from get_git_diff import GitDiff
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from dotenv import load_dotenv
import os
import unittest
from unittest.mock import MagicMock

class CommitMessage:
    def __init__(self, gitDiff):
        self.gitDiff = gitDiff

    def is_good_commit(self):
        diff = self.gitDiff.get_diff()
        if diff == "":
            return False
        return True

class TestCommitMessage(unittest.TestCase):
    def test_no_diff_makes_bad_commit(self):
        mock_diff = MagicMock(spec=GitDiff)

        mock_diff.get_diff.return_value = ""

        commit_gen = CommitMessage(mock_diff)
        assert(commit_gen.is_good_commit() == False)






if __name__ == '__main__':
    unittest.main()
