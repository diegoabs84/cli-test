# Project

This is a command-line interface (CLI) application built in Python. This CLI allows you to query the Merriam-Webster dictionary API and search for word meanings.

## Installation

First, clone the repository. Then, navigate to the repository root folder and install the requirements:

pip install -r requirements.txt

## Usage
First, you need to set an environment variable. This one will be your api-key, which you should create at the Merriem webster website.
You should call it "MERRIAM_WEBSTER_API_KEY", then you assign to it your api-key.

After that, you can run the application directly from the terminal:

python main.py

Or you can use it with Docker. First build the image:

docker build -t cli:1.0 .

Then run the application. Since you are using Docker, you should pass the environment variable on the command to run it, like this:

docker run -it -e MERRIAM_WEBSTER_API_KEY=your_api_key cli:1.0

## Tests

To run the tests, you can use:

pytest --junitxml=test_results.xml

This will create a xml file with the test results.



