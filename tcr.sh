#!/bin/sh

echo "Running tests..."
python test_suite.py

# Store the test result
TEST_RESULT=$?

# Check if tests failed
if [ $TEST_RESULT -ne 0 ]; then
    echo "Tests failed! Removing changes..."
    git reset --hard HEAD
else
    echo "Tests passed! Committing..."
    git add .
    COMMIT_MESSAGE=`commit_message`
    git commit -m "$COMMIT_MESSAGE"
fi

exit 0
