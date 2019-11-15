
"""
title: api_get_token
author: Phillip Hall
date: 2019-09-23 15:35
"""

import requests, json
from certauth.certauth import main, CertificateAuthority, FileCache, LRUCache, ROOT_CA
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

class API_Handle:
    """
    This class

    """

    def __init__(self):
        self.response = None
        # self.head = API_Handle.new_token()

    def get_data(self, url):
        ca = CertificateAuthority('My Custom CA', 'my-ca.pem', cert_cache='/tmp/certs')
        filename = ca.cert_for_host('geocoder.api.here.com')
        try:
            params = (
                ('searchtext', ' Marietta Technology Center Marietta Georgia'),
                ('app_id', 'TnPtPQJjC8hmv4YHd0bd'),
                ('app_code', 'e3AyX5YC_k_XE9ATggMWPw'),
                ('gen', '8'),
            )

            self.response = requests.get(url, params=params, verify=False)
            # self.response = requests.get(url, params=params, verify='my-ca.pem')
            self.json = self.response.json()
            print(json.dumps(self.json, indent= 4))
            print("Got your data!")
        except Exception as e:
            print(f"UH Oh, Something went wrong with getting your data: {e}")


        return self.response






if __name__ == '__main__':
    markets_url = 'https://geocoder.api.here.com/6.2/geocode.json'
    markets = API_Handle()
    markets.get_data(markets_url)



