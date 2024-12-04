# commit_message
an ai coder that just makes all the tests in a file pass.

## Setup
to modify or use this in source format, you must install the python requirements. You can do this by running `pip install -r requirements.txt`
or by using pyenv to create a local environment first, then doing the above.

## to use in another program
- compile the ai_coder.py using pyinstaller ai_coder.spec
- place it in your path or in your project
- use: ```message=`commit_message`; git commit -am "$message" ```
