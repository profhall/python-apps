
"""
title: api_get_token
author: Phillip Hall
date: 2019-09-23 15:35
"""

import requests
import json
import os

class API_Handle:
    """
    This class

    """

    def __init__(self):
        self.response = None
        # self.head = API_Handle.new_token()

    def get_data(self, url):

        try:
            token = '8hmsiwi4-4v04-n0v8:kouv-jdjiu2krnrc9'
            self.response = requests.get(url, headers={'Authorization': 'Basic ' + token})
            self.json = self.response.json()
            print(self.json)
            markets_with_stores = []
            markets_without_stores = []
            print("Got your data!")
        except Exception as e:
            print(f"UH Oh, Something went wrong with getting your data: {e}")


        return self.response





if __name__ == '__main__':
    markets_url = 'https://api.printful.com/'
    markets = API_Handle()
    markets.get_data(markets_url)
    locations = API_Handle()



