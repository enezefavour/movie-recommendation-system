import requests
import os
import sys

URL = 'https://files.grouplens.org/datasets/movielens/'
SMALL_DATA_SET = 'ml-latest-small.zip'
LARGE_DATA_SET = 'ml-latest.zip'

def download(download_type):
    filename = download_type
    download_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

    response = requests.get(URL + download_type, stream=True);
    with open(download_path, 'wb') as f:
        f.write(response.content)


def get_datasets():
    arguments = {
        'small': 'small',
        'large': 'large'
    }

    if len(sys.argv) < 2:
        download(SMALL_DATA_SET)
    else:
        arg = arguments.get(sys.argv[1])
        if (arg.lower() == 'small'):
            download(SMALL_DATA_SET)
        elif (arg.lower() == 'large'):
            download(LARGE_DATA_SET)


if __name__ == '__main__':
    get_datasets()
