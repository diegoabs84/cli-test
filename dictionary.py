# Python
import requests, os
from tabulate import tabulate




def get_definition(word):
    api_key = os.getenv('MERRIAM_WEBSTER_API_KEY')
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={api_key}"
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()

    definitions = []
    for item in data:
        if 'shortdef' in item:
            pronunciation = item['hwi']['prs'][0]['mw'] if 'prs' in item['hwi'] else None
            part_of_speech = item['fl'] if 'fl' in item else None
            for definition in item['shortdef']:
                definition = definition.replace('\n', ' ')  # replace newline characters with spaces
                definitions.append([pronunciation, part_of_speech, definition])

    return tabulate(definitions, headers=["Pronunciation", "Type of Speech", "Definition"], tablefmt='orgtbl')