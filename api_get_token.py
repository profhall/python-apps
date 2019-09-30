
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
        self.head = API_Handle.new_token()

    def get_data(self, url):

        try:
            self.response = requests.get(url, headers=self.head)
            self.json = self.response.json()

            markets_with_stores = []
            markets_without_stores = []
            print("Got your data!")
        except Exception as e:
            print(f"UH Oh, Something went wrong with getting your data: {e}")


        return self.response


    @staticmethod
    def new_token():
        """
        This methods calls an API and to generate a token for use of an API
        :return: a header object to be used in API call ex: {'Authorization': 'Bearer ' + token}
        """
        data = [
            ('grant_type', 'client_credentials'),
        ]
        try:
            response = requests.post(os.environ['TOKEN_AUTH_DOMAIN'],
                                     data=data,
                                     auth=
                                        (
                                         os.environ['AUTH_CLIENT_ID'],
                                         os.environ['AUTH_CLIENT_SECRET']
                                        )
                                     )

            response_json =response.json()
            token = response_json["access_token"]
            # print(response.content)
            # print(response.json())
            # print(json.dumps(response.json(), indent=4))
            header = {'Authorization': 'Bearer ' + token}
            print("Got Token:", token)
        except Exception as error:
            header = "No_Token"
            print(f"Uh Oh! Something went wrong with getting the Token: {error}")

        #return the header that will be used OR alter this to just return the token
        return header



if __name__ == '__main__':
    markets_url = 'https://master-data-location.apps-np.homedepot.com/location/markets'
    markets = API_Handle()
    markets.get_data(markets_url)
    locations = API_Handle()



