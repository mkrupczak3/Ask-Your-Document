import os
import argparse
import openai
from pathlib import Path
from llama_index import GPTVectorStoreIndex, SimpleDirectoryReader, download_loader, StorageContext, load_index_from_storage
# You must obtain an API key from OpenAI for use of this script:
# https://platform.openai.com/account/api-keys
#
# TODO Replace this with your API key!
DEFAULT_OPENAI_API_KEY = 'YOUR_OPENAI_KEY_HERE'

def main():
    parser = argparse.ArgumentParser(description='Create a VectorStoreIndex from a PDF and query it.')
    parser.add_argument('pdf', help='The target PDF file')
    parser.add_argument('query', help='The query to run on the VectorStoreIndex')
    parser.add_argument('--key', default=DEFAULT_OPENAI_API_KEY, help='Your OpenAI API key')

    args = parser.parse_args()

    api_key = args.key or DEFAULT_OPENAI_API_KEY
    if api_key == 'YOUR_OPENAI_API_KEY':
        print("You must replace 'YOUR_OPENAI_API_KEY' with your actual OpenAI API key in the script, or provide it using the --key flag.")
        print("For example: python3 ask_your_document.py --key 'YOUR_OPENAI_API_KEY' 'document.pdf 'What is the title of this document?'")
        return

    os.environ["OPENAI_API_KEY"] = api_key

    storage_dir = Path('./storage')
    docstore_file = storage_dir / 'docstore.json'

    try:
        if docstore_file.is_file():
            storage_context = StorageContext.from_defaults(persist_dir=storage_dir)
            index = load_index_from_storage(storage_context)
        else:
            PDFReader = download_loader("PDFReader")
            loader = PDFReader()
            documents = loader.load_data(file=Path(args.pdf))

            index = GPTVectorStoreIndex.from_documents(documents)
            index.storage_context.persist()

        query_engine = index.as_query_engine()

        print(query_engine.query(args.query))
    except openai.error.AuthenticationError:
        print("An error occurred while trying to authenticate with the OpenAI API. Please ensure you've provided a valid API key.")


if __name__ == "__main__":
    main()
