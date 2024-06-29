import unittest, os, pytest
from unittest.mock import patch, Mock
from dictionary import get_definition

class TestCLI(unittest.TestCase):
    @patch('requests.get')
    def test_get_definition(self, mock_get):
        # Set up the mock response
        mock_response = Mock()
        mock_response.json.return_value = [{
            'shortdef': ['mock definition'],
            'hwi': {'prs': [{'mw': 'mock pronunciation'}]},
            'fl': 'mock part of speech'
        }]
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        # Call the function
        definition = get_definition('word')

        # Check the result
        expected_definition = '| Pronunciation      | Type of Speech      | Definition      |\n|--------------------+---------------------+-----------------|\n| mock pronunciation | mock part of speech | mock definition |'
        self.assertEqual(definition, expected_definition)

        # Check the API call
        mock_get.assert_called_once_with('https://www.dictionaryapi.com/api/v3/references/collegiate/json/word?key=' + os.getenv('MERRIAM_WEBSTER_API_KEY'))

if __name__ == "__main__":
    pytest.main(['--junitxml=test_results.xml'])