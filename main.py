import re
import random
import requests


API_KEY = '6a783febcf5d65cff19161bb669734229dccfaa7'
API_URL = 'https://api.esv.org/v3/passage/text/'

CHAPTER_LENGTHS = [
  14, 18, 19, 16, 14, 20, 28, 13, 28, 39, 40
]


def get_passage():
    chapter = random.randrange(1, len(CHAPTER_LENGTHS))
    verse = random.randint(1, CHAPTER_LENGTHS[chapter])

    return 'Hebrews %s:%s' % (chapter, verse)


def get_esv_text(passage):
    params = {
        'q': passage,
        'indent-poetry': False,
        'include-headings': False,
        'include-footnotes': False,
        'include-verse-numbers': False,
        'include-short-copyright': False,
        'include-passage-references': False
    }

    headers = {
        'Authorization': 'Token %s' % API_KEY
    }

    data = requests.get(API_URL, params=params, headers=headers).json()

    text = re.sub('\s+', ' ', data['passages'][0]).strip()

    return '%s – %s' % (text, data['canonical'])


def render_esv_text(data):
    text = re.sub('\s+', ' ', data['passages'][0]).strip()

    return '%s – %s' % (text, data['canonical'])


if __name__ == '__main__':
    for i in range(3):
        print(get_esv_text(get_passage()))