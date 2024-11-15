import unittest
from unittest.mock import MagicMock
from ai import Ai

class CommitPrompt:

    def __init__(self, ai =  Ai()):
        self.ai = ai

    def get_commit_message(self, diff):
        return self.ai.get_commit_message(f"{diff}")

class TestCommitPrompt(unittest.TestCase):
    def test_diff_packaged_with_prompt_to_ai(self):
        mockAi = MagicMock(spec=Ai)
        mockAi.get_commit_message.return_value = "::FAKE COMMIT MESSAGE::"
        commit_prompt = CommitPrompt(mockAi)
        assert(commit_prompt.get_commit_message("::DIFF::") == "::FAKE COMMIT MESSAGE::")
        expectedPrompt = f"::DIFF::"
        mockAi.get_commit_message.assert_called_once_with(expectedPrompt)
