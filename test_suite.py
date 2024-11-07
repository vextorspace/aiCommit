import unittest
from commit_prompt import TestCommitPrompt
from commit_message import TestCommitMessage

def suite():
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()

    suite.addTests(loader.loadTestsFromTestCase(TestCommitPrompt))
    suite.addTests(loader.loadTestsFromTestCase(TestCommitMessage))

    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
