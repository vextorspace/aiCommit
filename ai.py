import os
import unittest
from dotenv import load_dotenv

load_dotenv()

class Ai:
    def __init__(self):
        pass

    def get_commit_message(self, prompt):
        pass

class TestAi(unittest.TestCase):
    def test_loads_environment_variables(self):
        ai = Ai()
        assert(bool(os.getenv('OPENAI_API_KEY')))
