# Project

This is a command-line interface (CLI) application built in Python. This CLI allows you to query the Merriam-Webster dictionary API and search for word meanings.

## Installation

First, clone the repository. Then, navigate to the repository root folder and install the requirements:

pip install -r requirements.txt

## Usage

You can run the application directly from the terminal:

python main.py

Or you can use it with Docker:

docker build -t cli:1.0 .

Then run the application:

docker run -it --rm cli:1.0

## Tests

To run the tests, you can use:

pytest --junitxml=test_results.xml

This will create a xml file with the test results.



