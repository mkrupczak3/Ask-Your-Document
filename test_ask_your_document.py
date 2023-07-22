import sys
import unittest
import ask_your_document
import tenacity

class TestAskYourDocument(unittest.TestCase):
    def setUp(self):
        try:
            with open('api.key', 'r') as key_file:
                self.OPENAI_API_KEY = key_file.read().strip()
                if not self.OPENAI_API_KEY:
                    print('Could not run tests: ', 'API key file is empty.')
                    sys.exit(1)
        except FileNotFoundError:
            print('Error', 'API key file not found.')
            sys.exit(1)

    def test_index_creation(self):
        sys.argv = ['test_ask_your_document.py', '--key', self.OPENAI_API_KEY, 'document.pdf', 'What is the title?']
        result = ask_your_document.main()
        self.assertIsNotNone(result)  # Update with a more specific assertion.

    def test_remote_call(self):
        sys.argv = ['test_ask_your_document.py', '--key', self.OPENAI_API_KEY, 'document.pdf', 'What is the title?']
        result = ask_your_document.main()
        self.assertIsNotNone(result)  # Update with a more specific assertion.

    def test_authentication_error(self):
        sys.argv = ['test_ask_your_document.py', '--key', 'incorrect_api_key', 'document.pdf', 'What is the title?']
        with self.assertRaises(tenacity.RetryError):  # It looks like a failed auth will cause a RetryError.
            ask_your_document.main()

if __name__ == '__main__':
    unittest.main()
