import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import JsonOutputParser

import unittest

load_dotenv()

class Ai:
    def __init__(self):
        self.llm = ChatOpenAI(
            model_name="gpt-4o",
            temperature=0,
            openai_api_key=os.getenv("OPENAI_API_KEY")
        )

    def get_commit_message(self, diff):
        prompt_template = """
                            You are a terse and efficient developer.
                            You only state the most important changes in commit messages.
                            each change should be on its own line.
                            each change message should be 50 characters or less.
                            the diff is: {diff}:

                            please write a non-generic commit message. """

        commit_prompt = ChatPromptTemplate.from_template(prompt_template)

        # Create the chain
        commit_chain = commit_prompt | self.llm

        # Run the chain
        commit = commit_chain.invoke({"diff": diff})
        return commit.content.strip()

class TestAi(unittest.TestCase):
    def test_loads_environment_variables(self):
        ai = Ai()
        assert(bool(os.getenv('OPENAI_API_KEY')))

    def test_get_commit_message(self):
        ai = Ai()
        message = ai.get_commit_message("Can you say hippo?")
        assert("hippo" in message.lower())
