import json
import os

import pandas as pd
from stocksymbol import StockSymbol


def fetch_index_list(api_key="6924cf46-6be5-41c7-ac63-575ba490e538"):
    if not os.path.exists('data/index_list.json'):
        ss = StockSymbol(api_key)
        symbol_list_us = ss.get_symbol_list(market="US")

        # Remove Unnecessary Data
        for index in symbol_list_us:
            del index['market']
            del index['quoteType']

        with open('data/index_list.json', 'w') as f:
            json.dump(symbol_list_us, f)
            return symbol_list_us

    with open('data/index_list.json', 'r') as f:
        index_list = json.load(f)
        return index_list

index_list = fetch_index_list()

def find_companies(title, article_data):
    title_lower = title.lower()
    article_data_lowercase = article_data.lower()

    found_in_article = []
    definitely_found = []

    # Loop through the index list and check if the short name or symbol is in the lowercased article and

    for index in index_list: 
        if (' ' + index['shortName'].lower() + ' ' in article_data_lowercase):
            if (' ' + index['longName'] + ' ' in article_data):
                found_in_article.append(index['symbol'])
                
                if  (index['longName'] in title) or (index['shortName'].lower() in title_lower):
                    definitely_found.append(index['symbol'])
                
            # print('Only short name matched: ' + index['shortName'], index["longName"], index["symbol"])
    return  found_in_article, definitely_found

lines = pd.read_csv('500_data.csv').to_numpy()

for line in lines:
    found_in_article, definitely_found = find_companies(line[5], line[6])
    if len(found_in_article) > 0:
        print(line[7], found_in_article, definitely_found)
