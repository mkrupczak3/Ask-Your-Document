# Ask Your Document

Ask Your Document is a Python script that allows you to extract information from a PDF document using a query written in plain language. The script uses the OpenAI's text-davinci-003 model and llama-index library to read and understand the document, and then provides answers to your queries based on the content of the document.

## Prerequisites

- Python 3: If you don't already have Python 3 installed on your system, you can download it from the official Python [website](https://www.python.org/).
- OpenAI API Key: You will need to obtain an API key from OpenAI. You can get your API key from the OpenAI [website](https://platform.openai.com/account/api-keys).

## Installation

1. Clone the project from GitHub (requires [git](https://github.com/git-guides/install-git)):
    ```bash
    git clone https://github.com/mkrupczak3/Ask-Your-Document
    ```

2. Go into the project directory:
    ```bash
    cd ask_your_document
    ```

3. Set up a Python virtual environment:
    ```bash
    python3 -m venv env
    ```

4. Activate the virtual environment:
    ```bash
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

5. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

Once you've set up your environment and installed the necessary packages, you can use the `ask_your_document.py` script to query your PDF document.

```bash
python3 ask_your_document.py --key 'YOUR_OPENAI_API_KEY' 'path_to_your_document.pdf' 'Your query here'
```

Replace `'YOUR_OPENAI_API_KEY'` with your actual OpenAI API key, `'path_to_your_document.pdf'` with the path to the PDF document you want to query, and `'Your query here'` with your actual query.

For example, if your OpenAI API key is `abcd1234`, the document you want to query is `document.pdf` located in the same directory, and your query is "What is the title of this document?", you would run:

```bash
python3 ask_your_document.py --key 'abcd1234' 'document.pdf' 'What is the title of this document?'
```

## Notes

If you encounter an error while trying to authenticate with the OpenAI API, please ensure you've provided a valid API key. You can either replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key in the script, or provide it using the `--key` flag when you run the script.