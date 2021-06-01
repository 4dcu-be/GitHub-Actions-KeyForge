import ssl
from urllib.request import Request, urlopen
import json
from datetime import datetime


def get_keyforge(url='https://www.keyforgegame.com/api/decks/count/'):
    ssl_context = ssl._create_unverified_context()
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    with urlopen(req, context=ssl_context) as response:
        html = response.read()

    return json.loads(html.decode('utf-8'))


if __name__ == "__main__":

    count_dict = get_keyforge()

    with open("./data/keyforge_decks.tsv", mode='a+') as fout:
        print(datetime.now(), count_dict["count"], sep='\t', file=fout)